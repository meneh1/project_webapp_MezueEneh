from flask import Flask, render_template, request

from mbta import find_stop_near

app = Flask(__name__)



@app.route('/', methods=['GET', 'POST'])
def find():
    # modify this function so it renders different templates for POST and GET method.
    # aka. it displays the form when the method is 'GET'; it displays the results when
    # the method is 'POST' and the data is correctly processed.
    if request.method == 'POST':
        place  = request.form["name"]
        return find_stop_near(place)
    else:
        return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)