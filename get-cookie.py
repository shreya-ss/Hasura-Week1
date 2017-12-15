from flask import Flask,request
app = Flask(__name__)

@app.route("/getcookies")
def get_cookies():
	name=request.cookies.get('name')
	age=request.cookies.get('age')
	return name+" "+age

if __name__=='__main__':
	app.run(port=8080,debug=True)
