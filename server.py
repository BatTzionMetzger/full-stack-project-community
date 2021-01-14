from flask import Flask, Response, request,render_template, make_response, redirect
import json
import requests
from string_utils import is_valid_email, is_valid_phone
from models import community, item, user

import smtplib
from email.mime.text import MIMEText
import sys
# import chilkat

import imghdr
import os
from flask import Flask, render_template, request, redirect, url_for, abort, \
    send_from_directory
from werkzeug.utils import secure_filename


def validate_image(stream):
    header = stream.read(512)  # 512 bytes should be enough for a header check
    stream.seek(0)  # reset stream pointer
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')


app = Flask(__name__, static_url_path='', static_folder='static', template_folder='template')


app.config['MAX_CONTENT_LENGTH'] = 1024 * 1024
app.config['UPLOAD_EXTENSIONS'] = ['.jpg', '.png', '.gif']
app.config['UPLOAD_PATH'] = 'C://Users//sara leah//Desktop//Excellenteam//course//python//web community//static//images//uploads'


@app.route('/signup', methods = ['POST'])
def signup():
    print("insigup")
    email = request.form['email']
    print("The email address is '" + email + "'")
    return render_template("login.html")



@app.route('/<page>')
def get_main_page(page):
    user_email = request.cookies.get("user_email")
    owner_mail = request.cookies.get("owner_item")
    # user_email ="77@gmail.com"
    user_items_list = {}
    user_ownered_product = {}
    item_dict = {"name": request.cookies.get("name"), "description": request.cookies.get("description"),
             "email": request.cookies.get("owners_mail"), "img_path": request.cookies.get("img_path"),
             "phone": request.cookies.get("phone")}
    # if item_dict["name"]:
        # response = make_response(render_template(page, item_dict=item_dict))
        # if user_email:
        #     response.set_cookie("user_email", user_email)
        # return response
    if user_email:
        community_users_list=user.get_all_user_in_communitiy_of_user(user_email)
        if owner_mail:
            user_items_list=item.get_item_by_owber(owner_mail)
        else:
            user_items_list = user.get_item_by_email(user_email)
        user_ownered_product = user.get_user_ownered_products(user_email)
        user_owned_len = len(user_ownered_product)
        first_item_len = user_owned_len if user_owned_len <= 3 else 3
        second_item_len = user_owned_len - first_item_len if user_owned_len - first_item_len > 0 else 0
        response = make_response(render_template(page, user_items = user_items_list,
                                user_owner_products = user_ownered_product, first_len = first_item_len,
                                second_len = second_item_len,community_users =community_users_list , item_dict=item_dict))
        response.set_cookie("user_email", user_email)
        response.set_cookie("owner_item",'',expires=0)
        return response
    return render_template(page, user_items = user_items_list, login_error ="", sign_up_error = "")
 


@app.route('/items/look_at/<item_id>')
def look_at_item(item_id):
    user_email = request.cookies.get("user_email")
    item_dict = item.get_item_details(item_id)
    if user_email:
        # item.buy(item_id, user_email)
        response = make_response(redirect("/item.html"))
        for key, value in item_dict.items():
            response.set_cookie(key, str(value))
        response.set_cookie("user_email", user_email)
        return response
    else:
        return json.dumps({"error": "Please log in or sign up"}), 400


@app.route('/index/<mail_item_of>', methods=['POST'])
def get_main_page_with_items_of_user(mail_item_of):
    response = make_response(redirect("/index.html"))
    response.set_cookie("owner_item", mail_item_of)
    return response


@app.route('/communities/signup')
def get_comm_signup_page():
    user_email = request.cookies.get("user_email")
    if user_email:
        response = make_response(redirect("/addcommunity.html"))
        response.set_cookie("user_email", user_email)
        return response
    return redirect('/addcommunity.html') 

@app.route('/communities', methods = ["POST"])
def add_community():
    user_email = request.cookies.get("user_email")

    name =  request.form.get("name")
    psd =  request.form.get("password")
    admin_mail =  request.form.get("admin_email")
    img_path =  request.form.get("img_path")
    if name and psd and admin_mail:
        if not is_valid_email(admin_mail):
            return render_template("/addcommunity.html", add_comm_error =  "\nThe email is not valid")
        community.insert(name, psd, admin_mail, img_path)
    else:
        return render_template("/addcommunity.html", add_comm_error =  "\nAll field- name, password and admin email are mandatories")
    
    if user_email:
        response = make_response(render_template("index.html"))
        response.set_cookie("user_email", user_email)
        return response
    return render_template("index.html")


@app.route('/users/signup')
def get_user_signup_page():
    pass

@app.route('/users/login')
def get_user_login_page():
    pass

