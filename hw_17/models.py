from settings import db


class Students(db.Model):
    id_student = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    last_name = db.Column(db.String(40), unique=True)

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name


class Teachers(db.Model):
    id_teachers = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40))
    last_name = db.Column(db.String(40), unique=True)
    academic_subject = db.Column(db.Text)

    def __init__(self, name, last_name, academic_subject):
        self.name = name
        self.last_name = last_name
        self.academic_subject = academic_subject
