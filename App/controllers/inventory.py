from App.models import Inventory, User, Ingredient
from App.database import db

#add this
def get_user_inventory(user_id):
    return Inventory.query.filter_by(user_id=user_id).all()

def get_user_inventory_item(user_id, ingredient_id):
    it = Inventory.query.filter_by(user_id=user_id, ingredient_id=ingredient_id).first()
    if it:
        return it
    else:
        return None

##added these two functions here
def add_inventory(id, ingredient_id):
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
    
def delete_inventory(id, ingredient_id):
    item = get_user_inventory_item(id, ingredient_id)
    print(item.get_json())
    if item.user_id == id:                         #here
        db.session.delete(item)
        db.session.commit()
        return True
    return None


# chenges here
def get_all_inventory_items_json(id):
    user_inventory = Inventory.query.filter_by(user_id=id).all()
    if not user_inventory:
        return None
    inventory_list = [item.get_json() for item in user_inventory]
    return inventory_list
