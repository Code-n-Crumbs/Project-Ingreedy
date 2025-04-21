from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
from App.controllers.ingredient import add_ingredient, get_all_ingredients_json, reduce_ingredient, delete_ingredient

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
    add_ingredient('potato', 1, 'lbs')
    add_ingredient('milk', 8, 'oz')
    add_ingredient('butter', 4, 'oz')
    add_ingredient('salt', 4, 'oz')
    return jsonify(get_all_ingredients_json()), 200

@index_views.route('/use1', methods=['GET'])
def example_use():
    reduce_ingredient('potato', 1)
    reduce_ingredient('milk', 1)
    reduce_ingredient('butter', 1)
    reduce_ingredient('salt', 1)
    return jsonify(get_all_ingredients_json()), 200

@index_views.route('/throw-milk', methods=['GET'])
def remove_milk():
    delete_ingredient('milk')
    return jsonify(get_all_ingredients_json()), 200
