<html>
    <head>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
        <link rel="stylesheet" href="/static/main.css" />
        <title>SWB Project Submit Form</title>
    </head>
    <body>
        <div class="container">
        <h1>Project Submit Form</h1><hr>
                <form action="/project_form" method="GET">
                    <div class="form-group">
                    <b>Company/Organization: </b> <input name="company" type="text" class="form-control"/><br>

                    <b>Contact's First Name:</b> <input name="firstname" type="text" class="form-control"/><br>

                    <b>Contact's Last Name:</b> <input name="lastname" type="text" class="form-control"/><br>

                    <b>Project Name:</b> <input name="project" type="text" class="form-control"/><br>

                    <b>Project Summary:</b> <input name="summary" type="text" class="form-control"/><br>

                    <b>Project Skill Needs:</b> <input name="skills" type="text" class="form-control"/><br>

                    <b>Approximate Due Date:</b> <input name="duedate" type="date" class="form-control"/><br>

                    <b>Desired Team Size (Number of individuals): <input name="teamsize" type="number" class="form-control"/><br>
                    <input value="Submit" type="submit" name="submit-data" class="btn btn-default"/>
                    </div>
                </form>
        </div>
    </body>
