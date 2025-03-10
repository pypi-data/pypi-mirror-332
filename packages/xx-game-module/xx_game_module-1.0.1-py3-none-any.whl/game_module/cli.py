#!/usr/bin/env python3
# game_module/cli.py
import os
import argparse
import subprocess
import shutil
from pathlib import Path
import tempfile

def install_repository(repository: str, target_dir: str = os.getcwd()):
    """克隆Gitee仓库到指定路径"""
    try:
        repo_url = f"https://gitee.com/{repository}.git"
        with tempfile.TemporaryDirectory() as temp_clone:
            subprocess.run(
                ["git", "clone", repo_url, temp_clone], 
                check=True, 
                capture_output=True
            )
            target_path = Path(target_dir).resolve()

            if target_path.exists():
                shutil.rmtree(target_path, ignore_errors=True)

            shutil.copytree(
                temp_clone, 
                target_path,
                ignore=shutil.ignore_patterns(".git"),
                dirs_exist_ok=True
            )

            print(f"✅ 成功克隆到: {target_path}")

    except subprocess.CalledProcessError as e:
        print(f"❌ Git操作失败: {e.stderr.decode()}")
    except Exception as e:
        print(f"❌ 系统错误: {str(e)} ")

def main():
    parser = argparse.ArgumentParser(description="Gitee仓库安装工具")
    parser.add_argument("command", choices=["install"])
    parser.add_argument("repository")
    parser.add_argument("target_dir", nargs='?', default=os.getcwd(), help='目标目录（默认为当前目录）')

    args = parser.parse_args()

    if args.command == "install":
        install_repository(args.repository, args.target_dir)

if __name__ == "__main__":
    main()