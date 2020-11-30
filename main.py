#to run write this in cmd
#start chrome --allow-file-access-from-files

from flask import Flask, request, jsonify, render_template, redirect, url_for
import util


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("app.html")


@app.route('/classify_image', methods=['GET', 'POST'])
def classify_image():
    image_data = None
    image_data = request.form['image_data']

    response = jsonify(util.classify_image(image_data))

    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


if __name__ == "__main__":
    print("Starting Python Flask server for Face Image Classification")
    util.load_saved_artifacts()
    app.run()
