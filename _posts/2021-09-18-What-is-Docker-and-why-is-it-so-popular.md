---
layout: post
title: "What is Docker and why is it so popular?"
author: munkeops
categories: [docker, devops]
image: "https://pradeeploganathan.com/wp-content/uploads/2018/08/docker-cover.png"
featured: false
hidden: false
---

Devops is a largely paid and growing field not in just terms of jobs but in terms ofdevelopement as well. Gone are the days we needed to purchase our own hardware just to host a website or purchase certain software and os to develop an application. Applications have become more and more modular in nature and are becoming easier to develop and deploy. This posts main purpose is to give you an introduction to the world of containers and images through the help of docker.

## OS and Hardware Compatibility

Docker containers and images work on the core principal of hardware virtualization. In older times, one hardware (laptop, PC, desktop, etc.) required one OS to organise resource management and other applications that run on that device need to be compatible with the OS as well as the hardware o that the it can be allocated resources. Hence application executeables are built in a different manner for each type of OS. For example executeables in Linux are of the form ". out" where as in windows they are of the form ".exe". Every OS (Linux or windows flavours) has their own unique style and method of interfacing with the hardware resources and applications so that it can allocate resources.

## OS nightmares in development and deployment

When developing an application we needed to install all subparts / packages/ programs which were not only compatible with the hardware but also with the OS. For example, when building an application in C we will need the gcc compiler that can compile our code to the correct binaries. Installing gcc on windows had a lengthy long process (installation of third party apps or custom configured OS recognised apps), whereas on Linux its very easily supported and available with just running a few commands on the terminal (most of the times inbuilt as well). But even if we did get the installation right, the versions and configs change for different applications. Compatibility issues are very common when developing.

Developers very well know it that they never just work on one project and each project has its own dependencies. Hence, due to compatibility issues each project might need a different version of the software (v2 or v1. 1 etc.). A common workaround in many programming languages is to create a virtual environment that can collect all the required packages and their correct version together. Another issue when collaborating with team members, having different OSes might cause issues with setting up the environment in many cases. In this case the common workarounds we have seen is people using common remote machines.

In terms of deployment when we ship code to some cloud server or to a client machine. Installing all the sub softwares and then getting the machine configured correctly is just a bad way to deliver solutions. Hence, what if we could not just wrap our code/application, but also the working environment with it. That is all the sub modules and packages and softwares required to run our code comes packaged with the code. As long as the hardware supports the application, we won't have to bother with the OS. So how can we make software OS independent in this way?

## Virtualization

With the introduction of virtualization/hyper-v/hypervisors we can make our applications Host OS independent. This piece of technology lets us isolate resources for a Guest OS, which can directly communicate with the hardware in parallel with the Host OS. Its essentially creating a virtual environment at the OS level, hence directly communicating to the hardware.

With this introduced we can simply run a lightweight virtualized instance of an OS on any Host OS and run commands and applications there. Hence, no more developing applications separately for different Host OSs. Simply develop on a single OS of choice and then ship the entire OS+Application to the deployment platform without any worries of incompatibility.


## Images and Containers- Our own enclosed environment and software

So now that we understand the possibility to wrap the OS+Application together for deployment, lets get into the methodology and terminology to do so. 

The OS+Application bundled together is called a container. When we boot our enclosed virtual OS with the application, we simply running a container. Similar to "container ships" that can hoard several containers without knowing what is there in them, we can imagine our deployment device with a Host OS running several such containers in parallel. (Note that the capabilities and number of containers running is dependent on the hardware). 

Containers are quite large and heavy and are like an actual OS. Hence, they are not shipped as is. In fact the Containers are compressed in a format known as Container Images. Just like image/ISO files for an OS a container is also shipped as images. Hence, during development we can simply create a container, install and add all applications or modules, and once complete we can convert it into an image and store it in a registry and then ship the image. One the deployment device they will simply boot a container from this image. Note that the image is a base template and several containers can be booted from the one single image. Once the container is booted, it will contain the exact environment and software as it was when we created the image from the container.



## Whats next?

Now that we know it is possible to package an ship applications which run directly on the hardware in a virtualised container the DevOps community has accepted and used it widely for application installations and deployments. Server machines that can host 100s of docker containers independently or in the form of clusters are also becoming extremely popular. 

To manage , update and administer such large and distributed software becomes a challenging task. Hence was born Kubernetes a container orchestration tool. 


For more such content stay tuned.
