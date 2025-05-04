from App.models import *
from App.database import db

def get_user_recipe(user_id, recipe_id):
    user_recipe = UserRecipe.query.filter_by(user_id=user_id,recipe_id=recipe_id).first()
    if user_recipe:
        return user_recipe
    else:
        return None
    
def get_all_user_recipes(user_id):
    return UserRecipe.query.filter_by(user_id=user_id).all()
