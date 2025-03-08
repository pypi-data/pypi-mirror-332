from nonebot import on_command
from nonebot.adapters.onebot.v11 import GroupMessageEvent, Message
from .database import async_session
from .models import GroupMessageStat
from sqlalchemy import select, func

rank_cmd = on_command("发言排行", aliases={"排行榜"}, priority=5)


@rank_cmd.handle()
async def show_rank(event: GroupMessageEvent):
    async with async_session() as session:
        result = await session.execute(
            select(
                GroupMessageStat.user_id,
                GroupMessageStat.message_count
            )
            .where(GroupMessageStat.group_id == str(event.group_id))
            .order_by(GroupMessageStat.message_count.desc())
            .limit(10)
        )

        rank_data = result.all()
        if not rank_data:
            await rank_cmd.finish("暂无统计数据")

        msg = "【今日发言排行榜】\n"
        for index, (user_id, count) in enumerate(rank_data):
            msg += f"{index + 1}. @{user_id} - {count}次\n"

        await rank_cmd.finish(Message(msg))