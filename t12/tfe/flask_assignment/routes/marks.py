from traceback import print_exc

from flask import Response, jsonify, request

from flask_assignment import app, db, Marks


@app.post("/marks")
def create_marks() -> Response:
    """
    Create a new Marks Object
    :return: Created Marks Object
    """
    try:
        marks = Marks(
            _id=request.form["id"],
            physics=int(request.form["physics"]),
            chemistry=int(request.form["chemistry"]),
            maths=int(request.form["maths"]),
        )
        db.session.add(marks)
        db.session.commit()
        return jsonify(marks.to_dict())
    except Exception as e:
        print_exc(e)
        return jsonify({"error": str(e)})
