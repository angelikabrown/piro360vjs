from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cycle_day = db.Column(db.String(10), nullable=False)  # Add this field
    temperature = db.Column(db.Float, nullable=False)
    mood = db.Column(db.String(50), nullable=False)
    energy = db.Column(db.String(50), nullable=False)
    notes = db.Column(db.Text, nullable=True)
    date = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "cycle_day": self.cycle_day,
            "temperature": self.temperature,
            "mood": self.mood,
            "energy": self.energy,
            "notes": self.notes,
            "date": self.date,
            "timestamp": self.timestamp
        }