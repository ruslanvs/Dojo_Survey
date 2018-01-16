from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "My_secret_session_key"

@app.route( "/" )
def front_page():
    return render_template( "index.html" )

@app.route( "/result", methods = ["POST"])
def result():
    iname = request.form["fname"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]
    error = False
    form = request.form


    if len(request.form['fname']) < 1:
        flash("Name cannot be blank!")
        error = True
    if len(request.form["comment"]) < 1:
        flash("Comment cannot be blank!")
        error = True
    if len(request.form["comment"]) > 120:
        flash("Comment exceeds 120 characters by " + str(len(request.form["comment"]) - 120) + " characters!" )
        error = True

    if error:
        return redirect( "/" ) #did not yet figure how to preserve the form data upon the error flash

    return render_template( "result.html", iname = iname, language = language, location = location, comment = comment )

app.run( debug = True )