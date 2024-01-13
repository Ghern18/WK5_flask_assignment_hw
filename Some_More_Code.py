#from flask import request
#from uuid import uuid4

#from app import app
#from db import students

#@app.get('/student') #route lets you run request by default!
#def student():
#    return {'students': list(students.values())}, 200

#@app.get('/student/<student_id>')
#def get_student(student_id):
#    try:
#        return{'student': students[student_id]}
#    except:
#        return {'message': 'Death Eater'}, 400

#@app.post('/student')
#def create_student():
#    student_data = request.get_json()
#    for k in ['student', 'email', 'house', 'password']:
#        if k not in student_data:
#            return {'message': "Please include Student's email, house, and password"}
#    students[uuid4()] = student_data
#    return {'message': f'{student_data["student"]} is sorted in a house'}, 201
              

#@app.put('/student/<student_id>')
#def update_student(student_id):
#    try:
#        student = students[student_id]
#        student_data = request.get_json()
#        student |= student_data
#        return {'message': f'{student["student"]}'}, 202
#    except KeyError:
#        return {'message': "Student sorted in Wrong House"}, 400
#  

#@app.delete('/student/<student_id>')
#def delete_student(student_id):
#    try:
#        del students[student_id]
#        return {'message': f'student dropped out and became death eater'}, 202
#    except:
 #       return {'message': "Invalid Student"}, 400

####################################################################################### Type Errors

#from flask import request
#from uuid import uuid4

#from app import app
#from db import spells, students

#@app.get('/spell')
#def get_spells():
#    return {'spells': list(spells.values())}

#@app.get('/spell/<spell_id>')
#def get_spell(spell_id):
#    try:
#        return{'spell': spells[spell_id]}, 200
#    except KeyError:
#        return {'message': "Invalid Ingredients to Create Spell"}, 400

#@app.post('/spell')
#def create_spell():
#    spell_data = request.get_json()
#    print(spell_data, '=============================\n\n')
#    student_id = spell_data['student_id']
#    if student_id in students:
#        spells[uuid4()] = spell_data
#        return {'message': "Spell Created"}, 201
#    return {'message': "Student needs Instructor to Practice Spell"}, 401

#@app.put('/spell/<spell_id>')
#def update_spell(spell_id):
 #   try:
 #       spell = spell[spell_id]
 #       spell_data = request.get_json()
 #       if spell_data['student_id']==spell['student_id']:
 #           spell['body'] = spell_data['body']
 #           return {'message': 'Spell Enhanced'}, 202
 #       return {'message': "Spell is Forbidden to Practice"}, 401
 #   except:
 #       return {'message': "Invalid Ingredients to Create Spell"}, 400

#@app.delete('/spell/<spell_id>')
#def delete_spell(spell_id):
#    try:
#        del spells[spell_id]
#        return {'message': "Spell Cured"}, 202
#    except:
#        return {'message': "Invalid Ingredients to Create Spell"}, 400
########################################################################################## Type Errors