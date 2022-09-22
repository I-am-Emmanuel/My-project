def custom_range(numb):
    pass


def infinite_number_generator():
    numb = 0
    while True:
        yield numb
        numb += 1


gen = infinite_number_generator()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

for i in gen:
    print(i)

