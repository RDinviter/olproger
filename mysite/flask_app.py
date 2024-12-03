from flask import Flask, render_template

app = Flask(__name__, '/static')


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about_olimp')
def about_olimp():
    return render_template("about_olimp.html")


@app.route('/programming_tech')
def programming_tech():
    return render_template("programming_tech.html")


@app.route('/algorithms_efficiency')
def algorithms_efficiency():
    return render_template("algorithms_efficiency.html")


@app.route('/containers')
def containers():
    return render_template("containers.html")


@app.route('/pref')
def pref():
    return render_template("pref.html")


@app.route('/two_pointers')
def two_pointers():
    return render_template("two_pointers.html")


@app.route('/binary_search')
def binary_search():
    return render_template("binary_search.html")


@app.route('/stl')
def stl():
    return render_template("STL.html")


@app.route('/recursion')
def recursion():
    return render_template("recursion.html")
