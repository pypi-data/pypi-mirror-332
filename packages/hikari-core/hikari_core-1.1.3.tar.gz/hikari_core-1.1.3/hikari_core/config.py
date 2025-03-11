from typing import Optional

from loguru import logger
from pydantic import BaseModel

from .data_source import dir_path


class Config_Model(BaseModel):
    proxy: Optional[str]
    http2: bool = True
    token: Optional[str] = '123456:111111111111'
    auto_rendering: bool = True
    auto_image: bool = True
    use_broswer: Optional[str] = 'chromium'
    game_path: Optional[str] = f'{dir_path}/game'
    yuyuko_url: Optional[str] = 'https://v3-api.wows.shinoaki.com:8443'
    yuyuko_type: Optional[str] = 'BOT'


hikari_config = Config_Model()


def set_hikari_config(  # noqa: PLR0913
    proxy: Optional[str],
    http2: bool = True,
    token: Optional[str] = '123456:111111111111',
    auto_rendering: bool = True,
    auto_image: bool = True,
    use_broswer: Optional[str] = 'chromium',
    game_path: Optional[str] = f'{dir_path}/game',
    yuyuko_url: Optional[str] = 'https://v3-api.wows.shinoaki.com:8443',
    yuyuko_type: Optional[str] = 'BOT',
):
    """配置Hikari-core

    Args:
        proxy (str): 访问WG使用的代理，格式http://localhost:7890
        http2 (bool): 是否开启http2，默认启用
        token (str): #请加群联系雨季获取api_key和token Q群:967546463
        auto_rendering (bool): 自动填充模板，默认启用
        auto_image (bool): 是否自动渲染，默认启用，若auto_rending未启用则该项配置无效
        use_broswer (str): chromium/firefox，默认chromium，性能大约为firefox三倍
        game_path (str):缓存文件夹路径，推荐设置在bot目录下，不配置默认为core目录下game
        yuyuko_url (str):yuyuko请求地址
    """
    global hikari_config  # noqa: PLW0602
    hikari_config.proxy = proxy
    hikari_config.http2 = http2
    hikari_config.token = token
    hikari_config.auto_rendering = auto_rendering
    hikari_config.auto_image = auto_image
    hikari_config.use_broswer = use_broswer
    hikari_config.game_path = game_path
    hikari_config.yuyuko_url = yuyuko_url
    hikari_config.yuyuko_type = yuyuko_type
    logger.info(f'当前hikari-core配置\n{hikari_config}')
