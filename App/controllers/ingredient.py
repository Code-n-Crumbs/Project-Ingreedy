from App.models import Ingredient
from App.database import db

def get_ingredient_by_id(ingredient_id):
    return Ingredient.query.get(ingredient_id)


def add_ingredient(ingredient_name):
    exist = Ingredient.query.filter(Ingredient.ingredient_name.ilike(ingredient_name)).first() #ilike handles case sensitivity
    if not exist:
      try:
        item = Ingredient(ingredient_name)
        db.session.add(item)
        db.session.commit()
        return item
      except Exception as e:
        print(e)
        db.session.rollback()
        return None
    return exist

def add_temp_ingredient(ingredient_name):
    exist = Ingredient.query.filter(Ingredient.ingredient_name.ilike(ingredient_name)).first()
    if not exist:
        new_temp_item = Ingredient(ingredient_name)
        db.session.add(new_temp_item)
        db.session.flush()
        return new_temp_item
    return exist


def delete_ingredient(ingredient_name):
    ingredient = Ingredient.query.filter_by(ingredient_name=ingredient_name).first()
    if ingredient:
        db.session.delete(ingredient)
        db.session.commit()
        return True
    return None

def get_all_ingredients_json():
    ingredients = Ingredient.query.all()
    if not ingredients:
        return []
    ingredients = [ingredient.get_json() for ingredient in ingredients]
    return ingredients
