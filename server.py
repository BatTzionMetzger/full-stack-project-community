from flask import Flask, Response, request,render_template
import json
import requests

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')


@app.route('/index')
def get_main_page():
    return render_template("index.html")
 

@app.route('/communities/signup')
def get_comm_signup_page():
    pass

@app.route('/communities', methods = ["POST"])
def add_community():
    pass

@app.route('/users/signup')
def get_user_signup_page():
    pass

@app.route('/users/login')
def get_user_login_page():
    pass

@app.route('/users', methods = ["POST"])
def add_user():
    pass

@app.route('/items/upload')
def get_add_item_page():
    pass

@app.route('/items')#query_str => item_id, uploaded_items, myorder
def get_items_by_query_page():
    pass

@app.route('/items', methods = ["POST"])
def add_item():
    pass

@app.route('/items/buy/<item_id>', methods = ["PATCH"])
def buy_item(item_id):
    pass

@app.route('/communities')
def get_community_details_page():
    pass





if __name__ == '__main__':
    app.run(port=3000)