from flask import Flask, request, jsonify
from uuid import uuid4
from db import spells, students

app = Flask(__name__)

@app.get('/spell')
def get_spells():
    return jsonify({'spells': list(spells.values())})

@app.get('/spell/<spell_id>')
def get_spell(spell_id):
    try:
        spell = spells[spell_id]
        return jsonify({'spell': spell}), 200
    except KeyError:
        return {'message': "Invalid Spell ID"}, 400

@app.post('/spell')
def create_spell():
    spell_data = request.get_json()
    student_id = spell_data.get('student_id')
    if student_id and student_id in students:
        spell_id = str(uuid4())
        spells[spell_id] = spell_data
        return {'message': "Spell Created"}, 201
    return {'message': "Student needs Instructor to Practice Spell"}, 401

@app.put('/spell/<spell_id>')
def update_spell(spell_id):
    try:
        spell = spells[spell_id]
        spell_data = request.get_json()
        if spell_data.get('student_id') == spell['student_id']:
            spell['body'] = spell_data['body']
            return {'message': 'Spell Enhanced'}, 202
        return {'message': "Spell is Forbidden to Practice"}, 401
    except KeyError:
        return {'message': "Invalid Spell ID"}, 400
    except Exception as e:
        return {'message': str(e)}, 500

@app.delete('/spell/<spell_id>')
def delete_spell(spell_id):
    try:
        del spells[spell_id]
        return {'message': "Spell Cured"}, 202
    except KeyError:
        return {'message': "Invalid Spell ID"}, 400
    except Exception as e:
        return {'message': str(e)}, 500





from flask import request
from uuid import uuid4

from app import app
from db import spells, students

@app.get('/spell')
def get_spells():
    return {'spells': list(spells.values())}

@app.get('/spell/<spell_id>')
def get_spell(spell_id):
    try:
        return{'spell': spells[spell_id]}, 200
    except KeyError:
        return {'message': "Invalid Ingredients to Create Spell"}, 400