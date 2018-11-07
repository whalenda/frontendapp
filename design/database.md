# Database Design

## Overview
Last updated: October 27th, 2018

Our current design consists of four main tables:
  * `Accounts`
  * `Models`
  * `UserModels`
  * `Pictures`

## `Accounts`
This table stores the account information for users when they elect to create an account.

### Columns
  * `email` PRIMARY KEY => email of user
  * `password` => salted password of user

## `Models`
This table stores the data for each model we have, but they associate of the model with a given user.

### Columns
  * `name` => name of landmark
  * `id` PRIMARY KEY => unique key for each model
  * `path` => path of the model on the server
  * `mid` => unique id from google cloud api that will allows us to gather more information on the object
  * `description` => the description of the landmark

## `UserModels`
This table stores the models that a user a paid for

### Columns
  *  `email`
  * `modelID` => refers to ID
  * (`email`, `modelID`) pair should be unique

## `Pictures`
This table keeps track of the "best" picture that gives us a certain model.

### Columns
  * `modelID` PRIMARY KEY
  * `score` => the confidence score from google cloud API
  * `path` => path to the picture 
