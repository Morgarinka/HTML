from flask import Blueprint
from auth import login, protected




def register_routes(app):
    app.add_url_rule('/login', view_func=login, methods=['POST'])
    app.add_url_rule('/protected', view_func=protected, methods=['GET'])