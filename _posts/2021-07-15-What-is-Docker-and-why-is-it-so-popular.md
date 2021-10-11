---
layout: post
title: "What is Docker and why is it so popular?"
author: munkeops
categories: [docker, devops]
image: "https://pradeeploganathan.com/wp-content/uploads/2018/08/docker-cover.png"
featured: false
hidden: false
---

Devops is ia largely paid and growing field not in just terms of jobs but in terms of developement as well. Gone are the days we needed to purchase our own hardware just to host a website or purchase certain software and os to develop an application. Applications have become more and more modular in nature and are becoming easier to develop and deploy. This posts main purpose is to give you an introduction to the world of containers and images through the help of docker.
## OS and Hardware Compatibility

Docker containers and images work on the core principal of hardware virtualisation. In older times, one hardware(laptop, pc, desktop etc) required one OS to organise resource management and other applications that run on that device need to be compatible with the os as well as the hardware o that the it can be allocated resources. Hence application executeables are built in a different manner for each type of OS. For example executeables in linux are of the form ".out" where as in windows they are of the form ".exe". Every OS (linux or windows flavours) have their own unique style and method of interfacing with the hardware resources and applications so that it can allocated resources. 

## OS nightmares in developing and deployment

When developing an application we needed to install all sub parts / packages/ programs which were not only compatible with the hardware but also with the OS. For example when building an application in C we will need the gcc compiler that can compile our code to the correct binaries. Installing gcc on windows had a lengthy long process( installation of third party apps or custom configured OS recognised apps), where as on linux its very easily supported and available with just running a few commands on the terminal (most of the times inbuilt as well). But even if we did get the installation right, the versions and configs change for different applications. Compatibility issues are very common when developing. 

Developers very well know it that they never just work on one project and each project has its own dependencies. Hence due to compatibility issues each project might need a different version of the software (v2 or v1.1 etc). A common workaround in many programming langauges is to create a virtual environment that can collect all the required packages and their correct version together. Another issue when collaborating with team members, having different OSes might cause issues with setting up the environment in many cases. In this case the the common workarounds we have seen is people using common remote machines.  

In terms of deployment when we ship code to some cloud server or to a clients machine. Installing all the sub softwares and then getting the machine configured correctly is just a bad way to deliver solutions. Hence what if we could not just wrap our code/application but also the working environment with it. That is all the sub modules and packages and softwares required to run our code comes packaged with the code. As long as the hardware supports the application we wont have to bother with the OS. So how can we make software OS independent in this way?

## Virtualisation

With the introduction of virtualisation/hyper-v/hypervisors this has become very much possible. It can isolate resources for a Guest OS which can directly communicate with the hardware in parrallel. 

## Images - Our own enclosed environment and software

We followed the Micro Service Architecture for deployment. The micro service architecutre essentially entails that different aspects/features of the project can be worked on independently and deployed separately. In this manner the application is not a whole and hence in case of an issue the entire website dosent need to brought down. We can continue to work and upgrade independent features and incorporate them onto websites.

## Whats next?

functions>classes>modules>packages>APIs maybe?
