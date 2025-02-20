# JobPortal Project

Welcome to the JobPortal project! This project is a web application built using the Django framework.

## Features

- User Authentication (Login/Signup)
- Company registration
- Job CRUD functionality (Create, Read, Update, Delete)

## Table of Contents

1. [Installation](#installation)
2. [Setup](#setup)
3. [Running the Project](#running-the-project)


## Installation

To set up the project locally, follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/MandarParekh007/JobPortal-Django.git
   cd jobportal

2. Create a Virtual Environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate

3. Install required dependencies:
    ```bash
    pip install -r requirements.txt

## Setup

Before running the project, you’ll need to set up the database and other environment variables:


1. Run database migrations to set up the tables:
    ```bash
    python manage.py migrate
    ```

2. Create superuser for Django admin panel:
    ```bash
    python manage.py createsuperuser
    ```

## Running the Project

1. To start the development server:
    ```bash
    python manage.py runserver
    ```

    