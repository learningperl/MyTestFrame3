# -*- coding: UTF-8 -*-
import os
from common import logger


def decrypt(t,s):
    """
    使用decrypt.jar实现的加密解密算法
    :param t: 0：表示加密，其他字符串表示解密
    :param s: 需要加密或者解密的字符串
    :return: 加密或者解密后的字符串
    """
    cmd = 'java -jar decrypt.jar ' + str(t) + ' ' + str(s)
    try:
        result = str(os.popen(cmd).read())
    except Exception as e:
        result = ''
        logger.exception(e)

    return result






