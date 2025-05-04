from App.models import RecipeIngredient, Ingredient, Inventory  ##changes here
from App.database import db

def add_recipe_ingredient(recipe_id, ingredient_id):
    new_ri = RecipeIngredient(recipe_id, ingredient_id)
    db.session.add(new_ri)
    db.session.commit()
    return new_ri

def change_missing_state(recipe_id, ingredient_id):
    ri = RecipeIngredient.query.filter_by(recipe_id=recipe_id, ingredient_id=ingredient_id).first()
    if ri:
        ri.missing = not ri.missing
        db.session.add(ri)
        db.session.commit()

def get_recipe_ingredients(recipe_id):
    return RecipeIngredient.query.filter_by(recipe_id=recipe_id).all()

def get_all_recipes_ingredients():
    return RecipeIngredient.query.all()

def get_ingredient_id_list(recipe_id):
    recipe_ingredients = get_recipe_ingredients(recipe_id)
    jon = [ri.get_json() for ri in recipe_ingredients]

    ingredients_id = []
    for json_recipe in jon:
        id = json_recipe['ingredient_id']
        #print(id)
        #ingredient = RecipeIngredient.query.filter_by(ingredient_id=id).all()
        #print(the.get_json())
        ingredients_id.append(id)

    #print(jon)
    return ingredients_id  

def get_ingredient_names(recipe_id):
    ids = get_ingredient_id_list(recipe_id)

    #print(ids)

    names = []
    for id in ids:
        the = Ingredient.query.filter_by(ingredient_id=id).first()
        the = the.get_json()
        name = the['ingredient_name']
        names.append(name)

    #print(names)
    return names

def get_missing_ingredients_count(user_id, recipe_id):

    #getting inventory ingredients for user
    i = Inventory.query.filter_by(user_id=user_id).all()
    user_inventory_json = [ri.get_json() for ri in i]

    user_inventory = []
    for uij in user_inventory_json:
        u_inventory_ing = uij['ingredient_id']
        user_ing = Ingredient.query.get(u_inventory_ing)
        user_ing = user_ing.get_json()
        u_ing_name = user_ing["ingredient_name"]
        user_inventory.append(u_ing_name.lower()) #convert to lowercase

    #getting ingredients for recipe by the id
    recipe_ingredients = get_recipe_ingredients(recipe_id)

    #print(recipe_ingredients)
    missing_ing = []
    missing_count = 0

    for item in recipe_ingredients:
        rep_ing = Ingredient.query.get(item.ingredient_id)
        rep_ing = rep_ing.ingredient_name

        if rep_ing.lower() not in user_inventory:
            #change_missing_state(item.recipe_id, item.ingredient_id)
            #print(rep_ing)
            missing_count += 1
            missing_ing.append(rep_ing)


    #print(missing)
    return missing_count
