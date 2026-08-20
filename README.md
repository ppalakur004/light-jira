##
The objective
-we are building an application which is similar to JIRA that allows users to  create, view, update, and delete support tickets.

##High Level Plan
-Build the API Design
-Build the Database schema using Mysql and connect python to SqlAlchemy
-connect the API endpoints with the sql backend
-Use pydantic to Validate the Requests
-Test the api endpoints with the FASTAPI endpoint.
-Once we have the working Basic Backend startbuilding the frontend and connect backend and frontend.

##Api Design
POST /tickets
GET /tickets
GET /tickets/{ticket_id}
PUT /tickets/{ticket_id}
DELETE /tickets/{ticket_id}

##Database design
-build Tables for Users
-Table for Tickets 
-status codes
-valid priorities

##Testing


##Acceptance Criterta

