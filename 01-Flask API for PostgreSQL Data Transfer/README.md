# PostgreSQL Python Service with Flask API

This repository features a Python service that facilitates data transfer between PostgreSQL databases using a Flask API. The service selects records from a source database, inserts them into a target database, and exposes the data in JSON format via a POST request endpoint.

## Features

- Connect to PostgreSQL databases
- Execute SELECT and INSERT queries
- Return query results as JSON
- Flask API to handle POST requests

## Prerequisites

- Python 3.x
- Flask
- psycopg2

## Configuration

Update the database connection details in the `Database` class initialization.

## Included Databases

Two PostgreSQL database dumps are included in this repository:

dvdrental.sql: A database with a full actor table.
dvdrentalinsert.sql: A database with an empty actor table.
When the API is called, the service will select 10 actor records from the dvdrental database and insert them into the dvdrentalinsert database.

## Usage

### Run the Flask application

```bash
python app.py
```

### Make a POST request to the service

Use tools like curl, Postman, or any HTTP client to make a POST request to the /transfer-records endpoint.
Example using curl:

```bash
curl -X POST http://127.0.0.1:5000/transfer-records
```

The service will return the selected records in JSON format along with HTTP status code 201 (Created).
Example:

```json
{
    "message": "Records Inserted.",
    "status": "success",
    "data": [
        {
            "actor_id": 1,
            "first_name": "Penelope",
            "last_name": "Guiness"
        },
        {
            "actor_id": 2,
            "first_name": "Nick",
            "last_name": "Wahlberg"
        },
        {
            "actor_id": 3,
            "first_name": "Ed",
            "last_name": "Chase"
        },
        {
            "actor_id": 4,
            "first_name": "Jennifer",
            "last_name": "Davis"
        },
        {
            "actor_id": 5,
            "first_name": "Johnny",
            "last_name": "Lollobrigida"
        },
        {
            "actor_id": 6,
            "first_name": "Bette",
            "last_name": "Nicholson"
        },
        {
            "actor_id": 7,
            "first_name": "Grace",
            "last_name": "Mostel"
        },
        {
            "actor_id": 8,
            "first_name": "Matthew",
            "last_name": "Johansson"
        },
        {
            "actor_id": 9,
            "first_name": "Joe",
            "last_name": "Swank"
        },
        {
            "actor_id": 10,
            "first_name": "Christian",
            "last_name": "Gable"
        }
    ]
}
```
