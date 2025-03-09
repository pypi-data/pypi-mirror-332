from nonebot import on_notice
from nonebot.adapters.onebot.v11 import GroupAdminNoticeEvent
from nonebot.plugin import PluginMetadata
from zhenxun_utils.enum import PluginType
from zhenxun_utils.log import logger

from ....models.level_user import LevelUser
from ...config import ZxpmConfig
from ...extra import PluginExtraData
from ...rules import notice_rule

__plugin_meta__ = PluginMetadata(
    name="群管理员变动监测",
    description="""检测群管理员变动, 添加与删除管理员默认权限,
    当配置项 ADMIN_DEFAULT_AUTH 为空时, 不会添加管理员权限""",
    usage="",
    extra=PluginExtraData(
        author="HibiKier",
        version="0.1",
        plugin_type=PluginType.HIDDEN,
    ).to_dict(),
)


admin_notice = on_notice(priority=5, rule=notice_rule(GroupAdminNoticeEvent))


@admin_notice.handle()
async def _(event: GroupAdminNoticeEvent):
    if event.sub_type == "set":
        admin_default_auth = ZxpmConfig.zxpm_admin_default_auth
        if admin_default_auth is not None:
            await LevelUser.set_level(
                str(event.user_id),
                str(event.group_id),
                admin_default_auth,
            )
            logger.info(
                f"成为管理员，添加权限: {admin_default_auth}",
                "群管理员变动监测",
                session=event.user_id,
                group_id=event.group_id,
            )
        else:
            logger.warning(
                "配置项 MODULE: [<u><y>admin_bot_manage</y></u>] |"
                " KEY: [<u><y>ADMIN_DEFAULT_AUTH</y></u>] 为空"
            )
    elif event.sub_type == "unset":
        await LevelUser.delete_level(str(event.user_id), str(event.group_id))
        logger.info(
            "撤销群管理员, 取消权限等级",
            "群管理员变动监测",
            session=event.user_id,
            group_id=event.group_id,
        )
