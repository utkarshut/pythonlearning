def generateSquare(num):
    result = []
    for i in num:
        result.append(i ** 2)
    return result


squareNum = generateSquare([1, 2, 3, 5])

print(squareNum)
print("first")


def generateSquareYield(num):
    for i in num:
        yield (i * i)


squareNumYield = generateSquareYield([1, 2, 3, 5])

print(next(squareNumYield))
print(next(squareNumYield))
print(next(squareNumYield))
print(next(squareNumYield))
print("second")

for num in [2, 3, 4]:
    print(num)

print("third")

a = (x ** 2 for x in squareNum)

print(list(a))

print(next(a))
print(next(a))
print(next(a))
print(next(a))

print("fourth")
