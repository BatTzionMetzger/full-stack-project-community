from flask import Flask, Response, request,render_template, make_response, redirect
import json
import requests
from string_utils import is_valid_email, is_valid_phone
from models import community, item, user

app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')

@app.route('/signup', methods = ['POST'])
def signup():
    print("insigup")
    email = request.form['email']
    print("The email address is '" + email + "'")
    return render_template("login.html")



@app.route('/<page>')
def get_main_page(page):
    user_email = request.cookies.get("user_email")
    if user_email:
        response = make_response(render_template(page))
        response.set_cookie("user_email", user_email)
        return response
    return render_template(page)
 


@app.route('/communities/signup')
def get_comm_signup_page():
    user_email = request.cookies.get("user_email")
    print(user_email)

@app.route('/communities', methods = ["POST"])
def add_community():
    req_details = request.get_json()
    name = req_details.get("name")
    psd = req_details.get("password")
    admin_mail = req_details.get("admin_mail")
    img_path = req_details.get("img_path")
    if name and psd and admin_mail:
        if not is_valid_email(admin_mail):
            return json.dumps({"error": "The email is not valid"}), 400
        community.insert(name, psd, admin_mail, img_path)
    else:
        return json.dumps({"error": "All field- name, psd and admin_mail are mandatory"}), 400
    
    return json.dumps({"created": name}), 201


@app.route('/users/signup')
def get_user_signup_page():
    pass

@app.route('/users/login')
def get_user_login_page():
    pass

@app.route('/users', methods = ["POST"])
def add_user():
    email =  request.form.get("email")
    psd = request.form.get("password")
    name = request.form.get("name")
    community_id = request.form.get("community")
    community_psd = request.form.get("community_password")
    phone = request.form.get("phone")
    if email and psd and name and community_id and community_psd:
        if not is_valid_email(email):
            return json.dumps({"error": "The email is not valid"}), 400
        if not is_valid_phone(phone):
            return json.dumps({"error": "The phone number is not valid"}), 400
        if user.is_exist(email):
            return json.dumps({"error": "The user is aleady exist"}), 400
        if community.is_exist(community_id, community_psd):
            user.insert(email, psd, name, community_id, int(phone))
        else:
           return json.dumps({"error": "The community and psd not match"}), 400 
    else:
        return json.dumps({"error": "All field- name, psd and admin_mail are mandatory"}), 400
    

    response = make_response(redirect('/index.html'))
    response.set_cookie("user_email", email)
    return response

@app.route('/items/upload', methods=["POST"])
def get_add_item_page():
    name =  request.form.get("name")
    description = request.form.get("Description")
    img_url = request.form.get("img_url")
    email = request.cookies.get("user_email")
    item.insert(name, description,img_url, email)
    response = make_response(redirect('/index.html'))
    return response



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