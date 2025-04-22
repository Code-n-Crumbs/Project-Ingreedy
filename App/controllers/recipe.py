from App.models import Recipe
from App.database import db

def create_recipe(name, directions, time):
    new_recipe = Recipe(name, directions, time)
    db.session.add(new_recipe)
    db.session.commit()
    return new_recipe

def get_recipe_by_name(name):
    return Recipe.query.filter_by(recipe_name=name).all()

def get_recipe(id):
    return Recipe.query.get(id)

def get_all_recipes():
    return Recipe.query.all()

def get_all_recipes_json():
    recipes = Recipe.query.all()
    if not recipes:
        return []
    recipes = [recipe.get_json() for recipe in recipes]
    return recipes