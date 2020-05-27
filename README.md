# Rando Slackbot
     
This project contains the rando slackbot with the following slash commands.

* /rando - Prints a randomly ordered list of users in the current channel

# Getting Started 

## Clone this repo
`git clone https://github.com/davidlcassidy/rando-slackbot.git` 

---
## Build the image - make sure you're in the root dir of the repo
`docker build -t rando:latest .`

---
## Run the container
`docker run -d -p 5000:5000 rando`