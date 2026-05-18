from flask import Flask, render_template, request, redirect, flash, url_for
import mycode
import os

app = Flask(__name__)
app.secret_key="faith123"

@app.route("/")
def home():
    return render_template("home.html")
@app.route("/2", methods=["GET","POST"])
def two_by_2():
    if request.method=="GET":
        return render_template('twobytwo.html', title="2x2 Eqation")
    else:
        try:
            x1=int(request.form.get('x1'))
            y1=int(request.form.get('y1'))
            t1=int(request.form.get('t1'))
            x2=int(request.form.get('x2'))
            y2=int(request.form.get('y2'))
            t2=int(request.form.get('t2'))
            result=mycode.solve_2x2(x1, y1, t1, x2, y2, t2)
            return render_template('twobytwo.html', title="2x2 Eqation", result=result, x1=x1, y1=y1, t1=t1, x2=x2, y2=y2, t2=t2)
        except ZeroDivisionError:
            flash("Invalid input")
            return redirect(url_for('two_by_2'))
@app.route("/3", methods=["GET","POST"])
def three_by_3():
    if request.method=="GET":
        return render_template('threeby3.html', title="3x3 Eqation")
    else:
        try:
            x1=int(request.form.get('x1'))
            y1=int(request.form.get('y1'))
            z1=int(request.form.get('z1'))
            t1=int(request.form.get('t1'))
            x2=int(request.form.get('x2'))
            y2=int(request.form.get('y2'))
            z2=int(request.form.get('z2'))
            t2=int(request.form.get('t2'))
            x3=int(request.form.get('x3'))
            y3=int(request.form.get('y3'))
            z3=int(request.form.get('z3'))
            t3=int(request.form.get('t3'))
            result=mycode.solve_3x3(x1, y1, z1, t1, x2, y2, z2, t2, x3, y3, z3, t3)
            return render_template('threeby3.html', title="3x3 Equation", result=result, x1=x1, y1=y1, z1=z1, t1=t1, x2=x2, y2=y2, z2=z2, t2=t2, x3=x3, y3=y3, t3=t3)
        except ZeroDivisionError:
            flash("Invalid input")
            return redirect(url_for('three_by_3'))

if __name__=="__main__":
    app.run(debug=True)