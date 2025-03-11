#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
wshuyi_nb2pdf主要的转换器模块

该模块负责将Jupyter Notebook转换为优化的PDF格式，
包括代码不截断、合适的字体大小、优化的分页和布局等功能。
"""

import os
import sys
import asyncio
from pathlib import Path
import subprocess
from typing import Optional, Union, Dict, Any

async def _html_to_pdf(html_path: Union[str, Path], 
                      pdf_path: Optional[Union[str, Path]] = None,
                      options: Optional[Dict[str, Any]] = None) -> Path:
    """
    使用playwright将HTML文件转换为PDF
    
    参数:
        html_path: HTML文件路径
        pdf_path: 输出PDF文件路径（可选）
        options: 额外的转换选项
    
    返回:
        PDF文件路径
    """
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        raise ImportError(
            "需要安装playwright: pip install playwright && playwright install chromium"
        )
    
    html_path = Path(html_path)
    
    if pdf_path is None:
        pdf_path = html_path.with_suffix('.pdf')
    else:
        pdf_path = Path(pdf_path)
    
    # 默认选项
    default_options = {
        'landscape': True,
        'scale': 0.95,
        'margin': {"top": "0.5in", "right": "0.5in", "bottom": "0.5in", "left": "0.5in"},
        'format': 'Letter',
        'wait_time': 2000,  # ms
        'print_background': True,
    }
    
    # 合并用户选项
    if options:
        default_options.update(options)
    
    # 获取HTML文件的URL
    html_url = f"file://{html_path.absolute()}"
    
    # 启动playwright
    async with async_playwright() as p:
        # 启动浏览器
        browser = await p.chromium.launch(headless=True)
        context = await browser.new_context(
            viewport={"width": 1600, "height": 1200}
        )
        page = await context.new_page()
        
        # 导航到HTML页面并等待加载完成
        await page.goto(html_url, wait_until="networkidle")
        
        # 注入自定义CSS，确保代码正确显示
        await page.add_style_tag(content="""
            body { 
                margin: 20px;
                font-size: 16px;
            }
            
            /* 代码单元格内容设置 */
            .jp-InputArea-editor, .jp-OutputArea-output, 
            .jp-Cell-inputWrapper, .jp-Cell-outputWrapper,
            .highlight, pre, code {
                font-size: 16px !important;  /* 增大代码字体 */
                line-height: 1.5 !important;
                white-space: pre-wrap !important;  /* 自动换行 */
                word-wrap: break-word !important;  /* 在单词间换行 */
                overflow-x: visible !important;
                max-width: 100% !important;
                font-family: Menlo, Consolas, Monaco, 'Courier New', monospace !important;
            }
            
            /* 确保代码单元格可见 */
            .jp-CodeCell .jp-Cell-inputArea {
                display: block !important;
                visibility: visible !important;
                max-width: 100% !important;
            }
            
            /* 输入/输出提示设置 */
            .jp-InputPrompt, .jp-OutputPrompt {
                display: inline-block !important;
                visibility: visible !important;
                font-size: 14px !important;
            }
            
            /* 代码块强调样式 */
            .highlight {
                background-color: #f8f8f8 !important;
                border: 1px solid #ddd !important;
                border-radius: 4px !important;
                padding: 10px !important;
                margin: 10px 0 !important;
                width: 100% !important;
            }
            
            /* 确保输入提示显示 */
            div.prompt {
                display: block !important;
                visibility: visible !important;
                min-width: 10px !important;
                font-size: 14px !important;
            }
            
            /* 确保代码单元格内容显示 */
            div.input_area {
                display: block !important;
                visibility: visible !important;
                font-size: 16px !important;
            }
            
            /* 代码高亮颜色修正 */
            .highlight .k, .highlight .kn, .highlight .kp, .highlight .kr, .highlight .kt {
                color: #008800 !important;
                font-weight: bold !important;
            }
            
            .highlight .n, .highlight .na, .highlight .nb, .highlight .nc, .highlight .nd, 
            .highlight .ne, .highlight .nf, .highlight .nl, .highlight .nn, .highlight .nx {
                color: #333333 !important;
            }
            
            .highlight .s, .highlight .sa, .highlight .sb, .highlight .sc, .highlight .sd, 
            .highlight .s2, .highlight .se, .highlight .sh, .highlight .si, .highlight .sx, 
            .highlight .sr, .highlight .s1, .highlight .ss {
                color: #dd2200 !important;
            }
            
            .highlight .c, .highlight .ch, .highlight .cm, .highlight .c1, .highlight .cs {
                color: #888888 !important;
                font-style: italic !important;
            }
            
            /* Markdown格式优化 */
            h1, h2, h3, h4, h5, h6 {
                margin-top: 20px !important;
                margin-bottom: 10px !important;
                page-break-after: avoid !important;
            }
            
            /* 确保页面断开时不会在代码块中间 */
            .jp-Cell {
                page-break-inside: avoid !important;
            }
            
            /* 表格样式 */
            table {
                border-collapse: collapse !important;
                width: 100% !important;
                margin: 15px 0 !important;
                overflow-x: auto !important;
            }
            
            th, td {
                border: 1px solid #ddd !important;
                padding: 8px !important;
                text-align: left !important;
            }
            
            tr:nth-child(even) {
                background-color: #f9f9f9 !important;
            }
        """)
        
        # 等待页面完全渲染
        await page.wait_for_timeout(default_options['wait_time'])
        
        # 生成PDF
        print(f"生成PDF: {pdf_path}")
        await page.pdf(
            path=pdf_path,
            format=default_options['format'],
            landscape=default_options['landscape'],
            print_background=default_options['print_background'],
            margin=default_options['margin'],
            scale=default_options['scale']
        )
        
        # 关闭浏览器
        await browser.close()
    
    print(f"PDF已生成：{pdf_path}")
    return pdf_path

def _ensure_nbconvert():
    """确保nbconvert已安装"""
    try:
        import nbconvert
    except ImportError:
        raise ImportError(
            "需要安装nbconvert: pip install nbconvert"
        )

def convert_notebook(notebook_path: Union[str, Path], 
                    output_path: Optional[Union[str, Path]] = None,
                    html_template: str = 'full',
                    options: Optional[Dict[str, Any]] = None) -> Path:
    """
    将Jupyter Notebook转换为PDF，确保代码完全显示
    
    参数:
        notebook_path: Jupyter Notebook文件路径
        output_path: 输出PDF文件路径（可选）
        html_template: HTML转换使用的模板
        options: 额外的转换选项
    
    返回:
        生成的PDF文件路径
    """
    _ensure_nbconvert()
    
    notebook_path = Path(notebook_path)
    
    if output_path is None:
        output_path = notebook_path.with_suffix('.pdf')
    else:
        output_path = Path(output_path)
    
    # 转换为HTML
    html_path = notebook_path.with_suffix('.html')
    print(f"转换 {notebook_path} 为 HTML...")
    
    html_cmd = [
        'jupyter', 'nbconvert', 
        '--to', 'html',
        '--template', html_template,
        '--output', html_path.name,
        str(notebook_path)
    ]
    subprocess.run(html_cmd, check=True)
    
    # 将HTML转换为PDF
    result = asyncio.run(_html_to_pdf(html_path, output_path, options))
    
    print(f"转换完成: {output_path}")
    return result
