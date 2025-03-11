"""
wshuyi-nb2pdf - 将Jupyter Notebook转换为优化的PDF格式
==================================================

这个包提供了将Jupyter Notebook转换为PDF的功能，特别关注：
- 确保代码不会在右侧被截断
- 使用合适的字体大小
- 优化分页和布局
- 支持中文和其他非拉丁字符

使用示例:
---------
命令行使用:
    wshuyi-nb2pdf notebook.ipynb [output.pdf]

Python中使用:
    from wshuyi_nb2pdf import convert_notebook
    convert_notebook('notebook.ipynb', 'output.pdf')
"""

__version__ = '0.1.0'

from .converter import convert_notebook

__all__ = ['convert_notebook']
