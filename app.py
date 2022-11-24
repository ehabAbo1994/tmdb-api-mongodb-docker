from flask import Flask, request, render_template
from mongodb import mongodb


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # GET REQUEST
def load_insert_item_html():
    if request.method == 'POST':
        movie_name = request.form['name']
        #print(movie_name)
        x = mongodb()
        x.insert_data(movie_name)
    return render_template('form.html')

app.run()