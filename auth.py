from flask import jsonify, request
import jwt
import datetime
from functools import wraps
from config import Config
from models import User
from utils import validate_user_input



def generate_token(user_id):
    token = jwt.encode({
        'user_id': user_id,
        'exp': datetime.datetime.now() + datetime.timedelta(hours=1)
    }, Config.SECRET_KEY, algorithm='HS256')
    return token

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = request.headers.get('Authorization').split(" ")[1] if 'Authorization' in request.headers else None

        if not token:
            return jsonify({'message': 'Token is missing!'}), 401

        try:
            data = jwt.decode(token, Config.SECRET_KEY, algorithms=['HS256'])
            current_user_id = data['user_id']
        except jwt.ExpiredSignatureError:
            return jsonify({'message': 'Token has expired!'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'message': 'Invalid token!'}), 401

        return f(current_user_id, *args, **kwargs)

    return decorated

def login():
    auth = request.json
    validate_user_input(auth)  
    user = User.query.filter_by(username=auth['username']).first()  

    if user and user.password == auth['password']: 
        token = generate_token(user.username)
        return jsonify({'token': token})

    return jsonify({'message': 'Could not verify'}), 401

@token_required
def protected(current_user_id):
    return jsonify({'message': f'This is a protected route for user: {current_user_id}'})