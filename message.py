file = open("messages.html")
out = open("out.html", 'w')

import sys

s = ""

for line in file:
  if "<div class=\"message\">" not in line and "Mitchell Vitez" not in line and "Evan Chavis" not in line:
		if line != "" and "<div class=\"msgbody\">" not in line:
			if "<abbr class=\"time published\"" not in line:
				line = line.replace("<div class=\"from\"><span class=\"profile fn\">","")
				line = line.replace("</div>","")
				line = line.replace("</span>","")
				s += line
out.write(s)
