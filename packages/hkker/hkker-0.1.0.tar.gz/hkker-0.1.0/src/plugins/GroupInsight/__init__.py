from nonebot import require, get_driver
from nonebot.plugin import PluginMetadata
from .database import init_db

# 先加载 apscheduler 插件
require("nonebot_plugin_apscheduler")

# 再导入其他模块
from . import commands, message_handler, scheduler_tasks

# 插件元数据
__plugin_meta__ = PluginMetadata(
    name="群聊统计",
    description="群聊消息统计与排行榜功能",
    usage="发送'发言排行'查看统计",
    type="application",
    extra={"version": "1.0.0"}
)

# 插件初始化
async def plugin_init():
    await init_db()

driver = get_driver()
driver.on_startup(plugin_init)
