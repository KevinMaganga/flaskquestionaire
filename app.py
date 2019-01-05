from flask import Flask , render_template, session, redirect, url_for, flash
#from flask_wtf import Form
#from wtforms import StringField
#from wtforms.validators import DataRequired
from flask import current_app
from flask_sqlalchemy import SQLAlchemy
import os

#string =os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
#db = SQLAlchemy(app)



@app.route('/')

def index():
    #string =os.path.dirname(os.path.abspath(__file__))
    #return string
    #return render_template('pics2.html')
    return "<h3> post your question </h3>"

	
@app.route('/contacts')
def contacts():
    return "<h3> Contacts </h3>"


@app.route('/post', methods = ['GET','POST'])
def post():
    if request.method== 'GET':
        return "<h3> get your question </h3>"
    elif request.method== 'POST':
        return "<h3> post your question </h3>"

    

@app.route('/question/<id>')

def question(id):
    var= str(id)
    
    return var



@app.route('/api/v1/GET/<auth>/<qid>/')

def api_get_question(auth,qid):
    
    return str(auth)+str(qid)



@app.route('/api/v1/GET/<auth>/all/')

def api_get_all_questions(auth):

    return str(auth)+" All questions"



@app.route('/api/v1/POST/<question>/')

def api_post_question(question):

    return question
	

