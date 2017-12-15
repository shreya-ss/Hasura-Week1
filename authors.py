from flask import Flask, render_template
app = Flask(__name__)
import requests
import json

@app.route('/authors')
def authors():
	url1 = 'https://jsonplaceholder.typicode.com/users'
	url2 = 'https://jsonplaceholder.typicode.com/posts'
	r1 = requests.get(url1)
	r2 = requests.get(url2)
	data1 = r1.json()
	data2 = r2.json()
	return render_template('authors.html', data1=data1, data2=data2)

if __name__ == '__main__':
	app.run(port=8080,debug=True)
