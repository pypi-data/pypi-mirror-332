from nonebot import on_message
from nonebot.adapters.onebot.v11 import GroupMessageEvent
from .database import async_session
from .models import GroupMessageStat
from sqlalchemy import select
from datetime import datetime

msg_handler = on_message(priority=10, block=False)


@msg_handler.handle()
async def handle_message(event: GroupMessageEvent):
    async with async_session() as session:
        # 查询或创建记录
        result = await session.execute(
            select(GroupMessageStat).where(
                GroupMessageStat.group_id == str(event.group_id),
                GroupMessageStat.user_id == str(event.user_id)
            )
        )
        stat = result.scalar_one_or_none()

        if stat:
            stat.message_count += 1
            stat.last_active = datetime.now()
        else:
            stat = GroupMessageStat(
                group_id=str(event.group_id),
                user_id=str(event.user_id),
                message_count=1,
                last_active=datetime.now()
            )
            session.add(stat)

        await session.commit()