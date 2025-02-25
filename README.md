# dweller
A re-implementation of the MakersBnB project in Django

Dweller is a Django-based property booking web application inspired by platforms like Airbnb. It serves as a portfolio project that demonstrates the creation of a modular, full-stack application using Django, HTMX, and PostgreSQL.

## Overview

Dweller allows property owners to create listings and users to browse and book properties. The project is designed as a Minimum Viable Product (MVP) with room for future enhancements. It features:

- User authentication (registration, login, logout)
- Property listing management (create, view, and filter listings)
- Basic booking functionality 
- Dynamic UI updates with HTMX

## Features

- **User Authentication:**  
  Secure user registration, login, and session management using Django's built-in auth system.

- **Property Listings:**  
  Property owners can add listings with details like title, description, price, location, and images. Listings are displayed on a dynamic home page.

- **Booking Functionality:**  
  Users can book properties for available dates. The booking model uses PostgreSQL’s native `DateRangeField` for handling date ranges.

- **Dynamic Content with HTMX:**  
  The homepage includes category filters that use HTMX to asynchronously update the property grid without a full page reload.

## Tech Stack

- **Backend:** Python, Django
- **Frontend Enhancements:** HTMX
- **Database:** PostgreSQL
- **Environment Management:** pipenv

## Installation

Follow these steps to set up the project locally:

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/your-project.git
   cd your-project
   ```

2. Create and activate the pipenv environment:
    ```bash
    pipenv --python 3.x #Use your desired Python version
    pipenv shell
    ```
3. Install dependencies:
    ```bash
    pipenv install
    ```

4. Configure your database:
    - Create a PostgreSQL database
    - Update your Django project's settings.py with your database credentials.

5. Apply migrations:
    ```bash
    python manage.py migrate
    ```
6. Create a superuser (for Django admin):
    ```bash
    python manage.py createsuperuser
    ```
7. Run the development server:
    ```bash
    python manage.py runserver
    ```
8. Access the application:
    - Open your browser and navigate to ==http://127.0.0.1:8000/== to view the home page.

## Usage
- For property Owners:
    Log in and navigate to the listing creation page to add your property details.
- For users:
    Browse the homagepage to view available proeprties. Use the category filters to dynamically udpate the listing grid. Click on a property to view details and book it for a specific date.

## License
This project is license under the MIT License.
