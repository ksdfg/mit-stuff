from traceback import print_exc
from typing import Union

from flask import jsonify, Response, request

from flask_assignment import app, db
from flask_assignment.models import Student
from flask import render_template


@app.post("/students")
def create_student() -> Response:
    """
    Create a new Student Object
    :return: Created Student Object
    """
    try:
        student = Student(name=request.form["name"], email=request.form["email"])
        db.session.add(student)
        db.session.commit()
        return jsonify(student.to_dict())
    except Exception as e:
        print_exc(e)
        return jsonify({"error": str(e)})


@app.get("/students")
def get_all_students() -> Union[str, Response]:
    """
    Get all students
    :return: Return HTML template displaying all students in a table
    """
    try:
        return render_template("students.html", students=[student.to_dict() for student in Student.query.all()])
    except Exception as e:
        print_exc(e)
        return jsonify({"error": str(e)})
