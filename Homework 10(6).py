def f_ending(strings, ending):
    try:
        return list(filter(lambda s: s.endswith(ending), strings))
    except TypeError:
        return "Type error"

params = ['hello', 'world', 'coding', 'nod']
ending = 'ing'
result = f_ending(params, ending)

print(result)