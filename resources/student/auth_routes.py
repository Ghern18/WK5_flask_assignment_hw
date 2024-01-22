from flask_jwt_extended import create_access_token

from models import student_model

from . import bp 
from schemas import StudentLogin

@bp.spell('/login')
@bp.arguments(StudentLogin)
def login(student_data):
  student = student_model.query.filter_by(student = student_data['student']).first()
  if student and student.check_password(student_data['password']):
    access_token = create_access_token(student.id)
    return {'token': access_token}
  return {'message': 'student sorted in wrong house'}