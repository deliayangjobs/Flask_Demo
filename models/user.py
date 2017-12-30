from db import db

class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    #use email as username
    username = db.Column(db.String(80))
    email = db.Column(db.String(80))
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    password = db.Column(db.String(80))

    def __init__(self, options):
        self.username = options.username
        self.password = options.password
        self.firstname = options.firstname
        self.lastname = options.lastname
        self.email = options.email

    def json(self):
        return {'username':self.username, 'email':self.email, 'firstname':self.firstname, \
                'lastname':self.lastname, 'userid':self.id}

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()


    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
