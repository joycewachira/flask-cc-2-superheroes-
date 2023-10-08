#!/usr/bin/env python3

from datetime import datetime
from flask import Flask
from models import db, Power, Hero, HeroPower

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def seed():
    # Create the Flask app and push the app context
    app = create_app()
    app.app_context().push()

    print("🦸‍♀️ Seeding powers...")

    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    # Create instances of the Power model and add them to the session
    for power_info in powers_data:
        power = Power(**power_info)
        db.session.add(power)

    db.session.commit()

    print("🦸‍♀️ Seeding heroes...")

    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        {"name": "Gwen Stacy", "super_name": "Spider-Gwen"},
        {"name": "Janet Van Dyne", "super_name": "The Wasp"},
        {"name": "Wanda Maximoff", "super_name": "Scarlet Witch"},
        {"name": "Carol Danvers", "super_name": "Captain Marvel"},
        {"name": "Jean Grey", "super_name": "Dark Phoenix"},
        {"name": "Ororo Munroe", "super_name": "Storm"},
        {"name": "Kitty Pryde", "super_name": "Shadowcat"},
        {"name": "Elektra Natchios", "super_name": "Elektra"}
    ]

    # Create instances of the Hero model and add them to the session
    for hero_info in heroes_data:
        hero = Hero(**hero_info)
        db.session.add(hero)

    db.session.commit()

    print("🦸‍♀️ Adding powers to heroes...")

    strengths = ["Strong", "Weak", "Average"]
    
    # Loop through each hero and assign random powers
    for hero in Hero.query.all():
        for _ in range(randint(1, 3)):
            # get a random power
            power = Power.query.order_by(func.random()).first()

            hero_power = HeroPower(hero=hero, power=power, strength=choice(strengths))
            db.session.add(hero_power)

    db.session.commit()

    print("🦸‍♀️ Done seeding!")

if __name__ == '__main__':
    from random import randint, choice
    from sqlalchemy.sql import func
    seed()
