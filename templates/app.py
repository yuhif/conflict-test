from flask import Flask, render_template
app = Flask(__name__)
@app.route("/")
def top_page():
    return render_template("index.html")
from flask import Flask, render_template, request
@app.route("/circle_input")
def circle_input():
    return render_template("circle_input.html")
@app.route("/circle_result")
def circle_result():
    radius = int(request.args.get("radius"))
    result = 3.14 * radius ** 2s
    return render_template("circle_result.html", result=result)
if __name__ == "__main__":
    app.run(debug=True)