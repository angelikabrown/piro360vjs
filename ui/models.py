from flask_sqlalchemy import SQLAlchemy

#initialize the database extention
db = SQLAlchemy()

class Data(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cycle_day = db.Column(db.String(10)) 
    temperature = db.Column(db.Float)
    mood = db.Column(db.String(50))
    energy = db.Column(db.String(50))
    notes = db.Column(db.String(200))
    date = db.Column(db.String(50))
    timestamp = db.Column(db.String(50))
    # Define the relationship with the User model
    #user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
   

    def __repr__(self):
        return f'<Data {self.cycle_day}>'
    
    def to_dict(self):
        return {
            'id': self.id,
            'cycle_day': self.cycle_day,
            'temperature': self.temperature,
            'mood': self.mood,
            'energy': self.energy,
            'notes': self.notes,
            'date': self.date,
            'timestamp': self.timestamp}