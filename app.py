from flask import Flask, render_template, request
import requests
import random
import mysql.connector


app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_HOST'] = '10.0.2.82'
app.config['MYSQL_USER'] = 'pyapp'
app.config['MYSQL_PASSWORD'] = '123_abcde'
app.config['MYSQL_DATABASE'] = 'responses'

# Create MySQL connection
mysql = mysql.connector.connect(
    host=app.config['MYSQL_HOST'],
    user=app.config['MYSQL_USER'],
    password=app.config['MYSQL_PASSWORD'],
    database=app.config['MYSQL_DATABASE']
)



# Sample list of URLs
sample_urls = [
    "https://mcdonalds.com.pk/",
    "https://mcdonalds.com.pk/full-menu/breakfast/",
    "https://mcdonalds.com.pk/full-menu/chicken-and-fish/",
    "https://mcdonalds.com.pk/full-menu/crispy-chicken/",
    "https://123.com",
    "https://1432.com",
    "https://noway.com"
]

@app.route('/')
def hello():
    # Choose a random URL from the list
    random_url = random.choice(sample_urls)

    try:
        # Make an HTTP GET request to the randomly chosen URL
        response = requests.get(random_url)
        response_text = f"URL: {random_url}\nResponse Code: {response.status_code}"
        cursor = mysql.cursor()
        cursor.execute("INSERT INTO url_responses (url, status_code) VALUES (%s, %s)", (random_url, response.status_code))
        mysql.commit()
        cursor.execute("SELECT * FROM url_responses")
        results = cursor.fetchall()
        cursor.close()

    except Exception as e:
        # Handle any exceptions (e.g., connection errors)
        response_text = f"Error: {str(e)}"
        cursor = mysql.cursor()
        cursor.execute("SELECT * FROM url_responses")
        results = cursor.fetchall()
        cursor.close()

    # Render the response in an HTML template
    server_ip = request.host.split(':')[0]
    return render_template('./response.html', response_text=response_text,results=results, server_ip=server_ip)

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=80,debug=True)

