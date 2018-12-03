from flask import Flask, render_template, redirect
from programpipeline import runPipeline

app = Flask(__name__)

@app.route('/')
def index():
	# return 'Hello World. Bring mich gleich um!'
	return render_template('index.html')

@app.route('/Programs')
def programs():
	return render_template('ProgramsDashboard.html')

@app.route('/RefreshPrograms')
def refreshPrograms():
	runPipeline()
	return redirect('/Programs')

if __name__ == '__main__':
	app.run(debug=True)
