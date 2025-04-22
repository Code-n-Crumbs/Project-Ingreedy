from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
from App.controllers.ingredient import add_ingredient, get_all_ingredients_json, delete_ingredient
from App.controllers.inventory import *
from App.models import *

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

@index_views.route('/items', methods=['GET'])
def example_items():
    add_ingredient('potato', 'lbs')
    add_ingredient('milk', 'oz')
    add_ingredient('butter', 'oz')
    add_ingredient('salt', 'oz')
    return jsonify(get_all_ingredients_json()), 200

@index_views.route('/bob-inv', methods=['GET'])
def see_inventory():
    #user = User.query.filter_by(id=1).first()
    ingredient1 = add_ingredient('rice', 'lbs')
    ingredient2 = add_ingredient('chicken', 'lbs')
    ingredient3 = add_ingredient('broccoli', 'lbs')
    add_to_inventory(ingredient1, 10)
    add_to_inventory(ingredient2, 10)
    add_to_inventory(ingredient3, 10)
    return jsonify(get_all_inventory_items_json()), 200
    #return jsonify(get_all_ingredients_json())

@index_views.route('/use1', methods=['GET'])
def example_use():
    user=User.query.filter_by(id=1).first()
    inv = Inventory.query.filter_by(user_id=1).first()
    #ingredient = Ingredient.query.filter_by()
    edit_inventory_amount(user, )
    reduce_ingredient('potato', 1)
    reduce_ingredient('milk', 1)
    reduce_ingredient('butter', 1)
    reduce_ingredient('salt', 1)
    return jsonify(get_all_ingredients_json()), 200

@index_views.route('/throw-milk', methods=['GET'])
def remove_milk():
    msg = delete_ingredient('milk')
    if not msg:
        return jsonify(get_all_ingredients_json()), 200
    else:
        return jsonify(msg), 400
