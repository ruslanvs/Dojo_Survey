from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route( "/" )
def front_page():
    return render_template( "index.html" )

@app.route( "/result", methods = ["post"])
def result():
    iname = request.form["fname"]
    location = request.form["location"]
    language = request.form["language"]
    comment = request.form["comment"]

    return render_template( "result.html", iname = iname, language = language, location = location, comment = comment )
    return redirect( "/" )

# @app.route( "/process", methods = ["post"])
# def process():
#     print "Data from form:"
#     print request.form
#     name = request.form["name"]
#     print name
#     return redirect( "/" )

app.run( debug = True )