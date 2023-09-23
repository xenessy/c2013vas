def raise_to(num, max_degree):
    i = 0
    for _ in range(max_degree):
        yield num ** i
        i += 1


res = raise_to(122345, 500)
print(res)
for _ in res:
    print(_)
    print("-"*20)
print('new')
for _ in res:
    print(_)
    print("-"*20)