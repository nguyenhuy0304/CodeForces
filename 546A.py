k, n, w = map(int, input().split())
money_all = 0
print(type(k))

for i in range(1, w+1):
    money_all = money_all + i * k

money_borrow = money_all - n
if money_borrow < 0:
    money_borrow = 0

print(money_borrow)