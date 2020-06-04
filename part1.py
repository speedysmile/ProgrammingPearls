#coding=utf-8
# @Time: 2020/5/30 11:38
# @Author: xl
# @File: part1.py
# @Software: PyCharm

"""
编程珠玑 第一章 开篇
问题描述：
输入：一个包含最多n个正整数的文件，每个数都小于n，其中n=10^7。如果在输入文件中有任何整数重复出现就是致命错误。
    没有其他数据与该整数相关联。
输出：按升序排列的输入整数的列表。
约束：最多有（大约）1M的内存空间可用，有充足的磁盘存储空间可用。运行时间最多几分钟，运行时间为10秒就不需要进一步优化了。

方案1：归并排序
方案2：位图排序
"""


class Bitmap:

    '''
    位图排序
    '''

    def __init__(self, max):
        if max % 32 == 0:
            self.size = self._calcLength(max)
        else:
            self.size = self._calcLength(max) + 1
        self.array = [0]*self.size

    def _calcLength(self, num):
        return num // 32

    def _calcByteIndex(self, num):
        return num % 32

    def count(self, num):
        eIndex = self._calcLength(num)
        bIndex = self._calcByteIndex(num)
        elem_num = self.array[eIndex]
        self.array[eIndex] = elem_num | (0x80000000 >> bIndex)
        # print(self.array)
        # print_num_hex(self.array)

    def test_num(self, num):
        eIndex = self._calcLength(num)
        bIndex = self._calcByteIndex(num)
        if self.array[eIndex] & (0x80000000 >> bIndex):
            return True
        return False


def print_num_hex(nums):
    line = ['%08X' % i for i in nums]
    print(" ".join(line))

if __name__ == '__main__':
    train_array = [5, 12, 738, 385, 617, 91, 8, 0, 30, 23, 46, 1036]
    # train_array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31]
    # train_array = [5, 12, 8, 0, 23]
    max_value = max(train_array)

    sort_array = []
    bitmap = Bitmap(max_value)
    for num in train_array:
        bitmap.count(num)

    for num in range(max_value + 1):
        if bitmap.test_num(num):
            sort_array.append(num)
            # print(sort_array)

    print(train_array)
    print(sort_array)