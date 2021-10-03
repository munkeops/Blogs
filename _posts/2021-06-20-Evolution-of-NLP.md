---
layout: post
title: "Evolution of NLP"
author: munkeops
categories: [thesis,nlp,deep learning]
image: assets/images/nlp-bert.png
featured: false
hidden: false
---



Hi guys, this post is gonna be about my study on the evolution of NLP. I presented this as my course thesis for NLP in my 4th year BTech in CSE. This blog is gonna be an overview of natural language processing techniques studied over the years and how it grew over time with DL integrations and eventually leading to discussing BERT.

# What is a language model?

Definition as per wikipedia - A statistical language model is a probability distribution over sequences of words. Given such a sequence, say of length n, it assigns a probability P to the whole sequence. 

Having a way to estimate the relative likelihood of different phrases is useful in many natural language processing applications, especially ones that generate text as an output.

# Traditional NLP

## Language Rules based models

Using grammars (modified Beam Search(greedy) / Viterbi(dynamic) )
Drawback - predicts POS tag not exact word

Language Rules based models were the first approach to getting artificial intelligence in language processing. Just like how humans follow syntactic and semantic rules in most languages, we could try and get a model to learn and understand the same. If the model could understand and intepret something as basic as meaningful sequence of words it would be a great task achieved. 

Algorithms such as modified Beam Search based on the greedy algorithm and Viterbi algorithm which is based on dynamic programming concepts were developed and were highly popular and accurate for many automated services. The models worked on studying a corpus for general grammatical rules and finding out the most probable sequence of words with  help of greedy and dynamic programming algorithms. Based the general rules (Context grammars) it was able to indentify logical positions of words based on what kind of a word it was. Algorithms such as these were widely used for senetence structure detection and understanding. 

The drawback of these algorithms were that they coudnt predict words, only the POS tags of the word that should exist at a given position.

## Ngram models 
Raw frequency count  
Drawback - dosen't take context or word meaning into account
      - corpus dependent , cases of UNK words 
      -large corpus needed

....Ngram models drawbacks led to working onWSD,  smoothing 

Then came the Ngram models. These models were trained to study a corpus and memorise the frequency count of n sequence of words. The model logic could not be argued with as it did produce decent results provided trained well. 

But again this model had several drawbacks in exchange for the exact word preditions -

- The model didnt take context or actual meaning of words into account.
- The model was highly corpus dependent, hence its frequency counts were purely based of what it has seen and consumed only, hence possibility of high Bias.
- Training such a model requires a huge corpus and the memory required to store the crunched information could also relatively be larger than other previously seen models.

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

