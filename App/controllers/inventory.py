from App.models import Inventory
from App.database import db
from sqlalchemy.exc import IntegrityError

def add_to_inventory(user, ingredient, amount):
    try:
        new_inventory_item = Inventory(user.id, ingredient.id, amount)
        db.session.add(new_inventory_item)
        db.session.commit()
        return new_inventory_item
    except Exception as e:
        print(e)
        db.session.rollback()
        return None
    return None

def remove_from_inventory(user, ingredient):
    try:
        inventory_item = Inventory.query.filter_by(ingredient_id=ingredient.id).first()
        db.session.delete(inventory_item)
        db.session.commit()
    except Exception as e:
        print(e)
        bdb.session.rollback()
        return None
    return None
    
def get_all_inventory_items_json(user):
    inventory = Inventory.query.filter_by(user_id=user.id).all()
    if not inventory:
        return ['fuck']
    inventory_list = [item.get_json() for item in inventory]
    return inventory_list