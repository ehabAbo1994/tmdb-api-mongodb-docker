from flask import Flask, request, render_template
from mongodb import mongodb


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # GET REQUEST
def load_insert_item_html():
    if request.method == 'POST':
        movie_name = request.form['name']
        #print(movie_name)
        mongo = mongodb()
        if request.form['submit_button'] == 'submit':
            mongo.insert_data(movie_name)
        elif request.form['submit_button'] == 'delete':
            mongo.del_data(movie_name)
        elif request.form['submit_button'] == 'read data':
            mongo.read_data()
    return render_template('form.html')

app.run()

