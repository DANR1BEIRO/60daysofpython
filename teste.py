# lista = list("daniel gomes ribeiro")
# print(lista)
# print(type(lista))
# print(len(lista))

# for x in range(0, 11):
#     print(x)


# lista2 = [1, 2, 3]
# x, y, z = lista2
# print(x)
# print(lista2[0])

fruits = ["banana", "apple", "strawberry"]

for fruit in fruits:
    if fruit.startswith("b"):
        print(f"I like {fruit.capitalize()}")
    else:
        print(f"I don't like {fruit.capitalize()}")