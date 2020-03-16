import os
from flask import Flask, render_template, jsonify
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager
from models import db, Family



BASE_DIR = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.url_map.strict_slashes = False
app.config['DEBUG'] = True
app.config['ENV'] = 'development'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'dev.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


db.init_app(app)
Migrate(app, db)
manager = Manager(app)
manager.add_command("db", MigrateCommand)


@app.route('/')
def root():
    return render_template('index.html')


@app.route('/member', methods=['GET', 'POST'])
def person_group():

    if request.method == 'GET':
        respuesta_body = {
            "members": myFamily.get_all_members(),
            "family_name": myFamily.last_name,
            "lucky_numbers": [],
            "sum_of_lucky": 1
        }

        return jsonify(respuesta_body), 200


    if request.method == 'POST':
        body = request.get_json()
        if 'name' not in body:
            return 'You need to specify the first_name',400
        if 'age' not in body:
            return 'You need to specify the last_name', 400
        if 'gender' not in body:
            return 'You need to specify the gender', 400
        if 'lucky_number' not in body:
            return 'You need to specify the lucky number', 400
            
        respuesta = myFamily.add_member(body)
        return jsonify(respuesta), 200

@app.route('/member/<int:member_id>', methods=['DELETE', 'PUT'])
def person():
    if request.method == 'DELETE':
        respuesta = myFamily.delete_member(member_id)

        return jsonify(respuesta), 200

    if request.method == 'PUT':
        respuesta = myFamily.add_member(member_id)
        return jsonify(respuesta), 200










if __name__ == '__main__':
    manager.run()


