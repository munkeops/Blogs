---
layout: post
title: "Abstractions and modularisation in python"
author: munkeops
categories: [python]
image: "https://i.pinimg.com/originals/19/99/7a/19997ab11e9aa8e89231f8954b95ca2b.jpg"
featured: false
hidden: false
---



Hi guys, here I am gonna talk about abstractions in python and how they help make code modular. Abstractions and the ease of using it in my opinion has made python extremely popular, cause with its huge community base we have modular packages developed for almost everything in python. 

### Abstraction

So what is abstraction? Its essentially an art of abstracting or hiding the non essential details. In terms of programming, we may not need to know how a certain function or class works but we just want to and need to know how to use it and if it does the job for us. for eg - we define a function that can add two values

```python
#calcadd.py
def add(a,b):
    return a+b
```
Now when we have to use this function, I only need to know how to use it i.e what are the values that will be sent to it and what are the values returned from it. The internal workings are abstracted by whoever developed this function.

```python
if __name__=='__main__':
    print(add(3,4))
```

Run the above script.
```
>python calcadd.py
7
```

### Modularisation

Modularisation is concept that goes hand in hand with abstraction. When you abstract code in the form of functions or classes or scripts, you also make them resuable. But just because the code is reusable dosent make it modular. It takes careful designing and conscious effort to make code modular. Simply putting random code into functions and calling it dosent make code modular in nature. 

So what do we understand by modularity? It is essential breaking down a flow of code into reusable independent and abstracted bits which have a logical value when added to the flow. Why and what do we achieve from this? 

From a developers perspective by doing so I now have each separate independent sections of the code working and can work on improving each section separately without breaking the othet sections. For example in a time constraint workflow with the following sections : A, B, C, and D takes 25s to complete. If section C is taking the most amount of time I can work on optimising and redeveloping section C without breaking A, B and D. Hence making my job easy as in case of a failure I can simply revert section C to the old code. This plug and play nature makes it easy to go about developing and optimising software.

From a user's perspective who is going to use this modular code, I simply have to plug and play each part of the flow without knowing how they are implemented.

### A popular Hierarchy

From a pythony perspective we can say that Abstractions can have a Hierarchy in the following manner:

functions>classes>modules>packages> ...APIs

#### Functions

Has a signature that defines the input and output in some form. Abstracts only pure code.

#### Classes

A class is essentially a blueprint for an object. This blueprint is nothing but functions an object can perform and variables native to that object. Now classes take abstraction to one step higher. They abstract several internal functions and as well as varibales into an object variable.

#### Modules

Modules are nothing but python scripts. A python script/module can contain several classes (which can contain several functions) and also several independant functions.

#### Packages

One step higher and we have packages. A package is an abstraction to python modules. With an __init__.py script you can have several modules imported and used. 

#### APIs

An API stands for application programming interface. It essentially is a way to interface with an application, either through endpoints or obfuscated code (code where you cant see the source code but can only use them). Now all of the above mentioned can be system level APIs. But for the discussion of this blog we will be looking only at Web APIs with flask.


