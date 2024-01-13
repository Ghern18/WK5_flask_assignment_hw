from flask import Flask, request, jsonify
from uuid import uuid4
from db import spells, students

app = Flask(__name__)

@app.get('/student')
def get_students():
    return jsonify({'students': list(students.values())}), 200

@app.get('/student/<student_id>')
def get_student(student_id):
    try:
        student = students[student_id]
        return jsonify({'student': student}), 200
    except KeyError:
        return {'message': 'Student not found'}, 404

@app.post('/student')
def create_student():
    student_data = request.get_json()
    required_fields = ['student', 'email', 'house', 'password']

    for field in required_fields:
        if field not in student_data:
            return {'message': f'Please include {field}'}, 400

    student_id = str(uuid4())
    students[student_id] = student_data
    return {'message': f'{student_data["student"]} is sorted in a house'}, 201

@app.put('/student/<student_id>')
def update_student(student_id):
    try:
        student = students[student_id]
        student_data = request.get_json()

        for k, v in student_data.items():
            student[k] = v

        return {'message': f'{student["student"]} updated'}, 202
    except KeyError:
        return {'message': 'Student not found'}, 404
    except Exception as e:
        return {'message': str(e)}, 500

@app.delete('/student/<student_id>')
def delete_student(student_id):
    try:
        del students[student_id]
        return {'message': 'Student deleted'}, 202
    except KeyError:
        return {'message': 'Student not found'}, 404
    except Exception as e:
        return {'message': str(e)}, 500