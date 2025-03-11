import time

def timer(func): #定义一个名为 timer() 的装饰器函数，它接受一个参数 func这个 func 就是即将要被修饰的函数
    def wrapper(*args, **kwargs): #在 timer() 函数内部，定义一个名为 wrapper() 的闭包函数
        start_time = time.time() #在调用 wrapper() 函数时，它会根据传入的参数来调用被修饰的函数 func，并在函数执行前后记录时间
        res = func(*args, **kwargs)
        stop_time = time.time()
        print(f'{func.__name__} run time is {stop_time - start_time}')
        return res #同时输出函数执行时间。最后，它将 func 函数的返回值返回
 
    return wrapper