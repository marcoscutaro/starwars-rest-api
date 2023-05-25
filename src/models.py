from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)
    
    
    def __repr__(self):
        return '<User %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "is_active": self.is_active,
            # do not serialize the password, its a security breach
        }

class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    height = db.Column(db.String(80), unique=False, nullable=False)
    mass = db.Column(db.Boolean(), unique=False, nullable=False)
    gender = db.Column(db.Boolean(), unique=False, nullable=False)
    skin_color = db.Column(db.String(120), unique=False, nullable=False)
    image = db.Column(db.String(120), unique=False, nullable=False)
    eye_color = db.Column(db.String(120), unique=False, nullable=False)
    hair_color = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Characters %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "height": self.status,
            "mass": self.species,
            "gender": self.gender,
            "skin_color": self.type,
            "image": self.image,
            "eye_color": self.url,
            "hair_color": self.created,
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), unique=True, nullable=False)
    rotation_period = db.Column(db.String(80), unique=False, nullable=False)
    orbital_period = db.Column(db.Boolean(), unique=False, nullable=False)
    diameter = db.Column(db.Boolean(), unique=False, nullable=False)
    climate = db.Column(db.String(120), unique=False, nullable=False)
    gravity = db.Column(db.String(120), unique=False, nullable=False)
    terrain = db.Column(db.String(120), unique=False, nullable=False)
    surface_water = db.Column(db.String(120), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Planets %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "rotation_period": self.status,
            "orbital_period": self.species,
            "diameter": self.gender,
            "climate": self.type,
            "gravity": self.image,
            "terrain": self.url,
            "surface_water": self.created,
        }

class Favorites(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    characters = db.Column(db.String(120), db.ForeignKey('characters.id'),unique=True, nullable=False)
    locations = db.Column(db.String(80), db.ForeignKey('locations.id'), unique=False, nullable=False)
    user_id = db.Column(db.Boolean(), db.ForeignKey('user.id'), unique=False, nullable=False)
    
    def __repr__(self):
        return '<Favorites %r>' % self.id

    def serialize(self):
        return {
            "id": self.id,
            "characters": self.characters,
            "planets": self.planets,
            "user_id": self.user_id,
            # do not serialize the password, its a security breach
        }