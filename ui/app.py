from flask import Flask 
from models import db, Data
from os import path
from routes import init_routes

#from . import create_app



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cyclesync.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'angie'  

  
    
   #initilaze the database with the app, connecting them
    db.init_app(app)

    #register the routes
    init_routes(app)

    #Create the database if it doesn't exist
    if not path.exists('cyclesync.db'):
        with app.app_context():
            db.create_all()
            print("Database created!")
            print(db)
            # existing_user = User.query.filter_by(username="joes").first()
            # if not existing_user:
            #     u2 = User(email="eat@joes", username="joes", password="password")
            #     db.session.add(u2)
            #     db.session.commit()
            # else:
            #     print("User with username 'joes' already exists.")
            #u5 = User(email="eat@jan", username="jan", password="passwurd")
            #cd1 = Data(cycle_day="CD1", temperature=98.6, mood="good", energy="low", notes="New cycle begins", date="2023-10-01", timestamp="2023-10-01 12:00:00")  
            cd2 = Data(cycle_day="CD2", temperature=98.7, mood="happy", energy="high", notes="Feeling great", date="2023-10-02", timestamp="2023-10-02 12:00:00")
            db.session.add(cd2)
            db.session.commit()




    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host='0.0.0.0', port=8080, debug=True)
