---
layout: post
title: "Image Search Engines"
author: munkeops
categories: [thesis,python,deep learning]
image: "https://www.artbusinessinfo.com/uploads/4/6/6/0/46602337/bing-reverse-image-search_orig.jpg"
featured: false
hidden: false
---


With the explosion of data that the web has made available for us, searching content on the internet cannot be limited to text queries. Web content is seeing a sharp rise in images and videos, with the use of Social media platforms. Video and image sharing apps have become very much popular amongst everyone carrying a smartphone these days. Apart from that movie sharing and streaming has also significantly become mainstream in current situations. Hence what if people wanted to search for items they see somewhere or in some movie and want to learn more about it. It would be amazing if we could query the web just how googling any anything is just fingertips away. Hence this blog will discuss and shed light upon the various aspects and challenges faced to create such a search engine. Our goal will be to be able to create a working search application for images. We should be able to see the internal cogs required for such an application and also discuss the advancements taking place to improve each of these sub tasks. Finally we conclude with several promising directions for future research. 


## Intro

Everyone is quite aware of the basic working of a general search engine such as Google. Search engines are essentially information retrieval applications, i.e. given an input they retrieve information that is likely to be the closest form of data available on the query. A popular known information retrieval algorithm is TF-iDF for document retrieval along with employment of clustering algorithms with it. While these are the basic building blocks of a search engine we have come a long way since then and have realised the need to create much more efficient and superior search algorithms. 

A general search engine such as Google performs document/ information retrieval from the large data bank known as the internet. Relying on simple techniques like before does not apply here. Hence crucial study has undergone to improve this algorithm time and again. Information retrieval is a major study by itself all together. Over the past two decades Google has made several advances and updates to its novel search engine. But it is not only the algorithms that have been improved over time, it is also the interaction and the way Google is able to understand a person's query. Given a query searching the most relevant and correct data is only half the aspect of an advanced search engine. The second and major part is how do we convert a humans query to machine interpretable query for utilising the efficient retrieval algorithms. What is the point of an efficient retrieval algorithm if it is not able to map the users actual query onto the algorithm?

It would be truly amazing if we could have our search engine understand our query by an image. It could be a problem as simple as trying to get information about a flower whose name I do not know but have seen grow in my garden. Traditional search engines would require one to describe the image as much as possible and create a query only to be unsure whether it is the only flower with 6 that description. Moreover people can be really bad with their descriptions, they may describe a Rose as a red flower. There are millions of varieties of flowers that can be red in color. 

A simple way could be that I put an image into the search bar and it is able to retrieve information regarding it. This has become very much possible now and major work is going on in this work and area. The potential for this kind of a search engine is very high considering the major advances in the field of image processing over the past decade. With introduction and extremely good results of Deep learning models image classification and understanding has become very easy today. Machines are able to comprehend and crunch information encapsulated in images. The processing has evolved from fourier to convolutions and have started giving very decent results. 

(for more read the paper shared below)

## Problem at hand

The problem to solve in this project when put in simple words can be spelled out as- to be able to create an application that is able to take images as inputs, comprehend them and return web related information ( cause internet is the biggest pool of information) or private database related information. In a broad sense we want to be able to search information via images. 

To do so we need the application to be able to comprehend or understand images. Just as NLP handles machines to understand language, with deep learning frameworks we must be able to understand images. In this paper we shall see the progress and growth of ideas and implementations and how certain algorithms were able to improve the quality of our search engine.

 The frameworks and modules in our current state do not allow us to be able to understand an image in a complete sense all at once unless trained carefully. Basically an image can communicate various kinds of information and our goal at a preliminary level is to first be able to extract some kind of information from it. The simplest way to go about doing so is to first get the machine to be able to differentiate between images. This task is known as classification. If given a set of curated images belonging to a finite set of classes( shirt, bag, shoes), are we able to get the application to simply differentiate an image( say of a shoe) from one another(of a shirt) by classifying them to their appropriate different classes. 

Moving ahead, by being able to do this for simple images we can now classify images into a broad sense of labels. With these labels (single label per image) we can now perform regular text queries. This uptil now seems a little naive i.e. while it is a great feat it isn't the best that can be done or rather these results don't peek any attention. Being able to classify an image and then query a word from a given set of known words is not what was the motivation behind the need for an image search engine. We want to be able to query images which may or may not even be able to be broadly classified but simply find items similar to it. A simple solution is to be able to to tag an image with multiple labels. (eg mona lisa = painting, lady, antique)

(for more read the paper shared below)
## Project Work

Below is the actual proof of concept of an easy to do self made image classification engine.

![training]({{site.baseurl}}/assets/images/ise_training.png)

the output developed in react and nodejs with tfjs displays the working product.


## References

Please read my entire thesis on this topics here - https://github.com/munkeops/Image-Search-Engine/blob/master/ProjectReport.pdf

Due to the Covid 19 I havent been able to work more in this direction but it was an important topic to me.


