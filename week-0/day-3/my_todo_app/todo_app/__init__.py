import os

from flask import Flask
from flask import request
from flask import render_template



#global variable
todo_store={}
todo_store['hemant']=['aa', 'bb', 'cc']
todo_store['shivang']=['aaa','bbb','ccc']
todo_store['depo']=['a','b','c']

 
def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass


    def insert_todo(name,todo):
        global tode_store
        current_todos=todo_store[name]
        current_todos.append(todo)
        return current_todos


    def select_todos(name):
        global todo_store
        return todo_store[name]

    def add_todo_by_name(name,todo):
        try:           
            return insert_todo(name,todo)
        except:
            return None 
        
    def get_todos_by_name(name):
        try:
            return select_todos(name)
        except:
            return None

    @app.route('/todos')
    def todos():
        name=request.args.get('name')
        print(name)
        list=get_todos_by_name(name);
        #return todo_view(list)
        if list==None:
            return render_template('my404.html'),404
        else:
            return render_template('todo_view.html',todos=list)

    @app.route('/add_todos')
    def add_todos():
        name=request.args.get('name')
        todo=request.args.get('todo')
        print(name,todo)
        list=add_todo_by_name(name,todo)
        #return "added succesfull"
        #list=get_todos_by_name(name);
        #return todo_view(list)
        if list==None:
            return render_template('my404.html'),404
        else:
            return render_template('todo_view.html',todos=list)
        


    return app

