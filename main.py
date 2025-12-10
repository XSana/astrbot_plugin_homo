from decimal import Decimal

from astrbot.api import logger
from astrbot.api.event import AstrMessageEvent, filter
from astrbot.api.star import Context, Star, register
from astrbot.core import AstrBotConfig
from data.plugins.astrbot_plugin_homo.homo import homo


@register("homo", "XSana", "将任意数字强行论证为 114514 相关算式", "114.514.1919810")
class Homo(Star):
    def __init__(self, context: Context, config: AstrBotConfig):
        super().__init__(context)

        self.config = config
        self.escape_markdown = self.config.get("escape_markdown", True)

    @filter.command("homo", alias={"恶臭论证"})
    async def abbr(self, event: AstrMessageEvent, num: Decimal):
        expr = homo(num)
        result_text = f"{num} = {expr}"

        if self.escape_markdown:
            escaped_text = result_text.replace("*", r"\*")
        else:
            escaped_text = result_text

        yield event.plain_result(escaped_text)
        event.stop_event()

    async def terminate(self):
        logger.info("[homo] plugin terminated")
