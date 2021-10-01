---
layout: post
title: "Wireless Sensor Networks"
author: munkeops
categories: [thesis, linux]
image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhecoira.leeds.ac.uk%2Fwp-content%2Fuploads%2Fsites%2F164%2F2018%2F04%2Fsensor-network.png&f=1&nofb=1"
featured: false
hidden: false
---

## Background

Wireless Sensor Networks have been quite popular for the constant monitoring of the physical conditions of the environment. Wireless Sensor Networks usually consist of multiple nodes which each have a sensor spread across a geographical area. Each node normally belongs to a cluster which it reports its data to when required. The cluster head keeps passing the data along from node to node until it reaches the central / head node. When passing data from cluster head to cluster head, the amount of data passed with each subsequent hop may increase with every hop due to the accumulation of multiple and thus, the power dissipation due to the transmission of the data increases with every hop thereby leading to uneven overall power dissipation amongst cluster heads.

Therefore, it is imperative to minimize the amount of data being passed with every hop instead of aggregating, accumulating and appending all the data together to pass it forward. A few ideas have been considered during the making of this report namely caching and the best spread of clusters using graph theory. However, this report primarily focuses on another method of minimizing data through compression. Two popular compressions techniques, Gunzip and Zip, have been analyzed primitively considering power dissipation due to computation and power dissipation due to transmission over a large number of files
which consist of random and structured data.

## Intro

A Wireless Sensor Network refers to a group of spatially dispersed and dedicated sensors for monitoring and recording the physical conditions of the environment and organizing the collected data at a central location. Wireless Sensor Networks are often used to measure real-time environmental conditions  such as temperature, humidity, sound, light, concentration of a pollutant in different media and movement. Nodes and Cluster Heads of a Wireless Sensor Network are often powered by batteries and hence, it is of the utmost importance to save as much as power as possible. Two sources of power dissipation in a Wireless Sensor Network that we attempt to look at in this report are processing and transmission. Power dissipated by processing refers to the power dissipated when any computation is done on a processor. Though the computation done on a processor may not be the same for every unit of computation because of the different types of computation and internal optimizations of the processor architecture, we assume an average value (α) of power dissipation per unit computation. The other source of power dissipation that we consider in this report is the power dissipated due to transmission which includes actively listening for messages and converting a message from one medium to another. As is the same with the power dissipation due to unit computation,
we assume and average value (β) of power dissipation per unit transmission.