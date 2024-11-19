# Flask Greeting API

This is a simple RESTful API built using Flask. It provides endpoints for creating, reading, updating, and deleting personalized greetings. The API supports the following HTTP methods: `GET`, `POST`, `PUT`, and `DELETE`.

## Features

- **GET /greet**: Returns a default greeting message.
- **POST /greet**: Accepts a name and returns a personalized greeting.
- **PUT /greet**: Updates a greeting message for a specific name.
- **DELETE /greet**: Deletes the greeting for a specific name.

## Getting Started

Follow these instructions to set up the project on your local machine for development and testing purposes.

### Prerequisites

1. **Python 3.x**: Make sure you have Python 3.7 or later installed.
   - You can check your Python version by running:
     ```bash
     python --version
     ```

2. **Pip**: Ensure that `pip` (Python's package installer) is installed.
   - Check with:
     ```bash
     pip --version
     ```

### Installing the Project

1. **Clone the repository** to your local machine:
   ```bash
   git clone https://github.com/your-username/Flask-API.git
   cd Flask-API
