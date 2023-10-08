#!/usr/bin/env python3

from flask import Flask, make_response, request, jsonify
from flask_migrate import Migrate

from models import db, Hero, Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return jsonify({'message': 'Welcome to the Superheroes API!'})

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    heroes_list = [{'id': hero.id, 'name': hero.name, 'super_name': hero.super_name} for hero in heroes]
    return jsonify(heroes_list)

@app.route('/heroes/<int:hero_id>', methods=['GET'])
def get_hero(hero_id):
    hero = Hero.query.get(hero_id)
    if hero:
        return jsonify({'id': hero.id, 'name': hero.name, 'super_name': hero.super_name})
    else:
        return make_response(jsonify({'error': 'Hero not found'}), 404)

# routes for Powers
@app.route('/powers', methods=['GET'])
def get_powers():
    powers = Power.query.all()
    powers_list = [{'id': power.id, 'name': power.name, 'description': power.description} for power in powers]
    return jsonify(powers_list)

@app.route('/powers/<int:power_id>', methods=['GET'])
def get_power(power_id):
    power = Power.query.get(power_id)
    if power:
        return jsonify({'id': power.id, 'name': power.name, 'description': power.description})
    else:
        return make_response(jsonify({'error': 'Power not found'}), 404)

# route to update Power description 
@app.route('/powers/<int:power_id>', methods=['PATCH'])
def update_power(power_id):
    power = Power.query.get(power_id)
    if not power:
        return make_response(jsonify({'error': 'Power not found'}), 404)

    data = request.get_json()
    power.description = data.get('description', power.description)
    db.session.commit()

    return jsonify({'id': power.id, 'name': power.name, 'description': power.description})

# route to create HeroPower (POST)
@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    hero_id = data.get('hero_id')
    power_id = data.get('power_id')
    strength = data.get('strength')

    hero = Hero.query.get(hero_id)
    power = Power.query.get(power_id)

    if not hero or not power:
        return make_response(jsonify({'error': 'Hero or Power not found'}), 404)

    new_hero_power = HeroPower(hero=hero, power=power, strength=strength)
    db.session.add(new_hero_power)
    db.session.commit()

    return jsonify({'id': new_hero_power.id, 'hero_id': hero_id, 'power_id': power_id, 'strength': strength})


if __name__ == '__main__':
    app.run(port=5555)
