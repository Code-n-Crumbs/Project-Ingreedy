from App.models import RecipeIngredient, Ingredient
from App.database import db

def add_recipe_ingredient(recipe_id, ingredient_id):
    new_ri = RecipeIngredient(recipe_id, ingredient_id)
    db.session.add(new_ri)
    db.session.commit()
    return new_ri

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