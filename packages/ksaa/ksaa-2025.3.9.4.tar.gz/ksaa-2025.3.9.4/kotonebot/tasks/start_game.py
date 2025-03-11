"""启动游戏，领取登录奖励，直到首页为止"""
import logging

from kotonebot import task, device, image, cropped, AdaptiveWait, sleep, ocr
from kotonebot.errors import GameUpdateNeededError
from . import R
from .common import Priority
from .actions.loading import loading
from .actions.scenes import at_home, goto_home
from .actions.commu import is_at_commu, handle_unread_commu
logger = logging.getLogger(__name__)

@task('启动游戏', priority=Priority.START_GAME)
def start_game():
    """
    启动游戏，直到游戏进入首页为止。
    
    执行前游戏必须处于未启动状态。
    """
    # TODO: 包名放到配置文件里
    if device.current_package() == 'com.bandainamcoent.idolmaster_gakuen':
        logger.info("Game already started")
        if not at_home():
            logger.info("Not at home, going to home")
            goto_home()
        return
    device.launch_app('com.bandainamcoent.idolmaster_gakuen')
    # [screenshots/startup/1.png]
    image.wait_for(R.Daily.ButonLinkData, timeout=30)
    sleep(2)
    device.click_center()
    wait = AdaptiveWait(timeout=240, timeout_message='Game startup loading timeout')
    while True:
        while loading():
            wait()
        with device.pinned():
            if image.find(R.Daily.ButtonHomeCurrent):
                break
            # [screenshots/startup/update.png]
            elif image.find(R.Common.TextGameUpdate):
                device.click(image.expect(R.Common.ButtonConfirm))
            # [kotonebot-resource/sprites/jp/daily/screenshot_apk_update.png]
            elif ocr.find('アップデート', rect=R.Daily.BoxApkUpdateDialogTitle):
                raise GameUpdateNeededError()
            # [screenshots/startup/announcement1.png]
            elif image.find(R.Common.ButtonIconClose):
                device.click()
            # [screenshots/startup/birthday.png]
            elif handle_unread_commu():
                pass
            else:
                device.click_center()
            wait()

if __name__ == '__main__':
    import logging
    logging.basicConfig(level=logging.INFO, format='[%(asctime)s] [%(levelname)s] [%(name)s] [%(funcName)s] [%(lineno)d] %(message)s')
    logger.setLevel(logging.DEBUG)
    start_game()

