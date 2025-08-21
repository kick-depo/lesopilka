from flask import Flask, render_template, url_for, request

app = Flask(__name__)



@app.route("/", methods=["GET", "POST"])
def about():
    if request.method == "POST":
        print(request.form)
    return render_template("index.html")




if __name__ == "__main__":
    app.run(debug=True)