# Import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

# Flask
app = Flask(__name__)

# Mongo database
client = PyMongo.MongoClient('mongodb://localhost:27017/')
mydb = client['mars_db']
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_db")

# Route
@app.route("/")
def home():

    mars_mission_data = mongo.db.collection.find_one()

    return render_template("index.html", data = mars_mission_data)

#define route to scrape new data
@app.route("/scrape")
def scrape():

    mars_data=scrape_mars.nasa_scrape()
    mars_data=scrape_mars.image_scrape()
    mars_data=scrape_mars.fact_scrape()
    mars_data=scrape_mars.hem_scrape()
    mongo.db.collection.update({}, mars_data, upsert=True)

    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)