from flask_app import app
from flask_app.models.model_dojos import Dojo
from flask import render_template, request, redirect

@app.route('/dojos')
def showDojo():
    return render_template("dojos.html", dojos=Dojo.get_all())

@app.route('/dojos/create', methods=['POST'])
def dojoCreate():
    Dojo.save(request.form)
    return redirect ('/dojos')

@app.route('/dojos/<int:id>')
def showSingleDojo(id):
    return render_template("dojo_show.html", dojo=Dojo.get_dojo_with_students({"id": id}))