from flask import Flask, render_template, request
import uuid
import json


app = Flask(__name__)


@app.route('/')
def main_page():
    return "<p>Main page</p>"


@app.route('/users/new')
def users_new():
    user = {'name': '',
            'email': '',
            'password': '',
            'passwordConfirmation': '',
            'city': ''}
    errors = {}

    return render_template(
        'users/new.html',
        user=user,
        errors=errors
    )

def save_user(user):
    with open('modifying_forms_flask/users.json', 'a') as file:
        file.write(json.dumps(user) + '\n')

@app.route('/users', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        nickname = request.form.get('nickname')
        email = request.form.get('email')
        user_id = uuid.uuid4().hex
        user = {'nickname': nickname, 'email': email, 'user_id': user_id}
        save_user(user)

        # Возвращаем сообщение об успешном создании пользователя
        return f"User created! ID: {user_id}, Nickname: {nickname}, Email: {email}"

    return render_template('users/create_user.html')


