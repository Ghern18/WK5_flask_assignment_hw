from app import db

from werkzeug.security import generate_password_hash, check_password_hash

class StudentModel(db.Model):

    __tablename__ = 'students'

    student_id = db.Column(db.Integer, primary_key = True)
    student = db.Column(db.String(50), nullable = False, unique = True)
    email = db.Column(db.String(75), nullable = False, unique = True)
    password_hash = db.Column(db.String(250), nullable = False)
    first_name = db.Column(db.String(30))
    last_name = db.Column(db.String(30))

    def __repr(self):
        return f'<Student: {self.student}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def commit(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, student_dict):
        for k, v in student_dict.items():
            if k != 'password':
                setattr(self, k, v)
            else:
                setattr(self, 'password_hash', generate_password_hash(v))
        # self.password_hash = v

 