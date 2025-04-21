from App.database import db

class Ingredient(db.Model):
    ingredient_id = db.Column(db.Integer, primary_key=True)
    ingredient_source = db.Column(db.Integer, db.ForeignKey('inventory.inventory_id'))
    ingredient_name = db.Column(db.String(225), nullable=False)
    ingredient_recipe = db.relationship('RecipeIngredient', backref='ingredient', lazy=True) #RI has an ingredient pseudo-column
    ingredient_unit = db.Column(db.String(64), nullable=False)

    def __init__(self, name, unit,):
        self.ingredient_name = name
        self.ingredient_unit = unit

    def get_json(self):
        return{
            "ingredient_id": self.ingredient_id,
            "ingredient_name": self.ingredient_name,
            "ingredient_unit": self.ingredient_unit
        }
