---
layout: post
title: "Setup a Flask API in 5 steps!"
author: munkeops
categories: [python, API, flask]
image: "https://i.ytimg.com/vi/GgS8-mn9zoM/maxresdefault.jpg"
featured: true
hidden: false
---



Hi guys, this post is gonna be a quick starters guide to setting up your very own flask server to make API requests. Before we get started ill try a give a bit of an overview on the aspects of this topic and where and how they are used.

### APIs

APIs stand for application programming interface. They are essentially a means for communication between different aspects of an application( eg frontend and backend). It also serves another purpose of keeping the code abstracted and hidden, essentially not revealing the source code. 

### APIs for web dev?

In webdev it is commonly seen (as in the microservice architecture) that the front end and the backend are essentially separated and hosted individually. Even in the case that they were hosted together the front end page needs a mechanism to communicate with the backend and perform certain actions. Example, suppose you had a button on the front end that would upload an image, compress it and send it back for download. Now upon clicking the button we need to initiate this process in the backend, this requires the front end to communicate with the backend and hence an API. 

### Flask

Flask is a python framwork built over raw concepts and low level apis such as sockets. With flask we can can setup a backend for a front end or standalone API for an application in no time. Its an extemely light weight and modular ready to run HTTP based API server. While you can deploy the frontend separately (react/html etc pages) and have the API separately, flask also supports the option of rendering pages in a lightweight manner as compared to some of the other heavy weights such as Django. 

### Steps to setup flask as an API

#### Step 1

install flask with python's pip package manager. 

```
pip install flask
```

#### Step 2

setup the falskapp package (flaskapp is the name of my app, you can name it anything):

```
root>mkdir flaskapp
root>cd flaskapp
flaskapp>touch __init__.py
```

#### Step 3 setup the flask object

Import the flask module and create the flask object (app) in __init__.py. Also import the views module here 

```python
from flask import Flask
app = Flask(__name__)

from .views import *
```

#### Step 4

create the views module (deriving from the mvc model)
```
flaskapp>touch views.py
```

inside views put the following template code:

```python
from . import app
@app.route("/home")
def home():
    return "Hello, Flask!"
```
#### Step 5

create a server instance (server.py) which will be entry code to this application.

```
root> touch server.py
```

import the flaskapp package and run it

```python
from flaskapp import *

app.run(host='127.0.0.1',port=5000,debug=True)
```
set host to locahost (127.0.0.1) for development and choose a port (5000 is generally used) and can set the debug mode to True so that the server updates and restarts when changes made durnig development.

### Result

Voila, you have your flask server up and running, to check it out you can open a browser and enter the ip and port as the server indicates in the output. The logs will show a GET request hit. 

![flaskoutput](..\assets\images\flaskoutput.jpg)

the final file structure is as follows

![flaskfilestruct](..\assets\images\flaskappstruct.jpg)

### What next ?

Going further you can create your own endpoints and send data along with the API as well. Alos you can checkout postman as a handy tool to test out APIs.