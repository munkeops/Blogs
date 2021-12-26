---
layout: post
title: "Get started with Intel's OpenVINO"
author: munkeops
# categories: [computer vision, python, openvino]
image: "https://miro.medium.com/max/1000/1*Xa8UkrkzVpyirla4TvSYeQ.jpeg"
featured: false
hidden: True
---



This post is going to give a gentle introduction to what is OpenVINO and how you can use it to increase vision based algorithms inference speeds.


## Intel's OpenVINO

Intel's OpenVINO is an inference framework that essentially optimizes deep learning, more specifically vision and video based processing, on a series of supported intel hardware. The intro as per Intel's documentation is as below :

>OpenVINO™ toolkit is a comprehensive toolkit for quickly developing applications and solutions that solve a variety of tasks including emulation of human vision, automatic speech recognition, natural language processing, recommendation systems, and many others. Based on latest generations of artificial neural networks, including Convolutional Neural Networks (CNNs), recurrent and attention-based networks, the toolkit extends computer vision and non-vision workloads across Intel® hardware, maximizing performance. It accelerates applications with high-performance, AI and deep learning inference deployed from edge to cloud.


## Supported hardware

The OpenVINO framework only supports a subsection of all available intel hardware products. In fact processors such as Celeron which are cheap and edge based slow CPUs which truly require the hardware acceleration do not support OpenVINO. So please be careful in checking out if your device falls under the given hardware requirements. The below link contains a list of supported processors and OS.

[ Supported Hardware ](https://software.intel.com/content/www/us/en/develop/tools/openvino-toolkit/system-requirements.html)

Even so Intel has tried to extend this framework's reach as much as possible. Currently, it supports many Intel platforms such as CPUs, GPUs, integrated GPU, intel Movidus VPU/ Neural Compute Stick and FPGAs.

## Supported Frameworks

The framework doesn't have support for all frameworks. Below is a list of officially supported frameworks that can work with OpenVINO. You can convert unsupported frameworks like Pytorch to ONNX and then run inference. Note that converting to ONNX may not always be the best option.

* Caffe
* TensorFlow
* MXNet
* ONNX
* Kaldi

## So what does OpenVINO do?

OpenVINO essentially converts your ML application into the most efficient format to run on Intel hardware. The OpenVINO framework can be used to make the best of most Intel hardware products for real-time production like inferences. Note that you cannot train with OpenVINO it is simply an inference framework.

OpenVINO consists of 2 parts for the entire inference pipeline. 
* the first step is to convert the model to the Itermediate Representation (IR) using the Model Optimizer
* the second step is to then run inference with this IR on an inference engine.


## So how does OpenVINO run an inference?

To run your model for inference with OpenVINO you will need to first convert it into an intermediate representation (IR). This IR representation is the key major factor in the accelerated performance. If you have read their documentation, they convert the models graph and layers into fused, efficient compute operations that are suitable for the Intel architecture. This IR is then fed to the OpenVINO inference engine, which runs it on any desired and supported hardware.

OpenVINO follows the write-once, deploy anywhere approach for the models it optimizes. The IR generated is independent of the hardware and will be accelerated for any hardware that this IR is supplied for.

### Further Reading and Resources

[ GITHUB ](https://github.com/openvinotoolkit/openvino) <br>
[ RELEASE NOTES ]( https://www.intel.com/content/www/us/en/developer/articles/release-notes/openvino-relnotes.html)