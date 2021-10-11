---
layout: post
title: "How I built tensorflow from source due to missing avx2 [incomplete]"
author: munkeops
categories: [computer vision, python, tensorflow]
image: "https://cdn-images-1.medium.com/max/1200/1*H-_-KC5YpXSR9jzeyX-5hQ.jpeg"
featured: false
hidden: true
---



Hi everybody, today I am gonna document another experience I had with installing tensorflow.  



## Intel's OpenVino

Intel's OpenVINO is an inference framework that essentially optmises deeplearning, more specifically vision and video based processing on a series of supported intel hardware. The intro as per Intel's documentation is as below :

>OpenVINO™ toolkit is a comprehensive toolkit for quickly developing applications and solutions that solve a variety of tasks including emulation of human vision, automatic speech recognition, natural language processing, recommendation systems, and many others. Based on latest generations of artificial neural networks, including Convolutional Neural Networks (CNNs), recurrent and attention-based networks, the toolkit extends computer vision and non-vision workloads across Intel® hardware, maximizing performance. It accelerates applications with high-performance, AI and deep learning inference deployed from edge to cloud.

## Supported hardware

The OpenVINO framework only supports a subsection of all available intel hardwares.

## Steps to setup an API

functions>classes>modules>packages>APIs maybe?
