from traceback import print_exc
from typing import Union

from flask import Response, jsonify, request, render_template, redirect, url_for

from flask_assignment import app, db, Marks


@app.post("/marks")
def create_marks() -> Response:
    """
    Create a new Marks Object
    :return: Created Marks Object
    """
    try:
        marks = Marks.query.get(request.form["id"])
        if marks is None:
            marks = Marks(_id=request.form["id"])
            for subject in ["physics", "chemistry", "maths"]:
                if request.form[subject]:
                    setattr(marks, subject, int(request.form[subject]))
            db.session.add(marks)
        else:
            for subject in ["physics", "chemistry", "maths"]:
                if request.form[subject] and request.form[subject] != str(getattr(marks, subject)):
                    setattr(marks, subject, int(request.form[subject]))
        db.session.commit()
        return redirect(url_for("get_marks", id=request.form["id"]))
    except Exception as e:
        print_exc(e)
        return jsonify({"error": str(e)})


@app.get("/marks")
def get_marks() -> Union[str, Response]:
    """
    Get all marks for a student
    :return: Return HTML template displaying all marks of a student in a table
    """
    try:
        student_id = request.args.get("id")
        marks = Marks.query.get(student_id)
        return render_template("marks.html", marks=marks, id=student_id)
    except Exception as e:
        print_exc(e)
        return jsonify({"error": str(e)})
