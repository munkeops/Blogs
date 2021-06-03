---
layout: post
title: "Python Wrapper methods with Decorators"
author: munkeops
categories: [Python]
image: "https://www.seriousfacts.com/wp-content/uploads/2017/05/australia-top-10-species-of-the-most-lethal-snakes.jpg"
featured: true
hidden: false
---

Hi, today I will be writing a bit about python decorators. First for those who are not very familiar with it, I'll explain it with my own personal experience of where I came across it the very first time. I am sure many of you have worked a bit on web development and so python being one of the highly use languages that supports popular web frameworks(Flask & Django), tends to be the first choice for many. Its okay if you have only seen either one they both employ the use of decorators. In my case I have used both Flask and Django multiple times to create websites and APIs on the go when needed. Now both of these frameworks use decorators to route incoming HTTP/HTTPS requests from the network traffic to methods that can be defined by us to perform certain tasks in response to the request

In the particular example shown below in a basic Flask code we see that all GET requests to the url "your-site-name.com/home" will be routed to the home method defined in flask to respond to the request, which in this case will return a string that will be displayed on the Website.

```python
@app.route("/home")
def home():
    return "Hello, Flask!"
```

I wont get into the flask details as much, but what must be seen is that the `@app.route()` decorator is used to route urls to python methods.

While this is one use case which I felt most people reading this must have seen, it isn't the only place its used, a lot of people must have also seen it used when defining classes (eg @static methods) or in other python frameworks. 

So what are decorators - python has these wonderful things called decorators which can perform method calls to wrap other methods with just the use of a single line. To understand this we will look at the concept of wrapper methods (& even wrapper classes). Many of you would have heard about it a lot in various other languages where they use wrapper methods and classes for a variety of things.

First things first what are wrapper functions, how and why they work in python with the use of decorators. In python everything is an object made by a class. That means variables, data, methods and also classes (made by metaclasses- wont get into it here) are all objects. Hence just as we define instances of our own classes and move it around just like a variable, a method can be used as a variable too. Furthermore due to this object nature it also allows us to pass methods as parameters to other methods. Hence we can see below that we are defining a method `deco` that takes a method `f` as an argument. This method also has a method `wrapper` defined within itself, and returns it just like a variable (rather an object).

```python
def deco(f):
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

But what if we passed `func` to `deco` then what would the output be? Note - `w` is the returned `wrapper` method from deco and we then call this new method `w` instead of `func`

CALL

```
w=deco(func())
w()
```

OUTPUT

```
This function has started
hi from func
This function has ended
```

As you can see the method `deco` essentially applied `wrapper` around our original method `func`. And so now the method executes as is but with the `wrapper` method adding some few more lines of code around it, essentially wrapping our original method - hence the name wrapper functions.

So how do decorators come here?

The issues with the above style of doing things is that we do not wish to add invocation lines i.e we do not want to have to call both methods. In large production codes many a times we simply define methods to be called in other modules, having the code in the above fashion would mean having to remember and invoke both methods properly. This makes it very unfriendly to use.


We can simple apply the line `@deco` above the method `func` and it will automatically use `deco` to wrap `func` with the method `wrapper`. This saves us from writing extra lines of code or even invoking the method. Hence our new code will look like this  :

```python
def deco(f):
    def wrapper(f):
        print("This function has started")
        f()
        print("This function has ended")
    return wrapper

@deco
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

But then a question arises what if the the functions that we send to the wrapper function has parameters, should we define the `wrapper` method to take in those inputs too as shown below?

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

The answer to that is an obvious no. Here is why - what if we want to use the wrapper in a modular fashion, where it can be used with another method that has a different signature? The script shown above is hard coded and cannot be reused hence while its not wrong it is not modular enough to extend to all the methods. Before I get into the solution for this Id like to also point out what if the `func` method has a return value? How will the wrapper deal with the return values. The following script will take care of the above issues.

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

The script above now can take any arbitrary method with any kind of a function signature and use the args and kwargs of that method itself, so we don't need to hard code it. The return value `ret` is returned back too. As shown above the `deco` method is now capable of accepting any method with any signature ( in our case `binary_add` and `ternary_add` ) and also returns the appropriate values. Now we can say the script is perfected.

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

This is essentially how the Flask framework also uses decorators to wrap the `app.route()` method (`route` method from the flask `app` class) around the method we define. While we focus on the web service function, the wrapper class in the decorator handles the network connections and routings.

Some other use cases where we can create our own handy wrapper methods with decorators are when we want to time a function or in large projects make custom tests for every method when called.

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

Thanks for reading this article, any questions can we asked below with your Github account.