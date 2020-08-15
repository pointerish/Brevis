# Brevis
A simple URL shortener API with Python and Flask.

Brevis is live at:
https://brevis-shortener.herokuapp.com/

## Brevis URL Shortener
Brevis accepts a POST request to `/shorten` containing a JSON formatted as such:

`{"url":"Long URL goes here."}`

This POST request will return a json containing an ID for the URL. The client should then send a GET request to `https://brevis-shortener.herokuapp.com/URLID` which will redirect to the original URL.

Of course, the Heroku domain is long and beats the purpose of the shortener, but this is just a proof of concept and a learning project.
