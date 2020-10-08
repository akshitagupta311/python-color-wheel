from flask import Flask, render_template, Blueprint
app = Flask(__name__)

# @app.route('/', methods=['POST', 'GET'])
# def hello():
#    if request.method == "GET":
#        return render_template('form.html')
#    else:
#        return render_template(
#            'output.html',
#            msg=request.form.get('msg'),
#            times=request.form.get('times')

@app.route('/')
def home():
   return render_template("Home.html")
 
# admin = Blueprint("admin",__name__)
 
@app.route('/calculate-color', methods=['POST'])
def calculate():

    msg=request.form.get('msg')
    print(msg)

# @admin.route('/')
# def admin_home():
#    return render_template("admin_home.html")
 
# @admin.route('/settings')
# def admin_settings():
#    return render_template("admin_settings.html")
 
# user = Blueprint("user",__name__)
 
# @user.route('/')
# def user_home():
#    return render_template("user_home.html")
 
# @user.route('/settings')
# def user_settings():
#    return render_template("user_settings.html")
 

# app.register_blueprint(admin, url_prefix="/admin")
# app.register_blueprint(user, url_prefix="/user")
 
app.run(debug=True)