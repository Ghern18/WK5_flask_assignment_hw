from flask import Flask, request
from uuid import uuid4
from flask.views import MethodView

from . import bp
from db import students

from schemas import StudentSchema


@bp.route('/student/<student_id>')
class Student(MethodView):
    @bp.response(200,StudentSchema)
    def get(self, student_id):
        try:
            return students[student_id]
        except:
            return {'message': 'Student not found'}, 400
        
    @bp.arguments(StudentSchema)
    def put(self, student_data, student_id):
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

    def delete(self, student_id):
        try:
            del students[student_id]
            return {'message': f'Student deleted'}, 202
        except KeyError:
            return {'message': 'Student not found'}, 404
        except Exception as e:
            return {'message': "Student is a Muggle"}, 500

@bp.route('/student')   
class UserList(MethodView):
    
    @bp.response(200, StudentSchema(many = True))
    def get(self):
        return list(students.values())
    
    @bp.arguments(StudentSchema)
    def post(self, student_data):
        students[uuid4()] = student_data
        return { 'message' : f'{student_data["student"]} created'}, 201

#@bp.response(200, StudentSchema(many=True))
#@bp.get('/student')
#def student():
#    return {'students': list(students.values())}

#@bp.post('/student')
#@bp.arguments(StudentSchema)
#def create_student(student_data):
#    students[uuid4()] = student_data
#    return { 'message' : f'{student_data["student"]} created'}, 201


#@bp.get('/student/<student_id>')
#@bp.response(200, StudentSchema)
#def get_student(student_id):
#    try:
#        return {'student': students[student_id]}
#    except:
#        return {'message': 'Student not found'}, 400


#@bp.put('/student/<student_id>')
#def update_student(student_id):
#    try:
#        student = students[student_id]
#        student_data = request.get_json()

#        for k, v in student_data.items():
#            student[k] = v

#        return {'message': f'{student["student"]} updated'}, 202
#    except KeyError:
#        return {'message': 'Student not found'}, 404
#    except Exception as e:
#        return {'message': str(e)}, 500

#@bp.delete('/student/<student_id>')
#def delete_student(student_id):
#    try:
#        del students[student_id]
#        return {'message': 'Student deleted'}, 202
#    except KeyError:
#        return {'message': 'Student not found'}, 404
#    except Exception as e:
#        return {'message': str(e)}, 500