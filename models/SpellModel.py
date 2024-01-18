from datetime import datetime

from app import db

class SpellModel(db.Model):

  __tablename__ = 'spells'

  id = db.Column(db.Integer, primary_key = True)
  body = db.Column(db.String, nullable = False)
  timestamp = db.Column(db.String)
  student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable = False)

  def __repr__(self):
    return f'<Spell: {self.body}>'
  
  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()