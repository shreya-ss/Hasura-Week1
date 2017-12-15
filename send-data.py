from flask import Flask,render_template, request
app = Flask(__name__)

@app.route('/input')
def input():
	return render_template('input.html')

@app.route('/welcome', methods=['POST'])
def welcome():
	if request.method == 'POST':
		result = request.form
		name=result.get('nm')
		print(name)
	return render_template("welcome.html",result = result)

if __name__ == '__main__':
   app.run(port=8080,debug = True)
