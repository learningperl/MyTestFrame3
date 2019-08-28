# -*- coding: UTF-8 -*-
import unittest, os
from utest import testlib
from parameterized import parameterized


# 创建一个测试类，继承unittest
class PramaTest(unittest.TestCase):

    @parameterized.expand([
        [1, 1, 2,'整数'],
        [1.1, 1.33333333, 2.43333333,'小数'],
        [1, '1', '11','字符串'],
    ])
    def test_add(self, x, y, z,d=''):
        """"""
        print(d)
        self.assertEqual(testlib.add(x, y), z)

    def test1(self):
        print('11111')


if __name__ == '__main__':
    unittest.main()
