from flask import Flask, request, jsonify
from uuid import uuid4

app = Flask(__name__)

student = {
 '1': {
    'student': 'harry',
    'email' : 'harrypotter@ct.com',
 },
 '2' : {
    'student': "ron",
    'email': 'ronweasley@ct.com',
 },
 '3' : {
    'student': "hermione",
    'email': 'hermionegranger@ct.com',
 }
}

spell = [
 {
    'id': '1',
    'body': "Expeliamus!!"
 },
 {
    'id': '2',
    'body': "Stupify!"
 },
]

#CRUD Operations
#Create - POST
#Restreive - GET
#Update - PUT
#Delete

#user routes

@app.route('/student', methods=['GET']) #route lets you run request by default!
def get_student():
    return jsonify(student)

@app.route ('/student', methods=["POST"])
def create_student():
    json_body = request.get_json()
    student[uuid4()] = {'student': json_body["student"], 'email': json_body["email"]}
    return jsonify({'message': f'{json_body["student"]} created'})

@app.route('/student', methods=["PUT"])
def update_student():
    json_body = request.get_json()
    student_id = json_body.get('id')
    if student_id:
        if student_id in student:
            student[student_id]['student'] = json_body['student']
            student[student_id]['email'] = json_body['email']
            return jsonify({'message': f'Student {student_id} updated'})
        else:
            return jsonify({'error': f'Student with id {student_id} not found'})
    else:
        return jsonify({'error': f'Student id not provided'})

@app.route('/student', methods=["DELETE"])
def delete_student():
    json_body = request.get_json()
    student_id = json_body.get('id')
    if student_id:
        if student_id in student:
            del student[student_id]
            return jsonify({'message': f'Student {student_id} deleted'})
        else:
            return jsonify({'error': f'Student with id {student_id} not found'})
    else:
        return jsonify({'error': f'Student id not provided'})

#post routes
@app.route('/spell', methods=['GET'])
def get_spell():
    return jsonify(spell)

@app.route('/spell', methods=['POST'])
def create_spell():
    json_body = request.get_json()
    spell.append({'id': uuid4(), 'body': json_body['body']})
    return jsonify({'message': f'Spell created'})

@app.route('/spell', methods=['PUT'])
def update_spell():
    json_body = request.get_json()
    spell_id = json_body.get('id')
    if spell_id:
        spell_to_update = next((spell for spell in spell if spell['id'] == spell_id), None)
        if spell_to_update:
            spell_to_update['body'] = json_body['body']
            return jsonify({'message': f'Spell {spell_id} updated'})
        else:
            return jsonify({'error': f'Spell with id {spell_id} not found'})
    else:
        return jsonify({'error': f'Spell id not provided'})

@app.route('/spell', methods=['DELETE'])
def delete_spell():
    json_body = request,

