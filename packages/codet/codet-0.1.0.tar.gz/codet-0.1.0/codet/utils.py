#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
工具函数模块
"""

import os
import sys
import platform


def get_system_info():
    """获取系统信息"""
    return {
        "system": platform.system(),
        "release": platform.release(),
        "version": platform.version(),
        "machine": platform.machine(),
        "processor": platform.processor(),
        "python_version": sys.version,
    }


def is_file_binary(file_path):
    """
    检查文件是否为二进制文件
    
    Args:
        file_path (str): 文件路径
        
    Returns:
        bool: 如果是二进制文件返回True，否则返回False
    """
    # 读取文件的前4KB内容
    chunk_size = 4096
    try:
        with open(file_path, 'rb') as f:
            chunk = f.read(chunk_size)
        
        # 检查是否包含空字节（通常表示二进制文件）
        if b'\x00' in chunk:
            return True
            
        # 尝试以UTF-8解码
        try:
            chunk.decode('utf-8')
            return False
        except UnicodeDecodeError:
            return True
    except Exception:
        # 如果出现任何错误，保守地认为它是二进制文件
        return True


def get_file_info(file_path):
    """
    获取文件信息
    
    Args:
        file_path (str): 文件路径
        
    Returns:
        dict: 包含文件信息的字典
    """
    stat_info = os.stat(file_path)
    return {
        "path": file_path,
        "size": stat_info.st_size,
        "created": stat_info.st_ctime,
        "modified": stat_info.st_mtime,
        "accessed": stat_info.st_atime,
        "is_binary": is_file_binary(file_path),
    }


def scan_directory(directory, recursive=False):
    """
    扫描目录
    
    Args:
        directory (str): 目录路径
        recursive (bool): 是否递归扫描
        
    Returns:
        list: 文件路径列表
    """
    files = []
    
    if recursive:
        for root, _, filenames in os.walk(directory):
            for filename in filenames:
                files.append(os.path.join(root, filename))
    else:
        for item in os.listdir(directory):
            item_path = os.path.join(directory, item)
            if os.path.isfile(item_path):
                files.append(item_path)
                
    return files 