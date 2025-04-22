from App.models import Ingredient
from App.database import db
from sqlalchemy.exc import IntegrityError


def add_ingredient(ingredient_name, ingredient_unit):
    item = Ingredient(ingredient_name, ingredient_unit)
    db.session.add(item)
    db.session.commit()
    return item


def delete_ingredient(ingredient_name):
    ingredient = Ingredient.query.filter_by(ingredient_name=ingredient_name).first()
    db.session.delete(ingredient)
    db.session.commit()


def get_all_ingredients_json():
    ingredients = Ingredient.query.all()
    if not ingredients:
        return []
    ingredients = [ingredient.get_json() for ingredient in ingredients]
    return ingredients
