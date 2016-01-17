#Project form

from bottle import get, post, request, route, run, template, static_file

@route('/project_form')
def project_form():
    return template('views/project_form')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/rebeldroid12/swb-db/static/')

run(host='localhost', port=8080, debug=True)

