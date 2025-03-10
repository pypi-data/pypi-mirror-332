# setup.py
from setuptools import setup, find_packages

setup(
    name="xx_game_module",
    version="1.0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "xx_game_module=game_module.cli:main"  # 确保cli.py中存在main函数
        ]
    },
    install_requires=[],  # argparse已包含在Python标准库，无需特别声明
    # 新增元数据
    author="xx_game_author",
    description="Game module CLI tool",
    python_requires=">=3.6",
    include_package_data=True,
)
