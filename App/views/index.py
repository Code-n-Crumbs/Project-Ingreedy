from flask import Blueprint, redirect, render_template, request, send_from_directory, jsonify
from App.controllers import create_user, initialize
from App.controllers.ingredient import add_ingredient, get_all_ingredients_json

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
    item = add_ingredient('potato', 1, 'lbs')
    item = add_ingredient('milk', 8, 'oz')
    item = add_ingredient('butter', 4, 'oz')
    item = add_ingredient('salt', 4, 'oz')
    return jsonify(get_all_ingredients_json())