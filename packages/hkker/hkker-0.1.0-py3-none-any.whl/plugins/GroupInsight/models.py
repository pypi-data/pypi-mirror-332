from sqlalchemy import Column, Integer, String, DateTime, UniqueConstraint
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class GroupMessageStat(Base):
    """群消息统计表"""
    __tablename__ = "group_message_stats"

    id = Column(Integer, primary_key=True, autoincrement=True)  # 正确设置自增
    group_id = Column(String(20), nullable=False)  # 群号
    user_id = Column(String(20), nullable=False)  # 用户QQ
    message_count = Column(Integer, default=0)  # 消息计数
    last_active = Column(DateTime)  # 最后活跃时间

    # 正确格式的 __table_args__
    __table_args__ = (
        UniqueConstraint("group_id", "user_id", name="uq_group_user"),  # 唯一约束示例
        {"extend_existing": True}  # 合并参数到单个字典
    )