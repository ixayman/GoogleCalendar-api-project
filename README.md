
## Google Calendar API Project

Introduction

Welcome to the Google Calendar API Project! This repository contains the code and documentation for managing calendars and events using the Google Calendar API. The project leverages Google's official Python client library to interact with the API.
Project Overview

This project demonstrates how to create, read, update, and delete calendars and events using the Google Calendar API. It includes examples of authentication, authorization, and API usage to help you integrate Google Calendar functionality into your applications.
## Features

#### Tests for:

   - Create Calendar: Add a new calendar to the user's Google Calendar account.
   - Update Calendar: Modify the details of an existing calendar.
   - List Calendars: Retrieve a list of all calendars in the user's account.
   - Delete Calendar: Remove a calendar from the user's account.
   - Create Event: Add a new event to a specific calendar.
   - Update Event: Modify the details of an existing event.
   - List Events: Retrieve a list of all events in a specific calendar.
   - Delete Event: Remove an event from a specific calendar.
## Technologies Used

    1. Python: The primary programming language used for the project.
    2. Google API Python Client: The official Python client library for Google APIs.
    3. OAuth2: For user authentication and authorization.
## Environment Variables

To run this project, you will need to add the following environment variables to your project

`Client_secret`

To acquire youre own secret file follow these steps:

    1. set up google Oauth consent 
    2. set up credentials
        - choose *desktop app* for python
        - choose *web app* if you want to use postman



## Installation

Clone the repository:

```bash
git clone https://github.com/ixayman/api-final-project.git
```


Install the required dependencies:
```bash
pip install google-api-python-client
pip install google-auth-oauthlib
```
## API Reference

#### google explains it better, go to:

```http
  https://developers.google.com/calendar/api/guides/overview
```




## Demo

#### add an event to your calendar using insert:

```bash
  event = {
    'summary': 'Sample Event',
    'start': {
        'dateTime': '2024-07-22T10:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
    'end': {
        'dateTime': '2024-07-22T12:00:00-07:00',
        'timeZone': 'America/Los_Angeles',
    },
}

event = service.events().insert(calendarId='primary', body=event).execute()
```

## 🚀 About Me
I'm a QA Automation student

![alt text](https://img.freepik.com/free-photo/cute-domestic-kitten-sits-window-staring-outside-generative-ai_188544-12519.jpg?t=st=1721654368~exp=1721657968~hmac=166aa1c7d3886de485e8a8dc9c5306a061f4afa96a78f65c0175f75608bc8384&w=2000)

