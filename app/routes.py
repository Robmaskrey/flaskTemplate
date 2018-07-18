# need to import the app variable itself
from app import app
from flask import render_template #needed to render html files
# from app.calculations import Calc #this is calling the module we created "Calc" from the app folder. The app variable is looking in the app folder into calculations file to find the Calc module, I have since deleted this module, but i wanted to leave this comment here for reference


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')#very bare minimum, must return a rendered template of index.html, in render_template, we are sending the variable calc to index. This allows the index route to access the calc module, I have since deleted this module, but i wanted to leave this comment here for reference
