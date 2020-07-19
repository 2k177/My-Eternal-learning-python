# import click
#
# @click.command()
# @click.option('--count', default=1, help='Number of greetings.')
# @click.option('--name', prompt='Your name',
#               help='The person to greet.')
# def hello(count, name):
#     """Simple program that greets NAME for a total of COUNT times."""
#     for x in range(count):
#         click.echo('Hello %s!' % name)
#
# if __name__ == '__main__':
#     hello()
# print_user_agent.py

import requests

SAMPLE_API_KEY = 'b1b15e88fa797225412429c1c50c122a1'

def current_weather(location, api_key=SAMPLE_API_KEY):
    url = 'http://samples.openweathermap.org/data/2.5/weather'
    print(url,"**",location)
    query_params = {
        'q': location,
        'appid': api_key,
    }

    response = requests.get(url, params=query_params)

    return response.json()['weather'][0]['description']

x = current_weather("London")
print(x)