# HOTEL
#### Video Demo: 
#### Description: basic hotel management system with dedicated admin and user panels.

## requirements: python3, flask, any web browser(tested on google chrome)
## usage: run the command {python3 app.py} and flask should handle the rest and return a local address to a virtual server. accessing the said address would get you into the admin-login page. log in using the user and password stored in admin.py. the username and password can be modified to your liking.

## details: uses a 2D array to store the rooms, each row is a floor. each room is a room object as per the class blueprint in hotel_room.py. uses another 2D array to keep track of reservation records and another as a bit-array to confirm date availability during reservation.

## each room ID is in the following format: Floor(1-2^64) - Number of beds(1-5) - Number in the floor(1-9)

## to check out more complex data structures used, please access ds.py

## Disclaimer: THIS PROJECT IS NOT SUITABLE FOR ANY FORM OF SERIOUS/COMMERTIAL USE. ANY LOSS REGARDING THE USAGE OF THE PROJECT IS ON THE USER. this project was made merely as a final project to a course and serves no other purpose.