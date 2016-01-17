from bottle import get, post, request, route, run

#@get('/login') # or
@route('/login')
def login():
    return '''
        <form action="/login" method="post">
            Username: <input name="username" type="text" />
            Password: <input name="password" type="password" />
            <input value="Login" type="submit" />
        </form>
    '''

run(host='localhost', port=8080, debug=True)