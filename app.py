from flask import Flask, render_template, request, redirect, url_for
import database
from gan_model import generate_image
import random

app = Flask(__name__)
database.init_db()

@app.route('/')
def index():
    images = database.get_all_images()
    return render_template("index.html", images=images)

@app.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        filename = f"img_{random.randint(1000,9999)}.png"
        generate_image(filename)
        database.add_image(filename)
        return redirect(url_for('index'))
    return render_template("create.html")

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        filename = f"updated_{random.randint(1000,9999)}.png"
        generate_image(filename)
        database.update_image(id, filename)
        return redirect(url_for('index'))
    return render_template("update.html", id=id)

@app.route('/delete/<int:id>')
def delete(id):
    database.delete_image(id)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
