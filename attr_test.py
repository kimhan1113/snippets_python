from collections import Counter

lists = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5, 6]


print(Counter(lists))
assert 1 == 0


class test:
    a = 1

    def hoxy(self):
        num = 10
        return num


t = test()

# t라는 객체에 있는 "hoxy" 라는 인스턴스를 쓰는법 오른쪽 괄호에는 피라미터값이 있으면 넣는다
print(getattr(t, "hoxy")())

# b라는 멥버가 있는지? true or false
print(hasattr(t, 'b'))

# t객체에서 a라는 변수를 찾아 5라는 값을 할당!!
setattr(t, "a", 5)
print(getattr(t, "a"))

result1 = isinstance(100, int)
# print(f"{result1}는 int 타입이 맞습니다.")


class test1:
    pass


class test2(test1):
    pass


t2 = test2()

result2 = isinstance(t2, test1)
print(result2)
