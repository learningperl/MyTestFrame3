# -*- coding: UTF-8 -*-
import unittest, os
from test_group import get_cishu
from parameterized import parameterized


# 创建一个测试类，继承unittest
class PramaTest(unittest.TestCase):

    @parameterized.expand([
        [[1, 1, 2, 2, 3, 3, 2, 2, 4, 3, 2, 4, 3, 2], True],
        [[1], False],
        [[1, 1], True],
        [[1, 2], False],
        [[1, 1, 1], True],
        [[1, 1, 1, 1], True],
        [[1, 1, 1, 1, 1, 3, 3, 3, 3, 3, 3, 3, 3, 3], False],
    ])
    def test_add(self, ll, s):
        """"""
        self.assertEquals(get_cishu(ll), s)


if __name__ == '__main__':
    unittest.main()
