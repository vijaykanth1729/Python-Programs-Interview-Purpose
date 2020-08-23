a = [1,2,3,4,5]
element = 200
position = 2

def add(list, obj, pos):
    return list[:pos] + [obj] + list[pos:]
data = add(a, element, position)
print(data)
