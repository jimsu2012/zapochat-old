# Zapochat

A Real Time Chat Application made with Python (Flask) and JavaScript

## What is it?

Zapochat allows users to send text messages and images to each other in real time. When a user visits Zapochat, a dialog box pops up asking for the user's name, which is stored in local memory so the user does not have to reinput it the next time.

Users can send messages in different rooms in Zapochat. They can change their room with a dropdown/button at the top right corner. The dropdown displays all the rooms that have been created and the user can create/join a room by pressing the button.

Users can send messages in rooms. When a user sends a message, it is displayed with their name and date/time sent, up to a hundred messages per room stored in server-side memory (though more can be seen on a client's page).

## Where is it?

Zapochat is deployed at [zapochat.herokuapp.com](https://zapochat.herokuapp.com).

Please note that the chat app will take up to ten seconds to load because it runs on Heroku's free plan, which sleeps if a site is inactive for over 30 minutes.
