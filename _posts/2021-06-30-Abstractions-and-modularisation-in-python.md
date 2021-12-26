---
layout: post
title: "Abstractions and modularisation in python"
author: munkeops
categories: [python]
image: "https://i.pinimg.com/originals/19/99/7a/19997ab11e9aa8e89231f8954b95ca2b.jpg"
featured: True
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
#calcadd.py
if __name__=='__main__':
    print(add(3,4))
```

Run the above script.
``` bash
> python calcadd.py
> 7
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

lets modify the above example for a calculator below using functions.

```python

# calculator_func.py

def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
	
if __name__=='__main__':
	a=20
	b=10
	print(add(a,b))
	print(sub(a,b))
	print(mul(a,b))
	print(div(a,b))
	

```

now run this script:

```bash
> python calc.py
> 30
> 10
> 200
> 2
```

this makes this much easier as now whenever i need to do some complex operation which requires to use one or more of these base operations more than once, I dont have to rewrite the code for these base operations.

Example :

suppose I want to calculate a<sup>2</sup>+b<sup>2</sup>-2ab, and i have the above functions

there are two ways to do this:

```python
# calculator_func.py
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
	
if __name__=='__main__':
	
# solution1.py
	
	sol=sub(add(mul(a,a),mul(b,b)),mul(2,mul(a,b)))
	
# solution2.py use the expression (a-b) squared

	val1 = sub(a-b)
	sol=mul(val1,val1)


```

As seen in the example code above, we can use the ready-made functions to perform the same task multiple times without having to write the code for those functions.

#### Classes

A class is essentially a blueprint for an object. This blueprint is nothing but functions an object can perform and variables native to that object. Now classes take abstraction to a step higher. They abstract several internal functions and as well as variables into an object variable which is user defined.

lets continue the above example to demonstrate what I mean.

suppose we converted the calculator script into a class and display the solution 2 discussed above.

```python
# calculator_class.py
class calculator:
	def __init__():
		pass
	def add(self,a,b):
		return a+b
	def sub(self,a,b):
		return a-b
	def mul(self,a,b):
		return a*b
	def div(self,a,b):
		return a/b
	
if __name__=='__main__':

	# create an object for the class
	calc=calculator()
	
# solution2.py use the expression (a-b) squared

	val1 = calc.sub(a-b)
	sol=calc.mul(val1,val1)

```

When you look at this code it feels like it is very much similar to the previous functions only example. But we havent made the full use of classes yet. As mentioned above classes can not only just store functions but variables also.

Hence lets take an example to understand this. Suppose we had to create a scientific calculator which has the option to calculate exponentials.

the function to make and exponential would be :

```python
# calculator_func.py
def exp(a,b):
	sol=1
	for i in range(b):
		sol=mul(sol,a)
	return sol
```

in fact this would also be the exact same code we would write inside a class as well. But suppose we want to find exponentials with respect to 'e'. And for those who have used scientific calculators you must know the importance and frequency with which we calculate exponentials with 'e'. Hence using this function we would have to pass the value of 'e' everytime. Which means we would have to know and store the value of e in some external variable as shown below:

```python
# calculator_func.py
def add(a,b):
	return a+b
def sub(a,b):
	return a-b
def mul(a,b):
	return a*b
def div(a,b):
	return a/b
def exp(a,b):
	sol=1
	for i in range(b):
		sol=mul(sol,a)
	return sol
	
if __name__=='__main__':
	
	e = 2.71828
	
#calcuate e squared
	print(exp(e,2))
	

```

But in a calculator you must have noticed that the value is generally by default stored in the calc and is provided as a button to use at any time. 

Hence we can use classes to do this and store the value of e internally as shown below.

```python

# calculator_class.py
class calculator:
	def __init__():
		self.exp_val=2.71828
	def add(self,a,b):
		return a+b
	def sub(self,a,b):
		return a-b
	def mul(self,a,b):
		return a*b
	def div(self,a,b):
		return a/b
	def exp(self,a,b=None):
		if(b==None):
		 	return self.exp_e(a)
		sol=1
		for i in range(b):
			sol=mul(sol,a)
		return sol
	def exp_e(self,b):
		sol=1
		for i in range(b):
			sol=mul(sol,self.exp_val)
		return sol
	
if __name__=='__main__':

	a=2
	b=3

# create an object for the class
	calc=calculator()
	
# if you pass two values it will calc a power b, but if you pass one value it will calculate e power a

	
	print(calc.exp(a,b)) # will return a power b
	print(calc.exp(a)) # will return e power a

```

The above example shows how we can use the same method to perform different tasks with an internal default value.

Note : method overloading is not supported in python by default and must be implemented in ways like I did in this example. As seen in the above example you could call calc.exp(a) or calc.exp_e(a), both would return the same but in doing the way shown above it adds abstraction as the user need not know about the extra function, for them this single function is doing the job.

#### Modules

Modules are nothing but python scripts. A python script/module can contain several classes (which can contain several functions) and also several independant functions which are not part of classes. It can also contain a lot of variables.

To create a connection from above examples all this while we were using the calc.py module.

Suppose once we define the code for this calculator, be it in a function form or a class form. we can now integrate calculator functionalities to other applications.

for explanation purpose lets make an equation solver application. Also now that we understand the added advantage in using classes we will use classes for further development.

```python
#eq_sol.py

class Eq_Solve:

	def __init__():
		pass
		
	def sum_square(a,b):
		val=a+b
		sol=val*val
		return sol
	
	def square_sum(a,b):
		val1=a*a
		val2=b*b
		return val1+val2



```

Note that for this example using modules dosent seem really helpful. This example was only chosen for ease of explanation. But imagine in a much more complex scenario where the operations were much more complicated using modules and classes is every helpful.

Now instead of using the inbuilt addition and multiplication operations we could use our own operations that we created (once again, this is just for explanation, to understand better just imagine +,* does'nt exist in python or are very complicated to implement).

given the file structure as below:

```bash
folder
	calc_class.py
	eq_sol.py
```

we can then modify eq_sol to use our predefined functions from calc_class by simply importing that module into eq_sol.

```python
#eq_sol.py

from calc_class import  calculator as cal #import only one class
# OR (Pick only 1)
from calc_class import * # import everything (classes,funcs and variable from calc_class)

class Eq_Solve:

	def __init__():
		pass
		
	def sum_square(a,b):
		val=cal.add(a,b)
		sol=cal.mul(val,val)
		return sol
	
	def square_sum(a,b):
		val1=cal.mul(a,a)
		val2=cal.mul(b,b)
		return cal.sum(val1,val2)
		
if __name__=='__main__':

	a=3
	b=2
	
	es=Eq_Solve()
	
	value1=es.sum_square(a,b) # (a+b)^2
	value2=es.square_sum(a,b)+cal.mul(2,cal.mul(a,b)) # a^2+b^2+2ab
	
	
	print(str(value1)+"=="+str(value2))


```
#### Packages

One step higher and we have packages. A package is an abstraction to python modules. With an __init__.py script you can have several modules imported and used. 

#### APIs

An API stands for application programming interface. It essentially is a way to interface with an application, either through endpoints or obfuscated code (code where you cant see the source code but can only use them). Now all of the above mentioned can be system level APIs. But for the discussion of this blog we will be looking only at Web APIs with flask.

### Further Reading

You can visit my blog on [Setup a Flask API in 5 steps!](https://munkeops.github.io/Blogs/How-to-setup-flask-api-server-in-5-steps/) This will help you setup APIs in flask.

