from nonebot.adapters import Bot, Event
from nonebot.exception import IgnoredException
from nonebot.matcher import Matcher
from nonebot.message import run_preprocessor
from nonebot.typing import T_State
from nonebot_plugin_alconna import At
from nonebot_plugin_session import EventSession
from zhenxun_utils.enum import PluginType
from zhenxun_utils.log import logger
from zhenxun_utils.message import MessageUtils

from ....models.ban_console import BanConsole
from ....models.group_console import GroupConsole
from ...config import ZxpmConfig
from ...extra.limit import FreqLimiter

_flmt = FreqLimiter(300)


# 检查是否被ban
@run_preprocessor
async def _(
    matcher: Matcher, bot: Bot, event: Event, state: T_State, session: EventSession
):
    if plugin := matcher.plugin:
        if metadata := plugin.metadata:
            extra = metadata.extra
            if extra.get("plugin_type") in [PluginType.HIDDEN, PluginType.DEPENDANT]:
                return
    user_id = session.id1
    group_id = session.id3 or session.id2
    if group_id:
        if user_id in bot.config.superusers:
            return
        if await BanConsole.is_ban(None, group_id):
            logger.debug("群组处于黑名单中...", "ban_hook")
            raise IgnoredException("群组处于黑名单中...")
        if g := await GroupConsole.get_group(group_id):
            if g.level < 0:
                logger.debug("群黑名单, 群权限-1...", "ban_hook")
                raise IgnoredException("群黑名单, 群权限-1..")
    if user_id:
        ban_result = ZxpmConfig.zxpm_ban_reply
        if user_id in bot.config.superusers:
            return
        if await BanConsole.is_ban(user_id, group_id):
            time = await BanConsole.check_ban_time(user_id, group_id)
            if time == -1:
                time_str = "∞"
            else:
                time = abs(int(time))
                if time < 60:
                    time_str = f"{time!s} 秒"
                else:
                    minute = int(time / 60)
                    if minute > 60:
                        hours = minute // 60
                        minute %= 60
                        time_str = f"{hours} 小时 {minute}分钟"
                    else:
                        time_str = f"{minute} 分钟"
            if (
                time != -1
                and ban_result
                and _flmt.check(user_id)
                and ZxpmConfig.zxpm_ban_reply
            ):
                _flmt.start_cd(user_id)
                await MessageUtils.build_message(
                    [
                        At(flag="user", target=user_id),
                        f"{ban_result}\n在..在 {time_str} 后才会理你喔",
                    ]
                ).send()
            logger.debug("用户处于黑名单中...", "ban_hook")
            raise IgnoredException("用户处于黑名单中...")
