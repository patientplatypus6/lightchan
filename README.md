# Lightchan Project

This is an open source image board. What I want to do here is create image board software that is relatively easy to understand and set up, runs using the latest GUI interface (using React), and is open source so that it can be modified and built upon by the community. The reason that this project exists is that there are both numerous image boards (such as 4chan, 8chan etc) that are anonymous by design, but the software is either old or deprecated. There is not much in the way of development in this area. On the other end of the spectrum there are social media sites such as Reddit and Facebook that are large, rely on a reputation system, and have closed source software. People are at the mercy of algorithms they often do not understand in order to drive profits for major companies. 


This software is a standalone piece of programming that anyone can build and create their own image board, and with a little knowledge of programming can customize their image board to their liking. In the future it may be possible to link these image boards together to share data, all with the understanding that the final product would be not-for-profit, anonymous, and not driven by an AI designed to maximize revenue.

The only knowledge that is required to build and run this software should be a base understanding of Python/Django, a base understanding of React, and a base understanding of how Docker and Docker Compose can spin up the two applications. NGINX is used to run and host pictures. In the future it *may* be desireable to host micro services for added functionality in other languages, or to create a sharded database system, but for the moment the code is simple by design.

In order to run this project cc into `lightchan/backend/` (where the `docker-compose.yml` file is located) and `sudo run.sh`. This project has been created on mac using Docker for Mac, so if you are instead using docker for linux or are running on a linux cloud provider run the following commands: 

`sudo docker system prune -a -f --volumes`
`sudo docker-compose build`
`sudo docker-compose up`

