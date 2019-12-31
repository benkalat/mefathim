#! /home/mefath5/.local/bin/python3
from time import gmtime, strftime
import cgi, cgitb 
print ("Content-Type: text/plain")
print ("")


# Create instance of FieldStorage 
form = cgi.FieldStorage() 

# Get data from fields
first_name = form.getvalue('first_name')
last_name  = form.getvalue('last_name')

print (first_name )

print ("<html>XYYYXXXX</html>")