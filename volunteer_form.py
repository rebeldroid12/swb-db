#Volunteerform

from bottle import get, post, request, route, run, template, static_file

@route('/volunteer_form')
def volunteer_form():
    return template('views/volunteer_form')

@route('/static/<filename>')
def server_static(filename):
    return static_file(filename, root='/home/rebeldroid12/swb-db/static/')

run(host='localhost', port=8080, debug=True)
