# Quiz Generator

**Quiz Generator** is a simple web application that allows users to take quizzes on various topics. Built with Python's Flask framework for the backend and HTML/CSS for the frontend, this project provides a basic interface for displaying multiple-choice questions and calculating scores.

## Features

- **Dynamic Quiz Interface**: Presents a set of predefined multiple-choice questions.
- **User Input Handling**: Collects user responses and computes results.
- **Score Calculation**: Displays the user's score based on correct answers.
- **Basic Styling**: Includes minimal CSS to improve the visual presentation.

## Project Structure

- **`app.py`**: Main Python script that sets up the Flask application, defines routes, and handles form submissions.
- **`templates/`**: Contains HTML templates for rendering the quiz and results pages.
  - `index.html`: Displays the quiz questions and options.
  - `result.html`: Shows the quiz results and score.
- **`static/`**: Directory for static assets such as CSS.
  - `styles.css`: Contains styles for the application.
- **`requirements.txt`**: Lists the Python dependencies needed to run the application.

## Installation

To get started with the Quiz Generator, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <your-github-repo-url>
   cd <repository-folder>

Create a Virtual Environment
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate

Install Dependencies:
pip install -r requirements.txt

Run the Application:
python app.py
