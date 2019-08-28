# -*- coding: UTF-8 -*-


# ll = [1, 1, 2, 2, 3, 3, 2, 2, 4, 3, 2, 4, 3, 2]
# ll = [1]
# ll = [1,1]
# ll = [1,2]
# ll = [1,1,1]
# ll = [1,1,1,1]
# ll = [1, 1, 1, 1,1, 3, 3, 3, 3, 3, 3, 3,3,3]


# 统计数字出现的频率
def get_cishu(ll):
    # 获取最小的频率
    def get_min(d):
        m = 0
        for min in d.values():
            if m == 0:
                m = min

            if min < m:
                m = min
        return m

    # 所有数字出现的频率对最小频率取余
    def check(d, min):
        if min < 2:
            return False

        for v in d.values():
            if v % min > 0:
                return False

        return True

    dict1 = {}
    for i in ll:
        try:
            flg = dict1[i]
        except Exception as e:
            flg = False
        if flg:
            dict1[i] += 1
        else:
            dict1[i] = 1

    min = get_min(dict1)
    res = check(dict1, min)
    return res

