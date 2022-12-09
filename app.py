from base64 import b64encode
from flask import Flask, request, render_template
from mongodb import mongodb

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])  # GET REQUEST
def load_insert_item_html():
    mongo = mongodb('mongodb', 27017)
    if request.method == 'POST':
        movie_name = request.form['name']
        #print(movie_name)
        binary_file = mongo.read_data(movie_name)
        if request.form['submit_button'] == 'submit':
            if mongo.insert_data(movie_name):
                image = b64encode(binary_file).decode("utf-8")
                src = "data:image/gif;base64," + image
                return f'<img src={src}>'
            else:
                return "poster added, please return and type the name again to show the poster"

        elif request.form['submit_button'] == 'delete':
            mongo.del_data(movie_name)
            return "movie deleted"
        elif request.form['submit_button'] == 'read data':
            read = mongo.read_all_posters()
            return read
    return render_template('form.html')


if __name__ == "__main__":

    app.run(debug=False, host='0.0.0.0', port=5001)

