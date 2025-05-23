from App.database import db

class Inventory(db.Model):
    inventory_id = db.Column(db.Integer, primary_key=True) #thinking of making this equal to the user id cause, each user only evar has 1 id
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    ingredient_id = db.Column(db.Integer, db.ForeignKey('ingredient.ingredient_id'), nullable = False)
    amount = db.Column(db.Integer)
    #has a pseudo-column called 'user'

    def __init__(self, user_id, ingredient_id, amount):
        self.user_id = user_id
        self.ingredient_id = ingredient_id
        self.amount = amount

    def get_json(self):
        return{
            "inventory_id": self.inventory_id,
            "user_id": self.user_id,
            "ingredient_id": self.ingredient_id,
            "amount": self.amount
        }
