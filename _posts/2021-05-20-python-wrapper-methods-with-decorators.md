---
layout: post
title: "Python Wrapper methods with Decorators"
author: munkeops
categories: [Python]
image: "https://www.psdgraphics.com/file/red-at-symbol.jpg"
featured: true
hidden: false
---

Hi, today I will be writing a bit about python decorators. First for those who do not know what decorators are, I'll explain it with my personal experience of where I came across it the first time. I am sure many of you have worked on web development and so python being one of the popular languages that does have web frameworks, tends to be the first choice for many. I have personally have used Flask and Django ( web development frameworks of python) in the past to create websites and APIs on the go when needed. Now both of these frameworks employ the use of decorators to route incoming HTTP/HTTPS requests from the network traffic to specific functions which can be defined by us and perform certain tasks in response to the particular invocation.

In the particular example shown below in a basic Flask code we see that all GET requests to the url "your-site-name.com/home" will be routed to the home function defined in flask to respond to the request, which in this case will return a string that will be displayed on the Website.

```python
@app.route("/home")
def home():
    return "Hello, Flask!"
```

I wont get into the flask details much but what we should notice is that with the use of the simple `@app.route()` decorator we are able to route urls to python functions.

Now coming to decorators, python has these wonderful things called decorators which can perform a series of tasks with just the use of a single line and some predefined functions. To understand this we will look at the concept of wrapper functions. Many of you would have heard about it a lot in various other languages where they use wrapper methods/functions and classes for a variety of things.

First things first what are wrapper functions, how and why they work. In python everything is an object made by a class. That means variables, data, functions and also classes (made by metaclasses- wont get into it here) are all objects. This means that just as we define instances of our own classes and throw it around as variables a function can be thrown around like a variable too, and by thrown around I mean passed as parameters to other functions. Hence we can see below that we are defining a function `f1` that takes a function as an argument. This function also defines a function within itself and returns the same just like a variable.

```python
def f1(f):
    def wrapper():
        print("This function has started")
        f()
        print("This function has ended")
    return wrapper

def func():
    print("hi from func")
```

 In this case what would happen if we called the method `func`- the output would be as below:

CALL

```
func()
```

OUTPUT

```
hi from func
```

But what if we passed `func` to `f1` then what the output would be?

CALL

```
w=f1(func())
w()
```

OUTPUT

```
This function has started
hi from func
This function has ended
```

As you can see the function `f1` essentially applied `wrapper` around our original method `func`. And so now the method executes as is but with the `wrapper` method adding some few more lines of code to it, essentially wrapping our original method - hence the name wrapper functions.

So how do decorators come here?

The issue with the above styles is that its not convenient to keep adding lines of code to invoke the method and then wrap it and create a new method instance `w`. One way to reduce the confusion is to just name `func` as func again:

```
func=f1(func())
func()
```

This works perfectly fine, but this still needs us to invoke the method. We would like to use `func` as func and not bother with writing the extra lines during invocation. Hence comes decorators.

We can simple apply the line `@f1` above the method func and it will automatically wrap `func` with the method `f1`. This saves us from writing extra lines of code or even invoking the method( when writing template codes we generally only want to define the methods not invoke them). Hence our new code will look like this  :

```python
def f1(f):
    def wrapper(f):
        print("This function has started")
        f()
        print("This function has ended")
    return wrapper

@f1
def func():
    print("hi from func")
```

CALL

```
func()
```

OUTPUT

```
This function has started
hi from func
This function has ended
```

But then a question arises what if the the functions that we send to the wrapper function has parameters, should we define the `wrapper` method to take in those inputs too as shown below?(f1 replaced with deco just to make it easier to understand)

```python
#bad way to handle
def deco(f):
    def wrapper(num1,num2):
        print("This function has started")
        f(num1,num2)
        print("This function has ended")
    return wrapper

@deco
def add(num1,num2):
    print("hi from func")
```

The answer to that is an obvious no. Here is why - what if we want to use the wrapper in a modular fashion, where it can be used with another function that has a different signature? The script shown above is hard coded and cannot be reused hence while its not wrong it is not modular enough to extend to all the functions. Before I get into the solution for this Id like to also point out what if the `func` method has a return value? How will the wrapper deal with the return values. The following script will take care of the above issues.

```python
def deco(f):
    def wrapper(*args,**kwargs):
        print("This function has started")
        ret=f(*args,**kwargs)
        print("This function has ended")
        return ret
    return wrapper

@deco
def binary_add(num1,num2):
    print("binary sum")
    return num1+num2

@deco
def ternary_add(num1,num2,num3):
    print("ternary sum")
    return num1+num2+num3

```

The script above now can take any arbitrary method and use the args and kwargs of that method itself and we don't need to hard code it. The return value `ret` is returned back too. As shown above the `deco` method is now capable of accepting any method with any signature (in our case `binary_add` and `ternary_add`) and also returns the appropriate values. Now we can say the script is perfected.

CALL

```
print(binary_add(1,1))
print(ternary_add(1,1,1))
```

OUTPUT

```
This function has started
binary sum
This function has ended
2
This function has started
ternary sum
This function has ended
3
```

This is essentially how the Flask framework also uses decorators to wrap the `app.route()` method (`route` method from the flask `app` class) around the method we define. While we focus on the web service function, the wrapper class handles the network connections and routings.

Some other use cases where we can create our own handy wrapper methods with decorators are when we want to time a function or in large projects test that every function is being called as it should be and track parameter values.

eg :

```python
import time


def timer(func):

    def wrapper(*args, **kwargs):
        start = time.time()
        rv = func()
        end = time.time()
        total = end-start
        print("\n\n\nTime To Run : ", total)
        return rv

    return wrapper


@timer
def test():
    time.sleep(1)


test()
```
Well thats all about wrapper methods with decorators for now. I hope you found this as exciting and interesting of a topic as I did. It definitely comes very handy with larger projects to simply add lines of code to a method without having to explicitly modify it, and also very useful to create abstracted modules and frameworks like Flask. 

Thanks for reading this article, any questions can we asked below by logging in with your Github account.