import community, item, user from models 

var login_form = document.getElementById('login_form'),
    email = document.getElementById('email_login'),
    password = document.getElementById('password_login'),
    errorMessage = document.getElementById('errors_login');

function check_login(event) {
    
    event.preventDefault();
    
    if (email.value === '' || password.value === '') {
        errorMessage.innerText = 'Email and password are mandatory';
    } else {
        if ( ! user.check_if_user_exists_by_email_and_password(email.value, password.value) ) {
            errorMessage.innerText = 'Email and password are mandatory';
        }
        else{
        errorMessage.innerText = '';
        }
    }
}

login_form.addEventListener('submit__login', check_login);


// if name and psd and admin_mail:
// if not is_valid_email(admin_mail):
//     return json.dumps({"error": "The email is not valid"}), 400
// community.insert(name, psd, admin_mail, img_path)
// else:
// return json.dumps({"error": "All field- name, psd and admin_mail are mandatory"}), 400

// if not is_user:
// return json.dumps({"error": "Either password or email are incorrect."}), 400