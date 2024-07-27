from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample questions and answers
questions = [
    {"question": "What is the capital of France?", "options": ["Paris", "London", "Rome"], "answer": "Paris"},
    {"question": "What is 2 + 2?", "options": ["3", "4", "5"], "answer": "4"},
    {"question": "What is the largest planet in our Solar System?", "options": ["Earth", "Jupiter", "Mars"], "answer": "Jupiter"}
]

@app.route('/')
def index():
    return render_template('index.html', questions=questions)

@app.route('/submit', methods=['POST'])
def submit():
    score = 0
    for i, question in enumerate(questions):
        user_answer = request.form.get(f'question_{i}')
        if user_answer == question['answer']:
            score += 1
    return render_template('result.html', score=score, total=len(questions))

if __name__ == '__main__':
    app.run(debug=True)
