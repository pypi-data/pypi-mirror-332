from nonebot.plugin import PluginMetadata
from nonebot.plugin import require
require("nonebot_plugin_localstore")
require("nonebot_plugin_uninfo")
from .conf import *
from .resources import *
from .suggar import *
from .API import *
from .conf import __KERNEL_VERSION__


__plugin_meta__ = PluginMetadata(
    name="SuggarChat OpenAI协议聊天插件",
    description="强大的聊天插件，支持OpenAI协议，多模型切换，完全的上下文支持，适配Nonebot2-Onebot-V11适配器",
    usage="按照Readme.md修改配置文件后使用，默认enable为false！",
    homepage="https://github.com/JohnRichard4096/nonebot_plugin_suggarchat/",
    type="application",
    supported_adapters={"~onebot.v11"},
)
