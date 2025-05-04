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

## added back these two functions
#ingredient would be created then passed through this function
def user_add_inventory(id, ingredient_id):
    ingredient = Ingredient.query.get(ingredient_id)
    if ingredient:
        try:
            new_inventory = Inventory(id, ingredient_id)
            db.session.add(new_inventory)
            db.session.commit()
            return new_inventory
        except Exception as e:
            print(e)
            db.session.rollback()
            return None
    return None
    
def user_delete_inventory(id, ingredient_id):
    item =  Inventory.query.filter_by(user_id=id, ingredient_id=ingredient_id).first()
    if item.user_id == id:                         #here
        db.session.delete(item)
        db.session.commit()
        return True
    return None

def add_recipe(id, name, directions, time, ingredients):
        new_recipe = Recipe(name=name, directions=directions, time=time)
        db.session.add(new_recipe)
        db.session.flush() #temporarily store a struture for it so that there is an id for ingredients to map to 

        #ingredient_list = ingredients.split(',')

        #ingredients will be a list of ingredient names
        for ingredient in ingredients: 
            exist = Ingredient.query.filter(Ingredient.ingredient_name.ilike(ingredient)).first()

            if not exist:
                ingredient = Ingredient(ingredient)
                db.session.add(ingredient)
                db.session.commit()
                exist = ingredient

            correlation_ri = RecipeIngredient(recipe_id=new_recipe.recipe_id, ingredient_id=exist.ingredient_id)
            db.session.add(correlation_ri)

        new_user_recipe = UserRecipe(id, new_recipe.recipe_id)
        db.session.add(new_user_recipe)
        db.session.commit()

        return new_recipe.get_json()
