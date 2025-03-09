from datetime import datetime, timedelta
from typing import Literal
from typing_extensions import Self

from tortoise import fields
from tortoise.functions import Count
from zhenxun_db_client import Model


class ChatHistory(Model):
    id = fields.IntField(pk=True, generated=True, auto_increment=True)
    """自增id"""
    user_id = fields.CharField(255)
    """用户id"""
    group_id = fields.CharField(255, null=True)
    """群聊id"""
    text = fields.TextField(null=True)
    """文本内容"""
    plain_text = fields.TextField(null=True)
    """纯文本"""
    create_time = fields.DatetimeField(auto_now_add=True)
    """创建时间"""
    bot_id = fields.CharField(255, null=True)
    """bot记录id"""
    platform = fields.CharField(255, null=True)
    """平台"""

    class Meta:  # type: ignore
        table = "chat_history"
        table_description = "聊天记录数据表"

    @classmethod
    async def get_group_msg_rank(
        cls,
        gid: str | None,
        limit: int = 10,
        order: str = "DESC",
        date_scope: tuple[datetime, datetime] | None = None,
    ) -> list[Self]:
        """获取排行数据

        参数:
            gid: 群号
            limit: 获取数量
            order: 排序类型，desc，des
            date_scope: 日期范围
        """
        o = "-" if order == "DESC" else ""
        query = cls.filter(group_id=gid) if gid else cls
        if date_scope:
            query = query.filter(create_time__range=date_scope)
        return list(
            await query.annotate(count=Count("user_id"))
            .order_by(f"{o}count")
            .group_by("user_id")
            .limit(limit)
            .values_list("user_id", "count")
        )  # type: ignore

    @classmethod
    async def get_group_first_msg_datetime(
        cls, group_id: str | None
    ) -> datetime | None:
        """获取群第一条记录消息时间

        参数:
            group_id: 群组id
        """
        if group_id:
            message = (
                await cls.filter(group_id=group_id).order_by("create_time").first()
            )
        else:
            message = await cls.all().order_by("create_time").first()
        return message.create_time if message else None

    @classmethod
    async def get_message(
        cls,
        uid: str,
        gid: str,
        type_: Literal["user", "group"],
        msg_type: Literal["private", "group"] | None = None,
        days: int | tuple[datetime, datetime] | None = None,
    ) -> list[Self]:
        """获取消息查询query

        参数:
            uid: 用户id
            gid: 群聊id
            type_: 类型，私聊或群聊
            msg_type: 消息类型，用户或群聊
            days: 限制日期
        """
        if type_ == "user":
            query = cls.filter(user_id=uid)
            if msg_type == "private":
                query = query.filter(group_id__isnull=True)
            elif msg_type == "group":
                query = query.filter(group_id__not_isnull=True)
        else:
            query = cls.filter(group_id=gid)
            if uid:
                query = query.filter(user_id=uid)
        if days:
            if isinstance(days, int):
                query = query.filter(
                    create_time__gte=datetime.now() - timedelta(days=days)
                )
            elif isinstance(days, tuple):
                query = query.filter(create_time__range=days)
        return await query.all()  # type: ignore

    @classmethod
    async def _run_script(cls):
        return []
