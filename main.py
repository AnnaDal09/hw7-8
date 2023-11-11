result = []
def divider(a, b):
    try:
        if a < b:
            raise ValueError("ValueError: a is less than b")
        if b > 100:
            raise IndexError("IndexError: b is greater than 100")
        if b == 0:
            raise ZeroDivisionError("ZeroDivisionError: division by zero")
        return a / b
    except ValueError as ve:
        print(ve)
    except IndexError as ie:
        print(ie)
    except ZeroDivisionError as zd:
        print(zd)
data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}
for key in data:
    res = divider(key, data[key])
    result.append(res)
print(result)

