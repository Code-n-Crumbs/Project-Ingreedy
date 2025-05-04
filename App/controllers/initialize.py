from .user import create_user
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass')
    user_bob = create_user('bob', 'bobpass') #here
    ingredient1 = add_ingredient('Flour')
    ingredient2 = add_ingredient('Cheese')
    ingredient3 = add_ingredient('Sauce')
    ingredient4 = add_ingredient('Oil')
    ingredient5 = add_ingredient('Yeast')
    ingredient6 = add_ingredient('Italian Seasoning')
    ingredient7 = add_ingredient('Sausage')
    ingredient8 = add_ingredient('Hotdog Bread')
    ingredient9 = add_ingredient('Bread')
    ingredient10 = add_ingredient('Pasta')
    ingredient11 = add_ingredient('Sauce')
    user_add_inventory(user_bob.id, ingredient1.ingredient_id)
    user_add_inventory(user_bob.id, ingredient2.ingredient_id)
    recipe1 = create_recipe("Home Made Pizza", "Make Dough. Roll dough into circle and paste sauce. Add grated cheese. Add toppings.", 5)
    recipe2 = create_recipe("Hot Dog", "Boil Sausage. Cut bread. Add sausage to bread. Add preferred sauces.", 30)
    add_recipe_ingredient(recipe1.recipe_id, ingredient1.ingredient_id)
    add_recipe_ingredient(recipe1.recipe_id, ingredient2.ingredient_id)
    add_recipe_ingredient(recipe1.recipe_id, ingredient3.ingredient_id)
    add_recipe_ingredient(recipe1.recipe_id, ingredient4.ingredient_id)
    add_recipe_ingredient(recipe1.recipe_id, ingredient5.ingredient_id)
    add_recipe_ingredient(recipe1.recipe_id, ingredient6.ingredient_id)
    add_recipe_ingredient(recipe2.recipe_id, ingredient7.ingredient_id)
    add_recipe_ingredient(recipe2.recipe_id, ingredient8.ingredient_id)
    recipe1_ing_list = []
    recipe2_ing_list = []
    recipe1_ing_list.append(ingredient2)
    recipe1_ing_list.append(ingredient9)
    recipe2_ing_list.append(ingredient10)
    recipe2_ing_list.append(ingredient11)
    add_recipe(user_bob.id, "Simple Sandwich", "Add cheese between two slices of bread", 5, ['Bread', 'Cheese'])
    add_recipe(user_bob.id, "Spaghetti", "Boil pasta. Make sauce.", 30, ['Pasta', 'Sauce'])
