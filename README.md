# python-code-challenge-superheroes

### Superheroes API

Welcome to the Superheroes API! This API allows you to manage superheroes, their powers, and relationships between heroes and powers.


## Getting Started

# Prerequisites

Before running the Superheroes API, make sure you have the following installed:

- Python 3
- Flask
- Flask-Migrate
- SQLite (or another supported database)

# Installation

1. Clone the repository:

   git clone https://github.com/joycewachira/flask-cc-2-superheroes-.git

2. Navigate to the project directory:

cd code-challenge/app

3. Install dependencies:

pip install -r requirements.txt

4. Initialize the database:

flask db init

5. Apply migrations:

    flask db migrate
    flask db upgrade

# Usage
Run the Server

To start the Superheroes API server, run:

python3 app.py

By default, the server runs on port 5555. You can access the API at http://localhost:5555/.
Endpoints

    GET /heroes: Get a list of all heroes.
    GET /heroes/{hero_id}: Get details of a specific hero by ID.
    GET /powers: Get a list of all powers.
    GET /powers/{power_id}: Get details of a specific power by ID.
    PATCH /powers/{power_id}: Update the description of a power.
    POST /hero_powers: Create a new hero-power relationship.

Refer to the API documentation for detailed information on each endpoint.

# Contributing

If you would like to contribute to the Superheroes API, follow these steps:

    Fork the repository on GitHub.
    Clone your forked repository.
    Create a new branch for your feature or bug fix.
    Make your changes and commit them.
    Push your changes to your forked repository.
    Submit a pull request.

# License

This project is licensed under the MIT License - see the LICENSE file for details.