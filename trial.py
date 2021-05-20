def f1(f):
    def wrapper(*args,**kwargs):
        print("This function has started")
        ret=f(*args,**kwargs)
        print("This function has ended")
        return ret
    return wrapper

@f1
def binary_add(num1,num2):
    print("binary sum")
    return num1+num2

@f1
def ternary_add(num1,num2,num3):
    print("ternary sum")
    return num1+num2+num3

print(binary_add(1,1))
print(ternary_add(1,1,1))
