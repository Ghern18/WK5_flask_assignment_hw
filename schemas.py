from marshmallow import Schema, fields

class StudentSchema(Schema):
    id = fields.Str(dump_only = True)
    student = fields.Str(requuired = True)
    email = fields.Str(required = True)
    house = fields.Str(required = True)
    password = fields.Str(required = True, Load_only = True)
    first_name = fields.Str()
    last_name = fields.Str()


class SpellSchema(Schema):
    student_id = fields.Str(dump_only = True)
    body = fields.Str(required = True)
    timestamp = fields.DateTime(dump_only = True)
    student_id = fields.Str(required = True)

