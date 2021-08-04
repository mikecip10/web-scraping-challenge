#import dependencies
from flask import Flask, render_template, redirect
from flask_pymongo import PyMongo
import scrape_mars

#initialize Flask
app = Flask(__name__)

#create a connection to a new Mongo database
mongo = PyMongo(app, uri="mongodb://localhost:27017/mars_app")

#define home route and function
@app.route("/")
def home():

    #pull data document from Mongo
    mission_data = mongo.db.collection.find_one()

    #return template and data
    return render_template("index.html", mars = mission_data)

#define route to scrape new data
@app.route("/scrape")
def scrape():

    #perform scrape
    mars_data = scrape_mars.scrape()

    #update the Mongo document to the new data values
    mongo.db.collection.update({}, mars_data, upsert=True)

    #redirect to home
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True)