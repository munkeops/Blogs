---
layout: post
title: "Evolution of NLP"
author: munkeops
categories: [thesis,nlp,deep learning]
image: assets/images/nlp-bert.png
featured: false
hidden: false
---

<!-- # ZeekDoc -->
 
 <!-- <p align="center">
  <img src=/Documentation/zeekLogo.png width=100>
 </p>
  -->

Hi guys, this post is gonna be about my the evolution of NLP. I presented this as my course thesis for NLP in my 4th year BTech in CSE. This blog is gonna be an overview of natural language processing techniques studied over the years and how it grew over time withDL integrations and eventually leading to discussing BERT.

# What is a language model?

A statistical language model is a probability distribution over sequences of words. Given such a sequence, say of length, it assigns a probability P to the whole sequence. 
Having a way to estimate the relative likelihood of different phrases is useful in many natural language processing applications, especially ones that generate text as an output.

# Traditional NLP

## Language Rules based models
Using grammars (modified Beam Search(greedy) / Viterbi(dynamic) )
Drawback - predicts POS tag not exact word

## Ngram models 
Raw frequency count  
Drawback - dosen't take context or word meaning into account
      - corpus dependent , cases of UNK words 
      -large corpus needed

....Ngram models drawbacks led to working onWSD,  smoothing 


## Word Embeddings
Solution to all problems faced by traditional NLP models.
Represent words as vectors
Each word can be represented by a set of features eg, gender, royalty etc.
Each word :  300 feats -> 300 length vector.  
Advantage - using vector spaces to denote similarity in words. (cosine similarity)

# Deeplearning in NLP

Word embeddings are just numerical representation of words. 
It isnt expected for people to encode embeddings for each word manually     ....tedious task 
Solution - Word2Vec / GloVe

