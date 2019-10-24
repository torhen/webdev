from flask import Flask, request, render_template
import pathlib, shutil, datetime, time

app = Flask(__name__, static_folder='',static_url_path='')

@app.route('/')
def test():
	l = list(pathlib.Path('apps').glob('*'))
	l = [str(p.stem) for p in l]
	s = '<html><h2>Apps</h2>\n'
	for stem in l:
		s = s + f"<a href='/{stem}'>{stem}</a><br>"
	s = s + '<html>\n'
	return s

@app.route('/<appname>')
def root(appname):
	"""provide just the main frame"""

		
	return render_template('index.html', appname=appname)
	
@app.route('/left/<appname>')	
def left(appname):
	with open(f'apps/{appname}/{appname}.html') as fin:
		txt_html = fin.read()
	with open(f'apps/{appname}/{appname}.js') as fin:
		txt_js = fin.read()
	return render_template('left.html', appname=appname)

@app.route('/right/<appname>')	
def right(appname):
	return app.send_static_file(f'apps/{appname}/{appname}.html')	

@app.route('/change',methods=['GET','POST'])
def change():
	""" update file using data from POST """
	file = request.form['file']
	text = request.form['text']
	
	with open(file, 'w') as fout:
		fout.write(text)
	print(f'updated: {file}')
	return "file updated"

	

app.run(debug=True)