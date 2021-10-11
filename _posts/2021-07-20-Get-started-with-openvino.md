---
layout: post
title: "Get started with Intel's OpenVINO"
author: munkeops
categories: [computer vision, python, openvino]
image: "https://miro.medium.com/max/1000/1*Xa8UkrkzVpyirla4TvSYeQ.jpeg"
featured: false
hidden: false
---



This post is gonna give a gentle introduction to what is OpenVINO and how you can use it to increase vision based algorithms inference speeds. 



## Intel's OpenVino

Intel's OpenVINO is an inference framework that essentially optmises deeplearning, more specifically vision and video based processing on a series of supported intel hardware. The intro as per Intel's documentation is as below :

>OpenVINO™ toolkit is a comprehensive toolkit for quickly developing applications and solutions that solve a variety of tasks including emulation of human vision, automatic speech recognition, natural language processing, recommendation systems, and many others. Based on latest generations of artificial neural networks, including Convolutional Neural Networks (CNNs), recurrent and attention-based networks, the toolkit extends computer vision and non-vision workloads across Intel® hardware, maximizing performance. It accelerates applications with high-performance, AI and deep learning inference deployed from edge to cloud.

## Supported hardware

The OpenVINO framework only supports a subsection of all available intel hardwares. In fact processors such as Celeron which are cheap and edge based slow cpus which truly require the hardware acceleration do not support OpenVINO. So please be careful in checking out if your device falls under the given hardware requirements. The below link contains list of supported processors and os.

https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit/system-requirements.html

## Supported Frameworks

The framework dosent support all frameworks but does support most. You can use ONNX to convert from unsupported frameworks. Below is the list of direct support

* Caffe
* TensorFlow
* MXNet
* ONNX
* Kaldi

## So what does OpenVINO do?

## So how does OpenVINO run in inference?

To run your model for inference with OpenVINO you will need to first convert it into an intermediate respresentation(IR) which has to be run with the OpenVINO inference engine.
