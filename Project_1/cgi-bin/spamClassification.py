#! C:/Python36/python.exe

import cgi
import classifier

form = cgi.FieldStorage()

mail = form.getvalue("text")

category = classifier.classify(mail)

print("Content-type:text/html\r\n\r\n")
print("""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<h1>Message is {}</h1>
</body>
</html>
""".format(category[0]))