from flask import Flask, jsonify
from mock_data import courses, students

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False  # 让中文正常显示

@app.route('/api/courses', methods=['GET'])
def get_courses():
    return jsonify({"courses": courses})

@app.route('/api/students', methods=['GET'])
def get_students():
    return jsonify({"students": students})

if __name__ == '__main__':
    app.run(debug=True)