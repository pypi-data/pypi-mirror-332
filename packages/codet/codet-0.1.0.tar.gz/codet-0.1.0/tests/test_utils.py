#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
工具函数测试模块
"""

import os
import tempfile
import unittest

from codet.utils import get_system_info, is_file_binary, get_file_info, scan_directory


class TestUtils(unittest.TestCase):
    """工具函数测试类"""

    def test_get_system_info(self):
        """测试获取系统信息"""
        info = get_system_info()
        self.assertIsInstance(info, dict)
        self.assertIn("system", info)
        self.assertIn("python_version", info)

    def test_is_file_binary(self):
        """测试二进制文件检测"""
        # 创建文本文件
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as text_file:
            text_file.write("这是一个文本文件")
            text_path = text_file.name

        # 创建二进制文件
        with tempfile.NamedTemporaryFile(mode='wb', delete=False) as binary_file:
            binary_file.write(b'\x00\x01\x02\x03')
            binary_path = binary_file.name

        try:
            self.assertFalse(is_file_binary(text_path))
            self.assertTrue(is_file_binary(binary_path))
        finally:
            # 清理临时文件
            os.unlink(text_path)
            os.unlink(binary_path)

    def test_get_file_info(self):
        """测试获取文件信息"""
        with tempfile.NamedTemporaryFile(mode='w', delete=False) as temp_file:
            temp_file.write("测试文件")
            file_path = temp_file.name

        try:
            info = get_file_info(file_path)
            self.assertIsInstance(info, dict)
            self.assertEqual(info["path"], file_path)
            self.assertIn("size", info)
            self.assertIn("created", info)
            self.assertIn("modified", info)
            self.assertIn("accessed", info)
            self.assertIn("is_binary", info)
        finally:
            os.unlink(file_path)

    def test_scan_directory(self):
        """测试目录扫描"""
        with tempfile.TemporaryDirectory() as temp_dir:
            # 创建一些测试文件
            for i in range(3):
                with open(os.path.join(temp_dir, f"file{i}.txt"), 'w') as f:
                    f.write(f"测试文件 {i}")

            # 创建子目录和文件
            sub_dir = os.path.join(temp_dir, "subdir")
            os.mkdir(sub_dir)
            with open(os.path.join(sub_dir, "subfile.txt"), 'w') as f:
                f.write("子目录文件")

            # 测试非递归扫描
            files = scan_directory(temp_dir, recursive=False)
            self.assertEqual(len(files), 3)

            # 测试递归扫描
            files = scan_directory(temp_dir, recursive=True)
            self.assertEqual(len(files), 4)


if __name__ == "__main__":
    unittest.main() 