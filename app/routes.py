from app import app, db
from flask import render_template, url_for, flash, redirect, request
from app.forms import FormativeSummativeScaleForm, FormativeSummativeAssignmentsForm
from app.models import UserAssignments, Assignment

fw = 0
sw = 0
total_num_of_assignments = 0

@app.route("/", methods=["GET", "POST"])
@app.route("/home", methods=["GET", "POST"])
def home():
    scale_form = FormativeSummativeScaleForm()
    if request.method == "POST":
        if scale_form.validate_on_submit():
            try:
                fw = int(scale_form.formative_weight.data)
                sw = int(scale_form.summative_weight.data)
                total_num_of_assignments = int(scale_form.total_number_of_assignments.data)
            except:
                flash("Please input a valid number for all inputs. Do not include a percent sign ('%'), or any other symbols.", "warning")
                return redirect(url_for("home"))
            if fw + sw != 100:
                flash("Please make sure both categories' weight, formative and summative, add up to 100 for the most accurate results. Try again.", "warning")
                return redirect(url_for("home"))
            if total_num_of_assignments > 20:
                flash("Please make sure the total number of assignments does not exceed 20. Try again.", "warning")
                return redirect(url_for("home"))

            new_user_intro_info = UserAssignments(num_of_assignments=total_num_of_assignments, formative_weight=fw, summative_weight=sw, assignments=[])
            db.session.add(new_user_intro_info)
            db.session.commit()

            return redirect(url_for("assignments"))

    elif request.method == "GET":

        return render_template("home.html", title="Home", form=scale_form)

@app.route("/formative_assignments", methods=["GET", "POST"])
def assignments():
    form = FormativeSummativeAssignmentsForm()
    current_user_assignments = UserAssignments.query.filter_by(id=1).first()
    
    if current_user_assignments == None:
        flash("You must provide the introductory credentials first. Please try again.", "warning")
        return redirect(url_for("home"))

    number_of_assignments = current_user_assignments.num_of_assignments

    if request.method == "POST":
        
        pass
    

    return render_template("assignments.html", title="Assignments", form=form, number_of_assignments=number_of_assignments)

