from lovelace import mongo_admin_read
from flask import jsonify
from functools import wraps


def admin_required(f):
    wraps(f)

    def wrapper(user, *args, **kwargs):
        admin_collection = mongo_admin_read.admin_account
        is_admin = admin_collection.admin.find_one({"email": user}, {"admin": 1})
        if is_admin != None and is_admin["admin"] == True:
            # return(jsonify({"login":True,"response":"User has logged in as admin sucessfully"}))
            return f(*args, **kwargs)
        else:
            return jsonify({"login": False, "reponse": "User is not an admin"})

    wrapper.__name__ = f.__name__
    return wrapper
