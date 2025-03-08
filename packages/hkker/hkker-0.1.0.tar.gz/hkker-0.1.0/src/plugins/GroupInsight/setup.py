from setuptools import setup, find_packages

setup(
    name="nonebot-plugin-group-insight",
    version="0.0.1",
    description="NoneBot2 插件：群聊消息统计与排行榜",
    long_description=open("README.md", encoding="utf-8").read(),
    long_description_content_type="text/markdown",
    author="wohaokunr",
    author_email="wohaokunr@gmail.com",
    packages=find_packages(),
    install_requires=[
        "nonebot2",
        "nonebot-plugin-apscheduler",
        "sqlalchemy",
        "aiosqlite",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.11",
    entry_points={
        'nonebot.plugins': [
            'nonebot_plugin_group_insight = nonebot_plugin_group_insight',
        ],
    },
)
