from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app
from flask_app.models import user
from flask import flash
import re

class Recipe:
    def __init__ (self,data:dict) -> object:
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.cooked_date = data['cooked_date']
        self.under_30 = data['under_30']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_recipes = []

    @classmethod
    def get_all(cls:object) -> list:
        query = '''
        SELECT * FROM recipes;
        '''
        results = connectToMySQL('recipes').query_db(query)

        all_recipes = []

        for recipes in results:
            all_recipes.append(cls(recipes))
        
        if not all_recipes:
            return False
        
        return all_recipes
    
    @classmethod
    def get_one(cls:object, data:dict) -> object:
        query = '''
        SELECT * FROM recipes WHERE id = %(id)s;
        '''

        result = connectToMySQL('recipes').query_db(query, data)

        if not result:
            return False

        return cls(result[0])

    @classmethod
    def add_recipe_post(cls, data:dict) -> None):
        query = '''
        INSERT INTO 
        posts (user_id, recipe_id)
        VALUES(%(user_id)s, %(recipe_id)s);
        '''

        return connectToMySQL('recipes').query_db(query,data)

    @classmethod
    def get_recipes_with_user(cls, data:dict) -> list:
        query = '''
        SELECT * FROM posts
        JOIN users ON user_id = users.id
        JOIN recipes ON recipe_id = recipes.id
        WHERE user_id = %(user_id)s;
        '''

        results = connectToMySQL('recipes').query_db(query,data)

        if results != 0:
            user_post = cls(results[0])

            for row in results:
                user_data = {
                    'id' : row.get('users.id'),
                    'first_name' : row.get('users.first_name'),
                    'last_name' : row.get('users.last_name'),
                    'email' : row.get('users.email'),
                    'password' : "Nice try, loser",
                    'created_at' : row.get('users.created_at'),
                    'updated_at' : row.get('users.updated_at')
                }

            user_post.user_recipes.append(user.User(user_data))

            return user_post

        else:
            print('OOOOOPSIIEEE POOOPSIEEEE! EMPTY QUERRRYYYY!')
