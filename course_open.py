# Course Checker
#
# Python programming intended to send messages via Email
# with updates from website (for sales, course availability, etc.)

import sys
import requests
import xml.etree.ElementTree as ET
import messageSMTP as SMTP

# ADD HERE: links to parse (UIUC course API)
link1 = "http://courses.illinois.edu/cisapp/explorer/schedule/2017/Spring/CS/411/31352.xml"

# exit if no links
if link1 == "":
	print("No link 1")

# get responses...... response = requests.get("http://www.website.com/link.xml")
response = requests.get(link1)	# use UIUC course API (with semester, year, etc., etc. in URL)

# load into trees (structure to parse xml data)
tree = ET.fromstring(response.content)

# list of relevant values to parse and look for
subject, number= ["CS", "411"]

# get section data, open, etc.
for child in tree.findall('parents'):
	subject = child.find('subject').attrib['id']
	number = child.find('course').attrib['id']
status = tree.find('enrollmentStatus').text

# create blank message to send
message = ""

# check if open
title = "Class Info"

# add to message if open
if (status != "Closed"):
	message += (subject + number + " - " + status + "\n")

else:
	message += "Nothing is Open"

# ADD HERE: email and password info
email = ""
key = ""

# no user data
if email == "" or key == "":
	print ("No email/password given")
	sys.exit()

# email to user
SMTP.email(email, email, title, message, key)
print("sent")

# print when done
print ("done")






