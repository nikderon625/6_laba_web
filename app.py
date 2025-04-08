from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route('/')
def index():
    instruments = ["Гитара", "Скрипка", "Флейта", "Саксофон", "Барабаны", "Пианино"]
    user_logged_in = False
    return render_template(
        "index.html",
        instruments=instruments,
        user_logged_in=user_logged_in
    )

@app.route('/about')
def about():
    shop_info = {
        "name": "Музыкальный мир",
        "description": "Лучшие музыкальные инструменты по доступным ценам.",
        "year": 2022
    }
    return render_template("about.html", shop=shop_info)

@app.route('/products')
def products():
    strings_path = os.path.join(app.static_folder, 'strings')
    winds_path = os.path.join(app.static_folder, 'winds')

    strings_images = os.listdir(strings_path) if os.path.exists(strings_path) else []
    winds_images = os.listdir(winds_path) if os.path.exists(winds_path) else []

    return render_template("products.html", strings=strings_images, winds=winds_images)

if __name__ == '__main__':
    app.run(debug=True)
