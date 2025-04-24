from flask import Flask 
from models import db, Data
from os import path
from routes import init_routes
from flask_cors import CORS

#from . import create_app



def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cyclesync.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'angie'  

    #Enable CORS for all routes
    CORS(app, resources={r"/*": {"origins": "*"}})
    
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
            cd1 = Data(cycle_day="CD1", temperature=98.6, mood="good", energy="low", notes="New cycle begins", date="2023-10-01", timestamp="2023-10-01 12:00:00")
            cd2 = Data(cycle_day="CD2", temperature=98.7, mood="good", energy="low", notes="Didn't sleep well last night", date="2023-10-02", timestamp="2023-10-02 12:00:00")
            cd3 = Data(cycle_day="CD3", temperature=98.8, mood="good", energy="med", notes="walked for 2 miles today", date="2023-10-03", timestamp="2023-10-03 12:00:00")
            cd4 = Data(cycle_day="CD4", temperature=98.9, mood="good", energy="med", notes="Feeling great!", date="2023-10-04", timestamp="2023-10-04 12:00:00")
            cd5 = Data(cycle_day="CD5", temperature=97.6, mood="good", energy="low", notes="Feeling great!", date="2023-10-05", timestamp="2023-10-05 12:00:00")
            db.session.add(cd2)
            db.session.commit()




    return app



# app.config['SITE_NAME'] = 'CycleSync'
# app.config['FLASK_DEBUG'] = 1


# with app.app_context():
#     db.create_all()
  
#     print("start")
#     print(db)

#      # Check if the username already exists
#     # existing_user = User.query.filter_by(username="joes").first()
#     # if not existing_user:
#     #     u2 = User(email="eat@joes", username="joes", password="password")
#     #     db.session.add(u2)
#     #     db.session.commit()
#     # else:
#     #     print("User with username 'joes' already exists.")
#     u4 = User(email="eat@bubba", username="bubba", password="password123")
#     db.session.add(u4)
#     db.session.commit()


if __name__ == "__main__":
    app = create_app()
    app.run(port=8080, debug=True)
