from marshmallow import Schema, fields

class Student(Schema):
    id = fields.Str(dump_only = True)
    student = fields.Str(requuired = True)
    email = fields.Str(required = True)
    house = fields.Str(required = True)
    password = fields.Str(required = True, Load_only = True)
    first_name = fields.Str(required = True)
    last_naem = fields.Str(required = True)


class Spell(Schema):
    id = fields.Str(dump_only = True)
    body = fields.Str(required = True)
    timestamp = fields.DateTime(dump_only = True)