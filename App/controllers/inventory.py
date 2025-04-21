from App.models import Inventory, User
from App.database import db
from sqlalchemy.exc import IntegrityError

def add_to_inventory(ingredient, amount):
    user = User.query.filter_by(id=1).first()
    try:
        new_inventory_item = Inventory(user.id, ingredient.ingredient_id, amount)
        db.session.add(new_inventory_item)
        db.session.commit()
        #print('WATCH OUT!!!!')
        #print(new_inventory_item)
        return new_inventory_item
    except Exception as e:
        print(e)
        db.session.rollback()
        return None
    return None

def remove_from_inventory(user, ingredient): # why is user here???
    try:
        inventory_item = Inventory.query.filter_by(ingredient_id=ingredient.ingredient_id).first()
        db.session.delete(inventory_item)
        db.session.commit()
    except Exception as e:
        print(e)
        bdb.session.rollback()
        return None
    return None
    
def get_all_inventory_items_json():
    user = User.query.filter_by(id=1).first()
    #print(user.username) # gets bob
    inventory_list = Inventory.query.filter_by(user_id=user.id).all() #issue is here
    #print(inventory_list)
    if not inventory_list:
        return []
    inventory_list = [item.get_json() for item in inventory_list]
    return inventory_list