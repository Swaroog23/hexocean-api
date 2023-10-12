# hexocean-api
Recruitment task for Hexocean

## Project overview
Core components of this projects are:
 - Django
 - Django Rest Framework
 - Pillow
 - PostgreSQL
Main function of this projects is to allow users to save images and recive links to thumbnails. Size of thumbnails is based on tiers.

## Endpoints
Aviable endpoints are:
 - /images/image <- Allows GET and POST from logged django users. On GET lists all saved images connected to user. On POST, returns links to endpoints with thumbnails
 - /uploads/<str:link> <- Allows GET. Returns basic tier of thumbnails, which is image of height 200px
 - /uploads/premium/<str:link> <- Allows GET. Returns premium tier of thumbnails, which is image of height 400px
 - /uploads/enterprise/<str:link> <- Allows GET. Returns original image

## Admin Panel
In django admin panel, you can set new users and assign them tiers. Every user must be a django user in order to use api endpoints

## Project setup
Project is set in docker compose. <br>
All you need to do is to execute command "docker compose up". <br>
Before starting django server, the aplication creates three user tiers and and admin user. <br>
User has a "Enterprise" tier set, so that you can explore the application fully. <br>
