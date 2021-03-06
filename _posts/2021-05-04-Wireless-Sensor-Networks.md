---
layout: post
title: "Wireless Sensor Networks"
author: munkeops
categories: [thesis, linux]
image: "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fhecoira.leeds.ac.uk%2Fwp-content%2Fuploads%2Fsites%2F164%2F2018%2F04%2Fsensor-network.png&f=1&nofb=1"
featured: false
hidden: false
---


Wireless Sensor Networks have been quite popular for the constant monitoring of the physical conditions of the environment. Wireless Sensor Networks usually consist of multiple nodes, which each have a sensor spread across a geographical area. Each node normally belongs to a cluster, which it reports its data to when required. The cluster head keeps passing the data along from node to node until it reaches the central / head node. When passing data from cluster head to cluster head, the amount of data passed with each subsequent hop may increase with every hop. Thus, the power dissipation due to the transmission of the data increases with every hop, thereby leading to uneven overall power dissipation amongst cluster heads.

Therefore, it is imperative to minimize the amount of data passed with every hop instead of aggregating, accumulating and appending all the data together to pass it forward. A few ideas were considered during the making of this report, namely “caching of data” and the “best layout of clusters using graph theory”. However, this report primarily focuses on another method of minimizing data through compression. Two popular compressions techniques, Gunzip and Zip, have been analyzed primitively, considering power dissipation due to computation and power dissipation due to transmission over many files which consist of random and structured data.

## Intro

A Wireless Sensor Network refers to a group of spatially dispersed and dedicated sensors for monitoring and recording the physical conditions of the environment and organizing the collected data at a central location. Wireless Sensor Networks are often used to measure real-time environmental conditions such as temperature, humidity, sound, light, concentration of a pollutant in different media and movement.  

Nodes and Cluster Heads of a Wireless Sensor Network are often powered by batteries and hence, it is of the utmost importance to save as much of the power as possible. Two sources of power dissipation in a Wireless Sensor Network that we attempt to look at in this report are processing and transmission. Power dissipated by processing refers to the power dissipated when any computation is done on a processor. Though the computation done on a processor may not be the same for every unit of computation because of the different types of computation and internal optimizations of the processor architecture, we assume an average value (α) of power dissipation per unit computation.

The other source of power dissipation that we consider in this report is the power dissipated due to transmission, which includes actively listening for messages and converting a message from one medium to another. As is the same with the power dissipation due to unit computation, we assume and average value (β) of power dissipation per unit transmission.

fire. Each of these nodes, part of one cluster (an encompassing black circle), reports the information it has collected to the nearest cluster head (indicated by blue dots). Each cluster head passes the information it receives forward to either the head node or another cluster head which then repeats the same process again. The head node (indicated by a solid blue circle and highlighted by a red circle in the center of Figure 1) aggregates and accumulates the received data to take the decision of notifying whether values have crossed their configured ranges. To solidify this with an example, Figure 1 shows a fire happening in two of the clusters to the center-left of the image. Nodes in the two clusters use their temperature sensors to detect the outbreak of a fire and send a message to their cluster head. The cluster head then forwards this message until it reaches the head node which afterwards performs the necessary actions. This example is simple and is said to be event-driven i.e., the nodes only alert the cluster head only when they detect a fire. As such, the length of the message is quite small and can be less than one megabyte. Therefore, the power consumed when transmitting the message forward from one cluster head to another cluster head is quite minimal. Moreover, very less power is dissipated due to computation as there is little to no computation being done in the cluster heads.

![figure1]({{site.baseurl}}/assets/images/wsnfig1.png)


Figure 2 is an illustration of the same Wireless Sensor Network in Figure 1 with a fundamental difference that the head node collects all the temperature readings from the nodes every hour instead of listening for one or more messages. In this figure, each cluster comprises five nodes, which send their temperature readings to the cluster head. Each cluster head passes the readings onwards to another cluster head or to the 8 head node. The major issue with this type of Wireless Sensor Network is the size of the message passed from cluster head to cluster head increases with every forward due to the receiving cluster head appending its own nodes’ temperature reading.


In Figure 2, the cluster head encompassed by the orange box (center-top) receives a message which has fifteen readings from the previous cluster head. It then adds five readings from its own nodes before sending a message comprising twenty readings to the head node. Although a message comprising twenty readings may seem trivial at this instant, this scenario can be extrapolated to a real-world Wireless Sensor Network comprising hundreds or thousands of nodes distributed across multiple clusters in a very skewed spread; the power dissipated due to transmission naturally increases from one cluster head to another, thereby leading to an uneven power dissipation across cluster heads even amongst the same level.
 

On top of the power dissipated due to transmission along every new cluster head each message encounters, there will be a slight increase in power dissipation due to computation because of the appending of the current cluster’s nodes’ temperature readings. This leads us to formulate the minute yet significant solution of compression.
  

In this report, we attempt to analyze two popular compression techniques, gunzip[6] and zip[7], and compare the power dissipated due to computation by compression and transmission of the compressed file.

![figure2]({{site.baseurl}}/assets/images/wsnfig2.png)

## References

for more content on this topic please read my paper on the same - https://github.com/munkeops/Third-Year-Thesis