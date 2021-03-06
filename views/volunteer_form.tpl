<html>
    <head>
        <link rel="stylesheet" href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
        <link rel="stylesheet" href="/static/main.css" />
        <title>SWB Volunteer Sign Up Form</title>
    </head>
    <body>
        <div class="container">
        	<h1>Statistics Without Borders Volunteer Sign Up Form</h1>
            <form action="/volunteer_form" method="GET">
                <div class="form-group">
                    <b>Volunteer Name: </b> <input name="firstname" type="text" class="form-control" placeholder="First Name"/><input name="lastname" type="text" class="form-control" placeholder="Last Name"/><br>

                    <b>E-mail Address: </b> <input name="email" type="email" class="form-control"/><br>

                    <b>Current Position: </b> <input name="position" type="text" class="form-control"/><br>

                    <b>Current Employer: </b> <input name="employer" type="text" class="form-control"/><br>

                    <b>Current Country: </b> <input name="country" type="text" class="form-control"/><br>

                    <b>State (if in U.S.): </b> <input name="state-USA" type="text" class="form-control"/><br>
                    
                    <b>Statistical Expertise:</b>
                    <textarea class="form-control" rows="5" name="expertise"></textarea><br><br>

                    <b>Software Skills (use comma for different skills): </b> <textarea class="form-control" rows="5" name="skills"></textarea><br><br><br>

                    <b>What Languages are you fluent in?</b> <textarea class="form-control" rows="5" name="languages"></textarea><br><br>

                    <b>Please briefly describe some of your experience (with an indication of the number of years of relevant experience) that may be relevant/useful to SWB projects.</b>
                    <textarea class="form-control" rows="5" name="experience"></textarea><br><br>

                    <input value="Submit" type="submit" name="submit-data" class="btn btn-default"/>

                </div>
            </form>
        </div>
     </body>