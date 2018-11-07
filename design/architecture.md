# Software Architecture

## Overview
Last updated: October 27th, 2018

This file is high-level idea of the basic functionality of the app from the perspective of the backend.

1. User submits photo
  * File uploader takes picture
  * (optional) in-app camera takes picture
  * Send the picture to our server via HTTPS (so that image is encrypted)
* (optional) Check to see if we have model already
  * Given an image, we can loop through our models to see if any is a good match
  * If we find a similar match, return the model
* Send picture to Google Cloud API
  * We use HTTPS to send the picture from our server to the cloud vision API
  * API returns json object:
    ```
    {
      "landmark": "suspension bridge",
      "mid": "g/unique_id",
      "score": 0.86352
    }
    ```
  * if we have never seen this landmark then store the results in our pictures database after cropping picture according to google cloud api
  * If we have seen this landmark then compare this result to the one in our database if the score is higher make this one our picture in the database.
* Search for context/description via Wikimedia API
  * We can take the landmark/tags from Google Cloud API and search for an article with Wikimedia API
  * The wikimedia API returns a snippet. In some cases, the snipped seems brief.

  NOTE: We might have to get our results from elsewhere if we cannot get more descriptive results
* Search for cheapest model from SketchFab and Turbo Squid
  * We can use the tags from our original query to the google cloud API to search SketchFab and Turbo Squid for royalty free models
  * If the price for the model is too expensive we can elect to not purchase it and convey to the user
* If we find a cheap model, buy it then charge the user a flat free of $0.99
  * We need to be able to pay(and keep track of how much we're buying) for a model
  * Once we've purchased the model, we need to integrate w/ Android Pay and Paypal for payment to the user.
