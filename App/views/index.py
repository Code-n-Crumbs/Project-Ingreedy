from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify, flash
from flask_jwt_extended import jwt_required, current_user, unset_jwt_cookies, set_access_cookies
from App.models import *
from App.controllers import *

index_views = Blueprint('index_views', __name__, template_folder='../templates')

@index_views.route('/', methods=['GET'])
def index_page():
    return render_template('index.html')

@index_views.route('/init', methods=['GET'])
def init():
    initialize()
    return jsonify(message='db initialized!')

@index_views.route('/health', methods=['GET'])
def health_check():
    return jsonify({'status':'healthy'})


## New View Pages

@index_views.route('/user', methods=['GET'])
@index_views.route('/user/recipe/<int:recipe_id>', methods=['GET'])
@jwt_required()
def user_page(recipe_id=None):
    all_recipes = get_all_recipes_json()

    if recipe_id is None and all_recipes:
        recipe_id = all_recipes[0]['recipe_id']

    user_inventory = get_user_inventory(current_user.id)
    the_recipe = get_recipe(recipe_id)
    recipe_ing = get_recipe_ingredients(the_recipe.recipe_id)
    missing_ing = get_missing_ingredients_count(current_user.id, recipe_id)

    recipe_info = []
    for recipe in all_recipes:
        #print(recipe)
        r_id = recipe['recipe_id']
        recipe_count = get_missing_ingredients_count(current_user.id, r_id)
        recipe_info.append({'recipe_id': recipe["recipe_id"],'recipe_name': recipe["recipe_name"], 'count': recipe_count})

    inventory = []
    for item in user_inventory:
        the = get_ingredient_by_id(item.ingredient_id)
        inventory.append(the)
        #print(the.get_json())

    r_ingrdients = []
    for item in recipe_ing:
        the = get_ingredient_by_id(item.ingredient_id)
        inventory_ids = {i_item.ingredient_id for i_item in inventory}

        if_missing = item.ingredient_id not in inventory_ids
        if item.missing != if_missing:
            change_missing_state(item.recipe_id, item.ingredient_id)

        #print(item.get_json())
        r_ingrdients.append({'ingredient_name': the.ingredient_name, 'missing': item.missing})
        # print(the.get_json())

    return render_template('index.html', current_user=current_user, recipes=recipe_info, ingredients=inventory, selected_recipe=the_recipe, ri=r_ingrdients, missing_ing=missing_ing)


@index_views.route('/createRecipe', methods=['GET'])
@jwt_required()
def create_new_recipe():
    return render_template('createRecipe.html', ingredients=new_ingredients)


## Action Routes

@index_views.route('/ingredient/add', methods=['POST'])
@jwt_required()
def add_user_inventory():
    data = request.form
    ingredient_name = data["ingredient_name"]
    new_ingredient = add_ingredient(ingredient_name)
   
    if new_ingredient:
        user_add_inventory(current_user.id, new_ingredient.ingredient_id)
        flash(f'Ingredient {new_ingredient.ingredient_name} added successfully!')
    else:
        flash('Please enter a valid ingredient name.', 'error')

    return redirect(request.referrer)


@index_views.route('/ingredient/delete/<int:ingredient_id>', methods=['GET'])
@jwt_required()
def remove_inventory(ingredient_id):
    inventory_item = get_user_inventory_item(current_user.id, ingredient_id)
    
    if not inventory_item:
        flash('You do not have permission to delete inventory.', 'error')
    else:
        user_delete_inventory(current_user.id, ingredient_id)
        flash(f'Item deleted!', 'success')

    return redirect(request.referrer)

new_ingredients = []
@index_views.route('/add-temp-ingredient', methods=['POST'])
@jwt_required()
def user_add_temp_ingredient():
    data = request.form
    #new_ingredient = add_temp_ingredient(data['ingredient_name'])
    #print(data['ingredient_name'])
    new_ingredients.append(data['ingredient_name'])
    #print(new_ingredients)
    return redirect(request.referrer)

@index_views.route('/delete-temp-ingredient/<string:ingredient>', methods=['GET'])
@jwt_required()
def user_delete_temp_ingredient(ingredient):
    global new_ingredients
    new_ingredients = [item for item in new_ingredients if item != ingredient]
    return redirect(request.referrer)

@index_views.route('/submit-recipe', methods=['POST'])
@jwt_required()
def user_add_recipe():
    data = request.form
    name=data["new_recipe_name"]
    directions=data['directions']
    time=data['time_taken']
    ingredients=new_ingredients
    add_recipe(current_user.id, name, directions, time, ingredients)
    new_ingredients.clear()

    flash(f'Recipe Added!', 'success')
    return redirect(request.referrer)
