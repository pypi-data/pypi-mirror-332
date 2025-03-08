import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker

# 确保目录存在
db_path = os.path.abspath("data/chat_stats.db")
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# 异步引擎
async_engine = create_async_engine(
    f"sqlite+aiosqlite:///{db_path}",
    echo=True  # 开启日志便于调试
)

# 同步引擎
sync_engine = create_engine(
    f"sqlite:///{db_path}",
    echo=True
)

# 会话工厂（修正为 async_sessionmaker）
async_session = async_sessionmaker(
    bind=async_engine,
    expire_on_commit=False
)

async def init_db():
    """初始化数据库"""
    from .models import Base
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
