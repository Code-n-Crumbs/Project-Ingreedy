from werkzeug.security import check_password_hash, generate_password_hash
from App.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)
    inventory_ingredients = db.relationship('Inventory', backref='user',lazy=True, cascade="all, delete-orphan")
    recipes = db.relationship('UserRecipe', backref='user', lazy=True, cascade="all, delete-orphan") # there is a 'user' psudo-column on UserRecipes table. One to many relationship.

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username,
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)
