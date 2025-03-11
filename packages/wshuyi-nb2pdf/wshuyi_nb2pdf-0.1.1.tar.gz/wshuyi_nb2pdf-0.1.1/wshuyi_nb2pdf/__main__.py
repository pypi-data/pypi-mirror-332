#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
wshuyi-nb2pdf主程序入口点
允许作为模块直接运行: python -m wshuyi_nb2pdf
"""

import sys
from .cli import main

if __name__ == "__main__":
    sys.exit(main())
