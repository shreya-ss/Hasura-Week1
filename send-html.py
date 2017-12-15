from flask import Flask,render_template
app = Flask(__name__)

@app.route('/html')
def send_html():
	return render_template("home.html")

if __name__=='__main__':
	app.run(port=8080,debug=True)