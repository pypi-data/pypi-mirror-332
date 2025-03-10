#!/usr/bin/env python3
# game_module/cli.py
import os
import argparse
import subprocess
import shutil
from pathlib import Path
import tempfile


def install_repository(repository: str, target_dir: str):
    """克隆Gitee仓库到指定路径"""
    try:
        # 构建完整仓库URL‌:ml-citation{ref="1,4" data="citationList"}
        repo_url = f"https://gitee.com/{repository}.git"
        # 外层临时目录变量保持原名
        with tempfile.TemporaryDirectory() as temp_clone:
            # 执行克隆到临时目录
            subprocess.run(
                ["git", "clone", repo_url, temp_clone], 
                check=True, 
                capture_output=True
            )
            target_path = Path(target_dir).resolve()

            # 清理目标目录（如果存在）
            if target_path.exists():
                shutil.rmtree(target_path, ignore_errors=True)

            # 从临时目录复制到目标目录
            shutil.copytree(
                temp_clone, 
                target_path,
                ignore=shutil.ignore_patterns(".git")
            )

            print(f"✅ 成功克隆到: {target_path}")
        print(f"✅ 成功克隆到: {target_path}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Git操作失败: {e.stderr.decode()}")
    except Exception as e:
        print(f"❌ 系统错误: {str(e)} ")
    finally:
        # 自动清理临时目录（TemporaryDirectory上下文已自动处理）
        pass


try:
    inner_temp_clone_path = Path(inner_temp_clone)
    if inner_temp_clone_path.exists():
        shutil.rmtree(inner_temp_clone_path)
except NameError:
    pass


def main():
    # 命令行参数解析‌:ml-citation{ref="1" data="citationList"}
    parser = argparse.ArgumentParser(description="Gitee仓库安装工具")
    parser.add_argument("command", choices=["install"])
    parser.add_argument("repository")
    parser.add_argument("target_dir")

    args = parser.parse_args()

    if args.command == "install":
        install_repository(args.repository, args.target_dir)


if __name__ == "__main__":
    main()
