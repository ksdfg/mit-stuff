from typing import Any

from flask_assignment import db


class Student(db.Model):
    __tablename__ = "students"

    _id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(50))

    marks = db.relationship("Marks", back_populates="student", uselist=False)

    def to_dict(self, exclude_relations: bool = False) -> dict[str, Any]:
        """
        Convert Model object to Dict
        :param exclude_relations: whether relation object dicts should be included or not
        :return: dict with model and relations data
        """
        obj = {"id": self._id, "name": self.name, "email": self.email}
        if not exclude_relations and self.marks:
            obj["marks"] = self.marks.to_dict(exclude_relations=True)
        return obj
