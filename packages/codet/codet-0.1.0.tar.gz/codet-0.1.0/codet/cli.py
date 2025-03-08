#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
命令行接口模块
"""

import sys
import click

from . import __version__


@click.group()
@click.version_option(version=__version__)
def cli():
    """Codet - 一个跨平台的命令行文件处理工具"""
    pass


@cli.command()
@click.argument('file', type=click.Path(exists=True))
@click.option('--output', '-o', help='输出文件路径')
def process(file, output):
    """处理指定文件"""
    click.echo(f"处理文件: {file}")
    if output:
        click.echo(f"输出到: {output}")
    # 这里添加文件处理逻辑


@cli.command()
@click.argument('directory', type=click.Path(exists=True, file_okay=False, dir_okay=True))
@click.option('--recursive', '-r', is_flag=True, help='是否递归处理目录')
def scan(directory, recursive):
    """扫描目录"""
    click.echo(f"扫描目录: {directory}")
    click.echo(f"递归模式: {'开启' if recursive else '关闭'}")
    # 这里添加目录扫描逻辑


def main():
    """CLI主入口函数"""
    try:
        cli()
    except Exception as e:
        click.echo(f"错误: {str(e)}", err=True)
        sys.exit(1)


if __name__ == "__main__":
    main() 