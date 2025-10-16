def validate_user_input(data):
    if not data.get('username') or not data.get('password'):
        raise ValueError("Username and password are required.")