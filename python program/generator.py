def count(n):
    num = 1
    while num <= n:
        yield num
        num += 1
for number in count(10):
    print(number)