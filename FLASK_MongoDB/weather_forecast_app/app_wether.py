import requests
from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
app.config['DEBUG'] = True

#To establish a connection
client = MongoClient('mongodb://localhost:27017')
#Accessing Databases

@app.route('/', methods=['GET', 'POST'])
def index():
    db = client['weather']
    posts = db.posts
    if request.method == 'POST':
        new_city = request.form.get('city')
        if new_city:
            print(new_city)
            post_data = {
                'name': new_city
            }
            result = posts.insert_one(post_data)
            print('One post: {0}'.format(result.inserted_id))

    cities = posts.find({})
    citiess = []
    for document in cities:
        print("document:", document.get('name'))
        citiess.append(document.get('name'))

    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=271d1234d3f497eed5b1d80a07b3fcd1'

    weather_data = []

    for city in citiess:

        r = requests.get(url.format(city)).json()

        weather = {
            'city' : city,
            'temperature' : r['main']['temp'],
            'description' : r['weather'][0]['description'],
            'icon' : r['weather'][0]['icon'],
        }

        weather_data.append(weather)


    return render_template('weather.html', weather_data=weather_data)
if __name__ == '__main__':
    app.run()