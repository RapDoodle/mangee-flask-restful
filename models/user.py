from core.db import db
from utils.hash import hash_data


class UserModel(db.Model):
    """The model related to users.

    To satisfy more requirements, add more fields to the model.
    Make sure to register them in the constructor.

    Note:
        Changing the name of the field `id` is not recommended since JWT
        will, by default, look for the attribute `id` in the model. For
        more information if the name of the field is changed, consult 
        https://pythonhosted.org/Flask-JWT/ 
        for the topic `identity_handler(callback)`

    Attributes:
        id (Integer): user's id
        username (String): user's username
        password_hash (LargeBinary): user's hashed password

    """
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32))
    password_hash = db.Column(db.LargeBinary(60))

    def __init__(self, username, password):
        # Clean the data
        username = str(username).strip()
        password = str(password).strip()

        # TODO: Verification for the inputs

        # Hash the password
        password_hash = hash_data(password)

        # Store the data in the object
        self.username = username
        self.password_hash = password_hash

    def save(self):
        db.session.add(self)
        db.session.commit()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
