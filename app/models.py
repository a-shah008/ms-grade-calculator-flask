from app import app, db

class UserAssignments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    num_of_assignments = db.Column(db.Integer)
    formative_weight = db.Column(db.Integer)
    summative_weight = db.Column(db.Integer)
    assignments = db.relationship("Assignment", backref="all_assignments")

    def __repr__(self):
        return f"User {self.id} Assignments: {self.assignments}"

class Assignment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    assignment_weight = db.Column(db.String(100))
    assignment_user_points = db.Column(db.Integer)
    assignment_max_points = db.Column(db.Integer)
    user_assignments_id = db.Column(db.Integer, db.ForeignKey("user_assignments.id"))

    def __repr__(self):
        return f"Assignment {self.id}: {self.assignment_name}"