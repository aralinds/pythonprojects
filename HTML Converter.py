f = open("atlbraves.html","r")
text = f.read()
text = text.replace("<h1>","")
text = text.replace("</h1>","")
print("========================") #it won't show up under the title
text = text.replace("<li>","")
text = text.replace("</li>","")
text = text.replace("</ul>","")
text = text.replace("<ul>","")
text = text.lstrip()
#players = print("1. Ronald Acuna (LF)") wont show up in numbered order

print(text)
