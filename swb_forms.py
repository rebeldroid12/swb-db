import sqlite3
from bottle import request, route, run, template, static_file, debug

@route('/evaluation_form', method='GET')
def eval_form():

	if request.GET.get('submit-data','').strip():
		project_name = request.GET.get('project','').strip()
		evaluator_first_name = request.GET.get('e1first','').strip()
		evaluator_last_name = request.GET.get('e1last','').strip()
		evaluator_role = request.GET.get('e1role','').strip()
		evaluee_first_name = request.GET.get('e2first','').strip()
		evaluee_last_name = request.GET.get('e2last','').strip()
		evaluee_role = request.GET.get('e2role','').strip()
		comment = request.GET.get('comment','').strip()
		rating = request.GET.get('rate','').strip()

		conn = sqlite3.connect('swb.db')

		conn.execute('''CREATE TABLE IF NOT EXISTS eval (
			id  INTEGER PRIMARY KEY AUTOINCREMENT,
			project_name  TEXT,
			evaluator_first_name  TEXT,
			evaluator_last_name TEXT,
			evaluator_role  TEXT,
			evaluee_first_name  TEXT,
			evaluee_last_name TEXT,
			evaluee_role  TEXT,
			comments  TEXT,
			rating  TEXT
			)''')
		conn.commit()

		c = conn.cursor()

		c.execute("INSERT INTO eval (project_name,evaluator_first_name, evaluator_last_name, evaluator_role, evaluee_first_name, evaluee_last_name, evaluee_role, comments, rating) VALUES (?,?,?,?,?,?,?,?, ?)", (project_name, evaluator_first_name, evaluator_last_name, evaluator_role, evaluee_first_name, evaluee_last_name, evaluee_role, comment, rating))
		conn.commit()
		c.close()

		return template('views/thankyou')

	else:
		return template('views/eval_form')

@route('/volunteer_form')
def volunteer_form():
    return template('views/volunteer_form')

@route('/project_form')
def project_form():
    return template('views/project_form')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/rebeldroid12/swb-db/static/')

debug(True)
run(host='localhost', port=8080, debug=True)

