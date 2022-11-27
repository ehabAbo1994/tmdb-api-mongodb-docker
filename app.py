import os
from flask import Flask, request, render_template
from mongodb import mongodb

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # GET REQUEST
def load_insert_item_html():
    if request.method == 'POST':
        movie_name = request.form['name']
        #print(movie_name)
        mongo = mongodb('localhost', 27017)
        #mongo = mongodb('mongo', 27017)
        if request.form['submit_button'] == 'submit':
            mongo.insert_data(movie_name)
            return "poster submited"
        elif request.form['submit_button'] == 'delete':
            mongo.del_data(movie_name)
            return "movie deleted"
        elif request.form['submit_button'] == 'read data':
            read = mongo.read_data()
            return read
    return render_template('form.html')


if __name__ == "__main__":

    app.run(debug=False, host='0.0.0.0', port=5001)

