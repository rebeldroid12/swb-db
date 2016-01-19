import sqlite3
import os
from bottle import request, route, run, template, static_file, debug, default_app

#evaluation form
@route('/', method='GET')
def index():
	return template('index')

@route('/db-projects')
def results():
	full_path = os.path.dirname(os.path.abspath(__file__))
	conn = sqlite3.connect(os.path.join(full_path, 'swb.db'))
	c = conn.cursor()
	c.execute("SELECT * FROM projects")
	projects = c.fetchall()
	c.close
	return template('results', project_data = projects)

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

		full_path = os.path.dirname(os.path.abspath(__file__))
		conn = sqlite3.connect(os.path.join(full_path, 'swb.db'))

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

		return template('thankyou')

	else:
		return template('eval_form')


#volunteer sign up form
@route('/volunteer_form')
def volunteer_form():

	if request.GET.get('submit-data','').strip():
		email = request.GET.get('email','').strip()
		first_name = request.GET.get('firstname','').strip()
		last_name = request.GET.get('lastname','').strip()
		work_position = request.GET.get('position','').strip()
		employer = request.GET.get('employer','').strip()
		country = request.GET.get('country','').strip()
		state = request.GET.get('state-USA','').strip()
		expertise = request.GET.get('expertise','').strip()
		language = request.GET.get('languages','').strip()
		experience = request.GET.get('experience','').strip()


		full_path = os.path.dirname(os.path.abspath(__file__))
		conn = sqlite3.connect(os.path.join(full_path, 'swb.db'))
		conn.execute('''CREATE TABLE IF NOT EXISTS volunteer (
		id integer PRIMARY KEY AUTOINCREMENT
		, email text
		, first_name text
		, last_name text
		, current_position text
		, current_employer text
		, country text
		, state text
		, expertise text
		, language text
		, experience text
		)
		''')
		c = conn.cursor()

		c.execute("INSERT INTO volunteer (email, first_name, last_name, current_position, current_employer, country, state, expertise, language, experience) VALUES (?,?,?,?,?,?,?,?,?,?)", (email, first_name, last_name, work_position, employer, country, state, expertise, language, experience))
		conn.commit()
		c.close()

		return template('thankyou')

	else:

		return template('volunteer_form')




#project form
@route('/project_form')
def project_form():

	if request.GET.get('submit-data','').strip():
		company = request.GET.get('company','').strip()
		first_name = request.GET.get('firstname','').strip()
		last_name = request.GET.get('lastname','').strip()
		project_name = request.GET.get('project','').strip()
		summary = request.GET.get('summary','').strip()
		skills = request.GET.get('skills','').strip()
		due_date = request.GET.get('duedate','').strip()
		team_size = request.GET.get('teamsize','').strip()

		full_path = os.path.dirname(os.path.abspath(__file__))
		conn = sqlite3.connect(os.path.join(full_path, 'swb.db'))
		conn.execute('''CREATE TABLE IF NOT EXISTS projects (
			id integer PRIMARY KEY AUTOINCREMENT
			, company text
			, contact_first_name text
			, contact_last_name text
			, project_name text
			, project_skills text
			, project_summary text
			, due_date date
			, team_size integer
			)
			''')
		c = conn.cursor()

		c.execute("INSERT INTO projects (company, contact_first_name, contact_last_name, project_name, project_skills, project_summary, due_date, team_size) VALUES (?,?,?,?,?,?,?,?)", (company, first_name, last_name, project_name, summary, skills, due_date, team_size))
		conn.commit()
		c.close()

		return template('thankyou')

	else:

		return template('project_form')

# @route('/static/<filename>')
# def server_static(filename):
# 	return static_file(filename, root='/home/rebeldroid12/swb-db/static/')

# debug(True)
# run(host='localhost', port=8080, debug=True)

application = default_app()