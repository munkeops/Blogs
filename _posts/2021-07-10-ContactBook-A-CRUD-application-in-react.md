---
layout: post
title: "ContactBook A CRUD application in ReactJS"
author: munkeops
categories: [react, mongodb, project]
image: assets/images/contactbook.png
featured: false
hidden: false
---



Hey, so this post is gonna be about a simple CRUD application made in React with node js for the backend, connecting to a Mongo Atlas Instance. This post and project aims at providing an overview of the project and final product.

## ContactBook

The application is a simple cloud based contact book. It supports the basic Create Read Update and Delete operations and contiains just a handful of details. The user must register and login to use the application based on which the contact information is stored. A cloud based contact book can be accessed from any device and from any location with just a login.

## Additional Features

The application supports some additional features as experimentation on my end -
- Google Captcha for registration
- Responsive website that can be opened on mobile phones and tab as well.

## Development tools

For this application I used GitLab for version control and continous integration. At the time of this project Github Actions was not fully developed to the current extent hence gitlab was the go to choice. With its CD pipelines I could easily deploy the application to preferred choice of nodes. The data for the application was directly stored in the mongo. Mongo's js package "Mongoose" package was extremely handy eliminating the need for a backend. With mongoose you can directly push/insert/retrieve data from any mongo instance provided its connection string.

## Deployment Tools

Gitlab's CI/CD pipeline was the go to choice for deployment to Heroku. At the time i was new to git and hence used the heroku cli to push code to the heroku repo for publishing but later updated it to Gitlabs CI/CD. Mongo instance for deployment was the mongo atlas, since its a scalable and cloud based deployment of mongo with a free tier.

## Results 

Vist the website and have a look at the final product - https://contact-book-rn.herokuapp.com/

Visit the github repo to have a look at the source code - https://github.com/munkeops/ContactBook
