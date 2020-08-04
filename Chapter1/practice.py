import time
from unittest import TestCase, main
from fib2 import *
from fib3 import *
from fib4 import *
from fib5 import *

class FibTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_result(self):
        for n in range(20):
            self.assertEqual(my_fib2(n), fib2(n))

    def test_performance(self):
        fibs = [fib2, fib3, fib4, fib5]
        m = 20
        for f in fibs:
            t1: float = time.time()
            for n in range(m):
                my_fib2(n)
            t1 = time.time() - t1
            t2: float = time.time()
            for n in range(m):
                f(n)
            t2 = time.time() - t2
            self.assertLessEqual(t1, t2)


def my_fib(n: int) -> int:
    """練習問題1.7-1 fib2と同様なのでテストをクリアできない
    """
    if n <= 1:
        return n
    return my_fib(n-1) + my_fib(n-2)


@lru_cache(maxsize=None)
def my_fib2(n: int) -> int:
    if n < 2:
        return n
    a: int = 0
    b: int = 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


# 練習問題1.7-2
# 使いやすいビットのシーケンスとして使えるint
class Sequence_of_bits:
    """ビットシーケンスとして使えるラッパークラス
    LIFO。
    """
    def __init__(self):
        self.data: int = 1
        self.n: int = -1

    @property # getterと同じ能力をもつ
    def bit_length(self):
        # bit_length() 整数を符号と先頭は除いて二進数で表すために必要なビット数を返却
        return self.data.bit_length() - 1

    @property
    def element_number(self):
        return self.bit_length // 2
        
    def add(self, value):
        self.data <<= 2
        self.data |= value

    def __iter__(self):
        self.n = -1
        return self

    def __next__(self):
        self.n += 1
        if self.n >= self.element_number:
            raise StopIteration
        return self.__getitem__(self.n)

    def __getitem__(self, element_no):
        pos = element_no * 2
        if element_no <= self.element_number:
            return self.data >> pos &0b11
        raise ValueError("Out of index")

    def __repr__(self):
        return bin(self.data)



def int_2_sequence(n: int):
    """練習問題1.7-2
    ビットのシーケンスとして使えるintの使いやすいラッパー"""
    pass

if __name__ == "__main__":
    print("練習問題1.7-1")
    print(my_fib(10))
    print("練習問題1.7-2")
    sob = Sequence_of_bits()
    sob.add(0b00)
    sob.add(0b01)
    sob.add(0b10)

    print(sob)

    for n, s in enumerate(sob):
        print(n, ":", s)
        print(sob[n])