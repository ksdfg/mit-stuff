from typing import Any

from flask_assignment import db


class Marks(db.Model):
    __tablename__ = "marks"

    _id = db.Column(db.Integer, db.ForeignKey("students._id"), primary_key=True)
    physics = db.Column(db.Integer)
    chemistry = db.Column(db.Integer)
    maths = db.Column(db.Integer)

    student = db.relationship("Student", back_populates="marks")

    def to_dict(self, exclude_relations: bool = False) -> dict[str, Any]:
        """
        Convert Model object to Dict
        :param exclude_relations: whether relation object dicts should be included or not
        :return: dict with model and relations data
        """
        obj = {"id": self._id, "physics": self.physics, "chemistry": self.chemistry, "maths": self.maths}
        if not exclude_relations and self.student:
            obj["student"] = self.student.to_dict(exclude_relations=True)
        return obj