@app.route('/login')
def login():
    email = request.args.get('email')
    password = request.args.get('password')
    if not email or not password:
        return render_template("/login.html", login_error =  "\nEither password or email are incorrect.", sign_up_error = "" )
    is_user = user.check_if_user_exists_by_email_and_password(email, password)
    if not is_user:
        return render_template("/login.html", login_error =  "\nPassword and Email are not match", sign_up_error = "")
    response = make_response(redirect("/index.html"))
    response.set_cookie("user_email", email)
    return response

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
            return render_template("/login.html", login_error =  "", sign_up_error = "\nThe email is not valid")
        if not is_valid_phone(phone):
            return render_template("/login.html", login_error =  "", sign_up_error = "\nThe phone is not valid")
        if user.is_exist(email):
            return render_template("/login.html", login_error =  "", sign_up_error = "\nThe user is aleady exist")
        if community.is_exist(community_id, community_psd):
            user.insert(email, psd, name, community_id, int(phone))
        else:
            return render_template("/login.html", login_error =  "", sign_up_error = "\nThe community and psd not match")
    else:
        return render_template("/login.html", login_error =  "", sign_up_error = "\nAll field- name, psd and admin_mail are mandatory")
    

    response = make_response(redirect('/index.html'))
    response.set_cookie("user_email", email)
    return response

@app.route('/items/upload', methods=["POST"])
def get_add_item_page():
    pass


@app.route('/items')#query_str => item_id, uploaded_items, myorder
def get_items_by_query_page():
    pass

@app.route('/items', methods = ["POST"])
def add_item():
    print("hiii1")
    name =  request.form.get("name")
    description = request.form.get("Description")
    img_url = request.form.get("img_url")
    email = request.cookies.get("user_email")
    if not name or not description:
        return render_template("/add_product.html", add_item_error = "The name and description are required")

    item.insert(name, description,img_url, email)
    #item.insert(name, description,img_url, email)

    
    uploaded_file = request.files['file']
    #filename = secure_filename(uploaded_file.filename)
    img_name= str(item.get_size_item()+1)+".jpg"
    # if filename != '':
    #     file_ext = os.path.splitext(filename)[1]
    #     if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
    #             file_ext != validate_image(uploaded_file.stream):
    #         abort(400)
    #    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'],str(item.get_size_item()+1)+".jpg"))

    #img_url = os.path.join(app.config['UPLOAD_PATH'])

    #print("img_url",img_url,len(img_url))

    uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], img_name))

    
    item.insert(name, description,img_name, email)

    response = make_response(redirect('/index.html'))
    response.set_cookie("user_email", email)
    return response

@app.route('/items/buy/<item_id>', methods = ["POST"])
def buy_item(item_id):
    user_email = request.cookies.get("user_email")

    if user_email:
        item.buy(item_id, user_email)
        response = make_response(redirect("/index.html"))
        response.set_cookie("user_email", user_email)
        return response
    else:
        return json.dumps({"error": "Please log in or sign up"}), 400

@app.route('/communities')
def get_community_details_page():
    pass


@app.route('/logout')
def logout():
    response = make_response(redirect("/index.html"))
    response.set_cookie("user_email", "", expires=0)
    return response

@app.route('/send_email', methods = ["POST"])
def send_email():
    name = request.form.get('name')
    email = 'slmj5885@gmail.com'
    subject = request.form.get('subject')
    message = request.form.get('message')
    user_email = request.cookies.get("user_email")

    to_send = user.get_owner_email(user_email)

    msg = MIMEText(message)
    # msg = message
    host = "server.smtp.com"
    server = smtplib.SMTP('64.233.184.108')
    MSG = "Subject: {}\n\n{}".format(subject, message)
    server.ehlo()
    server.starttls()
    server.login('slmj5885@gmail.com', '207352816')
    server.sendmail(email, to_send, MSG)

    server.quit()
    # mailman = chilkat.CkMailMan()
    # mailman.put_SmtpHost("localhost")
    # mailman.put_SmtpAuthMethod("NONE")
    # email = chilkat.CkEmail()
    # email.put_Subject("This is a test")
    # email.put_Body("This is a test")
    # email.put_From("Chilkat Support <support@chilkatsoft.com>")
    # success = email.AddTo("Chilkat Admin","admin@chilkatsoft.com")
    # if (success != True):
    #     print(mailman.lastErrorText())
    #     sys.exit()
    
    # success = mailman.CloseSmtpConnection()
    # if (success != True):
    #     print("Connection to SMTP server not closed cleanly.")

    response = make_response(redirect("/index.html"))
    response.set_cookie("user_email", email)
    return response

if __name__ == '__main__':
    app.run(port=3000)