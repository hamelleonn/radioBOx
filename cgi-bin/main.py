#!/usr/bin/env python3
import cgi
import cgitb

cgitb.enable()

print("Content-type: text/html")
print()

print("<html><head><title>User Registration Results</title></head><body>")
print("<h1>User Registration Results</h1>")

form = cgi.FieldStorage()

if "username" in form and "password" in form and "email" in form:
    username = form.getvalue("username")
    password = form.getvalue("password")
    email = form.getvalue("email")
    newsletter = form.getvalue("newsletter")
    country = form.getvalue("country")
    gender = form.getvalue("gender")

    print("<p>Username: {0}</p>".format(username))
    print("<p>Password: {0}</p>".format(password))
    print("<p>Email: {0}</p>".format(email))
    print("<p>Subscribed to newsletter: {0}</p>".format("Yes" if newsletter else "No"))
    print("<p>Country: {0}</p>".format(country))
    print("<p>Gender: {0}</p>".format(gender))

print("</body></html>")
