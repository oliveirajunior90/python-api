from api.database import SessionLocal
from api.models import User as UserModel
from .schema import User as UserSchema

class UsersView(object):

    def __init__(self, app, prefix):
        db = SessionLocal()

        @app.get(prefix)
        def get_all_users():
            return db.query(UserModel).all()
        
        @app.post(prefix)
        def create(user : UserSchema):
            db_user = UserModel(email=user.email, hashed_password=user.password)
            db.add(db_user)
            db.commit()
            return db_user
            
        