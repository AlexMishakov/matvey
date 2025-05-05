"""
Цикл пока:


while a > 0:
    a -= 1


нц пока сверху стена
    ...
кц

break - останавливает цикл for / while
"""

a = 4
while a > 0:
    a -= 1
    print(a)


while True:
    a = int(input())
    if a == 0:
        break

    # ...



