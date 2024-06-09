def my_decorator(func):
    def wpr():
        print("before Call func")
        func()
        print("after Call func")
    return wpr

@my_decorator

def sayhello():
    print("hello")
    
sayhello()