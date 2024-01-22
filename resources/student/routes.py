from flask import request

from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import abort
from . import bp
from schemas import StudentSchema, StudentSchemaNested
from models.student_model import StudentModel


@bp.route('/student/<student_id>')
class Student(MethodView):

    @bp.response(200,StudentSchemaNested)
    def get(self,student_id):
        student = StudentModel.query.get(student_id)
        if student:
            print(student.spells.all())
            return student
        else:
            abort(400, message='Studnet not found in campus')

    @jwt_required()   
    @bp.arguments(StudentSchema)
    def put(self, student_data, student_id):
        student = StudentModel.query.get(get_jwt_identity())
        if student and student.id == student_id:
            student.from_dict(student_data)
            student.commit()
            return { 'message': f'{student.student} sorted in a house'}, 202
        abort(400, message = "Student not found in campus")

    @jwt_required()
    def delete(self, student_id):
        student = StudentModel.query.get(get_jwt_identity())
        if student==student_id:
            student.delete()
            return { 'message': f'Student: {student.student} Expelled!' }, 202
        return {'message': "Student not found in campus"}, 400

@bp.route('/student')   
class StudentList(MethodView):
    
    @bp.response(200, StudentSchema(many = True))
    def get(self):
        return StudentModel.query.all()
    
    @bp.arguments(StudentSchema)
    def post(self, student_data):
        try: 
            student = StudentModel()
            student.from_dict(student_data)
            student.commit()
            return { 'message' : f'{student_data["Student"]} sorted in a House!' }, 201
        except:
            abort(400, message='Student Sorted in the Wrong House')

      
@bp.route('/student/follow/<followed_id>')
class FollowUser(MethodView):

  @jwt_required()
  def post(self, followed_id):
    followed = StudentModel.query.get(followed_id)
    follower =StudentModel.query.get(get_jwt_identity())
    if follower and followed:
      follower.follow(followed)
      followed.commit()
      return {'message':'followed student'}
    else:
      return {'message':'student not found on campus'}, 400
    
  @jwt_required()  
  def put(self, followed_id):
    followed = StudentModel.query.get(followed_id)
    follower = StudentModel.query.get(get_jwt_identity())
    if follower and followed:
      follower.unfollow(followed)
      followed.commit()
      return {'message':'unfollowed student'}
    else:
      return {'message':'student not found in campus'}, 400

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