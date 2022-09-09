from flask_app import app
from flask_app.models.user import User
from flask import Flask, render_template, redirect, session, request, flash

@app.route('/recipes')
def r_recipes(): 
    return render_template('recipes.html')

@app.route('/recipe/view')
def r_recipe_view(): 
    return render_template('recipe_view.html')

@app.route('/recipe/create')
def r_recipe_create():
    return render_template('recipe_create.html')

@app.route('/recipe/edit')
def r_recipe_update():
    return render_template('recipe_update.html')

@app.route('/recipe/delete/<int:id>')
def d_recipe_delete(id):
    data = {
        'id' : id
    }
    # Recipe.delete(id)
    return redirect('/recipes')
