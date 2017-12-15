from flask import Flask,redirect
app = Flask(__name__)

@app.route('/robots.txt')
def deny_request():
	return redirect('http://httpbin.org/deny')

if __name__=='__main__':
	app.run(port=8080, debug=True)
