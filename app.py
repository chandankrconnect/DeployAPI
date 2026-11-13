
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "success": True,
        "message": "Welcome to my deployed Flask API"
    })

@app.route('/students')
def students():
    student_list = [
        {"id": 1, "name": "Rahul"},
        {"id": 2, "name": "Anjali"},
        {"id": 3, "name": "Kiran"}
    ]

    return jsonify({
        "success": True,
        "students": student_list
    })

if __name__ == '__main__':
    app.run(debug=False)
