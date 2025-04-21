from App.models import *
from App.database import db

def create_user(username, password):
    newuser = User(username=username, password=password)
    db.session.add(newuser)
    db.session.commit()
    return newuser

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user(id):
    return User.query.get(id)

def get_all_users():
    return User.query.all()

def get_all_users_json():
    users = User.query.all()
    if not users:
        return []
    users = [user.get_json() for user in users]
    return users

def update_user(id, username):
    user = get_user(id)
    if user:
        user.username = username
        db.session.add(user)
        return db.session.commit()
    return None

def add_recipe(id, name, directions, time, ingredients):
        new_recipe = Recipe(name=name, directions=directions, time=time)
        db.session.add(new_recipe)
        db.session.flush() #temporarily store a struture for it so that there is an id for ingredients to map to 

        #ingredient_list = ingredients.split(',')

        #ingredients will be a list of ingredient names
        for ingredient in ingredients: 
            exist = Ingredient.query.filter_by(ingredient_name=ingredient).first()

            if not exist:
                exist = Ingredient(ingredient)
                db.session.add(exist)
                db.session.flush()

        correlation_ri = RecipeIngredient(recipe_id=new_recipe.recipe_id, ingredient_id=exist.ingredient_id)
        db.session.add(correlation_ri)

        new_user_recipe = UserRecipe(id, new_recipe.recipe_id)
        db.session.add(new_user_recipe)
        db.session.commit()

        return new_recipe.get_json()
