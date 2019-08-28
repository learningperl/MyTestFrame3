# -*- coding: UTF-8 -*-
import sys

if __name__ == '__main__':
    print(sys.argv)

# import unittest
# from utest import testlib
#
#
# class MyTest(unittest.TestCase):
#     """
#         继承unittest的TestCase类
#         这一个类就是单元测试类
#     """
#
#     def setUp(self):
#         """
#             实例函数的setup，每一个测试方法执行前都会执行一次
#             :return:
#         """
#         print('初始化')
#
#     def tearDown(self):
#         """
#             实例函数的setup，每一个测试方法执行完成后都会执行一次
#             :return:
#         """
#         print('结束')
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         """
#             类函数的setup，只会在最开始执行一次
#             :return:
#         """
#         print('最开始执行')
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         """
#             类函数的setup，只会在最后执行一次
#             :return:
#         """
#         print('执行结束')
#
#     def test_int(self):
#         """
#             这是一个测试方法
#             测试方法必须以test开头命名
#             :return:
#         """
#         res = testlib.add(11111111111111111111111111111111111111,1)
#         self.assertEqual(res,11111111111111111111111111111111111111)
#
#     def test_float(self):
#         res = testlib.add(1.0, 1.1)
#         self.assertEqual(res, 2.1)
#
#     def test_str(self):
#         res = testlib.add('a', 'b')
#         self.assertEquals(res, 'ab')
#
#
# # 使用unittest运行
# if __name__ == '__main__':
#     """
#         没有默认报告
#     """
#     unittest.main()
