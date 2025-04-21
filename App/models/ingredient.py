from App.database import db

class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_name = db.Column(db.String(225), nullable=False)
    ingredient_recipe = db.relationship('RecipeIngredient', backref='ingredient', lazy=True)
    ingredient_amount = db.Column(db.Integer, nullable = False)
    ingredient_unit = db.Column(db.String(64), nullable=False)

    def __init__(self, name, amount, unit):
        self.ingredient_name = name
        self.ingredient_amount = amount
        self.ingredient_unit = unit

    def get_json(self):
        return{
            "ingredient_id": self.ingredient_id,
            "ingredient_name": self.ingredient_name,
            "ingredient_amount": self.ingredient_amount,
            "ingredient_unit": self.ingredient_unit
        }
