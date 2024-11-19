from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api, reqparse, fields, marshal_with, abort

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)
api = Api(app)

class UserModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    message = db.Column(db.String(180), unique=True, nullable=False)
    name = db.Column(db.String(80), unique=True, nullable=False)
    def __repr__(self):
        return f"(message={self.message}, name={self.name})"

user_args = reqparse.RequestParser()
user_args.add_argument("message", type=str, required=True, help="Greeting is required")
user_args.add_argument("name", type=str, required=True, help="Name is required")

userFields = {
    'id': fields.Integer,
    'message': fields.String,
    'name': fields.String
}


class Users(Resource):
    @marshal_with(userFields)
    def get(self):
        users = UserModel.query.all()
        return users
    
    @marshal_with(userFields)
    def post(self):
        args = user_args.parse_args()
        user = UserModel(message=args['message'], name=args['name'])
        db.session.add(user)
        db.session.commit()
        users = UserModel.query.all()
        return users, 201
    
class User(Resource):
    @marshal_with(userFields)
    def get(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        return user
    
    @marshal_with(userFields)
    def patch(self, id):
        args = user_args.parse_args()
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        user.message = args['message']
        user.name = args["name"]
        db.session.commit()
        return user
    
    @marshal_with(userFields)
    def delete(self, id):
        user = UserModel.query.filter_by(id=id).first()
        if not user:
            abort(404, message="User not found")
        db.session.delete(user)    
        db.session.commit()
        users = UserModel.query.all()
        return users #, 204

api.add_resource(Users, '/greet/')
api.add_resource(User, '/greet/<int:id>')

@app.route('/')
def hello():
    return '<h1>Hello! Flask Rest API</h1>'

#run the app on localhost and 5000
if __name__ == '__main__':
    app.run(debug=True)