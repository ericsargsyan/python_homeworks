from functools import wraps

def my_decorator(new_list: list) -> callable:
    print("first step _ 1")
    def decorator(func:callable) -> callable:
        print("first step _ 2")
        @wraps(func)
        def decor(*args,**kwargs):
            print("first step _ 3")
            print("function starts")
            
            result = func(*args,**kwargs)
            print("function ended")
            new_list.append(result)
            return result
        return decor
    return decorator    

my_list = []
@my_decorator(my_list)  # foo = my_decorator(my_list)(foo)
def foo(x,b):
    for i in range(x, b):
        print(i)
    return i

a = foo(5,b=9) # my_decorator(my_list)(foo)(5,b=9)

# print(a, my_list)

def generat_num(num: int):

    for i in range(num):
        yield i

print(generat_num)
a=generat_num(5)
for i in
print(next(a))


