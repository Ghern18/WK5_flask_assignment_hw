from flask import request
from uuid import uuid4

from app import app
from db import students

@app.get('/student') #route lets you run request by default!
def student():
    return {'students': list(students.values())}, 200

@app.get('/student/<student_id')
def get_student(student_id):
    try:
        return{'student': students[student_id]}
    except:
        return {'message': 'Death Eater'}, 400

@app.post('/student')
def create_student():
    student_data = request.get_json()
    for k in ['student', 'email', 'house', 'password']:
        if k not in student_data:
            return {'message': "Please include Student's email, house, and password"}
    students[uuid()] = student_data
    return {'message': f'{student_data["student"]} is sorted in a house'}, 201
              

@app.put('/student/<student_id>')
def update_student(student_id):
    try:
        student = students[student_id]
        student_data = request.get_json()
        student |= student_data
        return {'message': f'{student["student"]}'}, 202
    except KeyError:
        return {'message': "Student sorted in Wrong House"}, 400
  

@app.delete('/student/<student_id>')
def delete_student(student_id):
    try:
        del students[student_id]
        return {'message': f'student dropped out and became death eater'}, 202
    except:
        return {'message': "Invalid Student"}, 400