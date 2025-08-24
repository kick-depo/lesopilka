from flask import Flask, render_template, request, flash, url_for

app = Flask(__name__)
app.config['SECRET_KEY'] = 'NaVi'



@app.route("/", methods=["GET", "POST"])
def about():
    
    if request.method == "POST":
        print(request.form)
        if len(request.form['phone']) > 2:
         flash(f"Телефон отправлен {request.form['phone']}", category='success')
        else:
            flash("Ошибка отправки", category='error')
    return render_template("index.html")

@app.route("/auth", methods=["GET", "POST"])
def auth():
   return render_template("auth.html")

@app.errorhandler(404)
def pageNotFound(error):
   return "<h1>Опа, а тут у нас ощибочька 404 :c </h1><br><h3>Вернуться на <a href='/'>главную</<a>", 404


if __name__ == "__main__":
    app.run(debug=True)