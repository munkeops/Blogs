---
layout: post
title: "Poke2 : A full stack game"
author: munkeops
categories: [full stack,react,node,ci/cd,mongodb]
image: assets/images/poke2.png
featured: false
hidden: false
---



Hi guys, here I am gonna talk about my full stack project Poke2 was developed in collaboration with Qurram and Khaliq from my college. The game is my first attempt at a full fletched dyanamic full stack web application with CI/CD and a microservice architecture. 

## Stack

We used the MERN stack for this application. Mongo Atlas served as our database, while the front end was developed in ReactJS. The backend is developed in a node-express server and is independent of the front end. 

## Architecture

We followed the Micro Service Architecture for deployment. The micro service architecutre essentially entails that different aspects/features of the project can be worked on independently and deployed separately. In this manner the application is not a whole and hence in case of an issue the entire website dosent need to brought down. We can continue to work and upgrade independent features and incorporate them onto websites.

## CI/CD

Continuous Integration and Continuous deployment is an important aspect when dealing with web projects that are service based. Continuous Integration deals with being able to continuously integrate new changes to the base code without breaking the application. With the use of Gitlab which also serves as a version control system where we were able to work independently on different aspects of the website and continuously integrate. We developed feature branches for each of us to incorporate new features and dev, test and production branches for incorporating the agile methodology of development (did not follow entirely for this project as it was just the three of us). Since we follow the Micro Service Architecture we worked independently on different features of the front end and backend. While one of us worked on the front end, another worked on the backend and another on the game logic and features. Once the features were incorporated they would be tested/checked and then pushed to the master branch which had an automated CD setup. It would run some checks on the code and then push it to our production servers in heroku. 

## Game Idea

The game is suppose to be a replica with our own touch to it of the popular pokemon game. The pokeAPI served as our data pool for the pokemons abilities, figurines,stickers,actions etc and so was used intensively in developing the project (another form/application of microservice). The official documentation also consisted of a variety of formulas that could be used to develop the game logic for scoring and attack and effects. 

## Implementation Logics involved

Since it had to be a 1v1 game we had to develop an application that could dynamically assign rooms and communicate with the server and with the player all efficiently and in real time. We employed the use of websockets for active communication. 



