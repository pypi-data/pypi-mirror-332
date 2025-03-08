from nonebot_plugin_apscheduler import scheduler
from .database import async_session
from .models import GroupMessageStat
from datetime import datetime

@scheduler.scheduled_job("cron", hour=0, timezone="Asia/Shanghai")
async def daily_reset():
    """每日凌晨重置数据"""
    async with async_session() as session:
        await session.execute(
            update(GroupMessageStat)
            .values(message_count=0)
        )
        await session.commit()