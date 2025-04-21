from App.models import Ingredient
from App.database import db
from sqlalchemy.exc import IntegrityError
from flask_jwt_extended import (
    get_jwt_identity,
    jwt_required,
)


def add_ingredient(ingredient_name, ingredient_amount, ingredient_unit):
    item = Ingredient.query.filter_by(ingredient_name=ingredient_name).first()
    if not item:
        item = Ingredient(ingredient_name, ingredient_amount, ingredient_unit)
        db.session.add(item)
        db.session.commit()
    else:
        item.ingredient_amount = item.ingredient_amount + ingredient_amount
        db.session.commit()


def reduce_ingredient(ingredient_name, ingredient_amount):
    ingredient = Ingredient.query.filter_by(ingredient_name=ingredient_name).first()
    if not ingredient:
        return jsonify(message='Error. Item does not exist, cannot be removed')
    else:
        if ingredient.ingredient_amount < ingredient_amount:
            return jsonify(message='Error. Trying to remove more inventory than you have in stock.')
        else:
            ingredient.ingredient_amount = ingredient.ingredient_amount - ingredient_amount
            db.session.commit()


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
