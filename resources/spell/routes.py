from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import SpellModel
from schemas import SpellSchema, SpellSchemaNested

from . import bp


@bp.route('/<spell_id>')
class Spell(MethodView):

    @bp.response(200, SpellSchemaNested)
    def get(self, spell_id):
        Spell = SpellModel.query.get(spell_id)
        if Spell:
            return Spell 
        abort(400, message='Spell is Forbidden to Cast')
   
    @jwt_required
    @bp.arguments(SpellSchema)
    def put(self, spell_data ,spell_id):
        spell = SpellModel.query.get(spell_id)
        if spell and spell.student_id == get_jwt_identity():
            spell.body = spell_data['body']
            spell.commit()   
            return {'message': 'spell rendered'}, 201
        return {'message': "Spell is Forbidden to Cast"}, 400

    @jwt_required()
    def delete(self, spell_id):
        spell = SpellModel.query.get(spell_id)
        if spell and spell.student_id == get_jwt_identity():
            spell.delete()
            return {"message": "Spell Redacted"}, 202
        return {'message':"Spell is Forbidden to Cast"}, 400


@bp.route('/')
class SpellList(MethodView):


    @bp.response(200, SpellSchema(many = True))
    def get(self):
        return SpellModel.query.all()
    
    @bp.arguments(SpellSchema) 
    def post(self, spell_data):
        try:
            spell = SpellModel()
            spell.student_id = get_jwt_identity() 
            spell.body = spell_data['body']
            spell.commit()
            return { 'message': "Spell Casted" }, 201
        except:
            return { 'message': "Student in need of Professor to Cast Spell"}, 401   

    



#@bp.get('/')
#def get_spells():
#    return ({'spells': list(spells.values())})

#@bp.get('/<spell_id>')
#def get_spell(spell_id):
#    try:
#        spell = spells[spell_id]
#        return({'spell': spell}), 200
#    except KeyError:
#        return {'message': "Invalid Spell ID"}, 400

#@bp.post('/')
#def create_spell():
#    spell_data = request.get_json()
#    student_id = spell_data.get('student_id')
#    if student_id and student_id in students:
#        spell_id = str(uuid4())
#        spells[spell_id] = spell_data
#        return {'message': "Spell Created"}, 201
#    return {'message': "Student needs Instructor to Practice Spell"}, 401

#@bp.put('/<spell_id>')
#def update_spell(spell_id):
#    try:
#        spell = spells[spell_id]
#        spell_data = request.get_json()
#        if spell_data.get('student_id') == spell['student_id']:
#            spell['body'] = spell_data['body']
#            return {'message': 'Spell Enhanced'}, 202
#        return {'message': "Spell is Forbidden to Practice"}, 401
#    except KeyError:
#        return {'message': "Invalid Spell ID"}, 400
#    except Exception as e:
#        return {'message': str(e)}, 500

#@bp.delete('/<spell_id>')
#def delete_spell(spell_id):
#    try:
#        del spells[spell_id]
#        return {'message': "Spell Cured"}, 202
#    except KeyError:
#        return {'message': "Invalid Spell ID"}, 400
#    except Exception as e:
#        return {'message': str(e)}, 500
