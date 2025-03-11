#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
wshuyi-nb2pdf 命令行接口
"""

import argparse
import sys
from pathlib import Path
from typing import List, Optional

from .converter import convert_notebook

def parse_args(args: Optional[List[str]] = None) -> argparse.Namespace:
    """解析命令行参数"""
    parser = argparse.ArgumentParser(
        description="将Jupyter Notebook转换为格式优化的PDF文件，确保代码不会被截断。"
    )
    
    parser.add_argument("notebook_path", help="要转换的Jupyter Notebook文件的路径")
    parser.add_argument("output_path", nargs="?", default=None, help="输出PDF文件的路径 (可选，默认为notebook同名PDF)")
    
    # 转换选项
    parser.add_argument("--portrait", action="store_true", help="使用纵向布局 (默认为横向)")
    parser.add_argument("--scale", type=float, default=0.9, help="PDF缩放比例 (默认: 0.9)")
    parser.add_argument("--paper-size", default="Letter", help="纸张大小 (例如: A4, Letter, 默认: Letter)")
    parser.add_argument("--html-template", default="full", help="HTML模板 (默认: full)")
    parser.add_argument("--wait-time", type=int, default=2000, help="等待时间(毫秒)以确保完全加载 (默认: 2000)")
    
    return parser.parse_args(args)

def main(args: Optional[List[str]] = None) -> int:
    """命令行入口点"""
    parsed_args = parse_args(args)
    
    try:
        options = {
            "landscape": not parsed_args.portrait,
            "scale": parsed_args.scale,
            "format": parsed_args.paper_size,
            "wait_time": parsed_args.wait_time
        }
        
        output_path = convert_notebook(
            parsed_args.notebook_path,
            parsed_args.output_path,
            html_template=parsed_args.html_template,
            options=options
        )
        
        print(f"✓ 成功将Notebook转换为PDF: {output_path}")
        return 0
        
    except Exception as e:
        print(f"错误: {str(e)}", file=sys.stderr)
        return 1

if __name__ == "__main__":
    sys.exit(main())
