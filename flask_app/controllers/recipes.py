from flask_app import app
from flask_app.models import user, recipe
from flask import Flask, render_template, redirect, session, request, flash

@app.route('/recipes')
def r_recipes():
    if 'user_id' not in session:
        flash(u'Sorry pal, you are not logged in!', 'login')
        return redirect('/login')

    print('rendering success page...')
    return render_template('recipes.html')

@app.route('/recipe/view')
def r_recipe_view(): 
    if 'user_id' not in session:
        flash(u'Sorry pal, you are not logged in!', 'login')
        return redirect('/login')

    return render_template('recipe_view.html')


@app.route('/recipe/create')
def r_recipe_create():
    if 'user_id' not in session:
        flash(u'Sorry pal, you are not logged in!', 'login')
        return redirect('/login')

    return render_template('recipe_create.html')

@app.route('/recipe/edit')
def r_recipe_update():
    # if 'user_id' != 'r_user_id':
    #     flash(u"Cheeky, aren't we?", 'login')
    if 'user_id' not in session:
        flash(u'Sorry pal, you are not logged in!', 'login')
        return redirect('/login')

    return render_template('recipe_update.html')

@app.route('/recipe/delete/<int:id>')
def d_recipe_delete(id):
    # if 'user_id' != 'r_user_id':
    #     flash(u"Cheeky, aren't we?", 'login')

    if 'user_id' not in session:
        flash(u'Sorry pal, you are not logged in!', 'login')
        return redirect('/login')

    data = {
        'id' : id
    }
    # Recipe.delete(id)
    return redirect('/recipes')
