list_a = ['a', 'b', 'c', 'd', 'd', 'e', 'a']
print("list_a:", list_a, type(list_a))
list_b = sorted(set(list_a), reverse=True)
print("list_b:", list_b, type(list_b))
