from flask import Flask, request, render_template
import pathlib, shutil, datetime, time

app = Flask(__name__, static_folder='',static_url_path='')

@app.route('/')
def root():
	"""provide just the main frame"""
	# create default app if nothing existst
	if not pathlib.Path('app.html').exists():
		shutil.copy('templates/default_app.html','app.html')
	if not pathlib.Path('app.js').exists():
		shutil.copy('templates/default_app.js','app.js')
	t = time.time()
	return render_template('index.html', t=t)
	
@app.route('/left')	
def left():
	with open('app.html') as fin:
		txt_html = fin.read()
	with open('app.js') as fin:
		txt_js = fin.read()
	return render_template('left.html', txt_html=txt_html, txt_js=txt_js)

@app.route('/right')	
def right():
	return app.send_static_file('app.html')	

@app.route('/change',methods=['GET','POST'])
def change():
	""" update file using data from POST """
	s = str(datetime.datetime.now())
	txt_html = request.form['txt_html']
	txt_js = request.form['txt_js']

	with open('app.html', 'w') as fout:
		fout.write(txt_html)
		
	with open('app.js', 'w') as fout:
		fout.write(txt_js)
		
	return "file updated"
	

app.run(debug=True)