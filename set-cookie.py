from flask import Flask,make_response
app = Flask(__name__)

@app.route('/setcookie')
def set_cookie():
	resp=make_response("Cookies are set!")
	resp.set_cookie("name","Shreya")
	resp.set_cookie("age","20")
	return resp

if __name__=='__main__':
	app.run(port=8080,debug=True)
