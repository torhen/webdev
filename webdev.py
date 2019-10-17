from flask import Flask, request, render_template
import pathlib, shutil, datetime

app = Flask(__name__, static_folder='',static_url_path='')

@app.route('/')
def root():
	"""provide just the main frame"""
	# create default app if nothing existst
	if not pathlib.Path('app.html').exists():
		shutil.copy('templates/default_app.html','app.html')

	return render_template('index.html')
	
@app.route('/left')	
def left():
	with open('app.html') as fin:
		text = fin.read()
	return render_template('left.html', text=text)

@app.route('/right')	
def right():
	return app.send_static_file('app.html')	

@app.route('/change',methods=['GET','POST'])
def change():
	""" update file using data from POST """
	s = str(datetime.datetime.now())
	txt = request.form['txt']

	with open('app.html', 'w') as fout:
		fout.write(txt)
	return "file updated"
	

app.run(debug=True)