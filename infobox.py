import requests
from bs4 import BeautifulSoup
import clipboard

url = input("주소를 입력하세요 : ")
r = requests.get(url)

soup = BeautifulSoup(r.text, "html5lib")

infobox_key = soup.find("table", class_="infobox") 
infobox_value=soup.find("table",class_="infobox")

title=soup.find("title").text

key=[]
value=[]

for wrapper in infobox_key.find_all('th'):
    for colspan in infobox_key.findAll(attrs ={"colspan" : "2"}):
        colspan.decompose()
    A=wrapper.text
    if A != "":
        key.append(A)

for wrapper in infobox_value.findAll('td'):
    for colspan in infobox_value.findAll(attrs ={"colspan" : "2"}):
            colspan.decompose()
    B=wrapper.text
    if B != "":
        value.append(B)

html="<script src=\"http://code.jquery.com/jquery-latest.js\"></script><script>$(document).ready(function() { $(\'#AnnotationContent\').css(\"overflow-y\", \"scroll\");});</script><style type=\"text/css\">"+".tg  {border-collapse:collapse;border-spacing:0;border-color:#bbb;}"+".tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#bbb;color:#594F4F;background-color:#E0FFEB;}"+".tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#bbb;color:#493F3F;background-color:#9DE0AD;}"+".tg .tg-c3ow{border-color:inherit;text-align:center;vertical-align:top}"+".tg .tg-0lax{text-align:left;vertical-align:top}"+".tg .tg-0pky{border-color:inherit;text-align:left;vertical-align:top}"+"</style>"+"<table class=\"tg\">"+"<tr>"+"<th class=\"tg-c3ow\"colspan=\"2\"><br>"+title+"</th>"+"</tr>"+"<tr><td class=\"tg-0lax\">"+''.join(key[0])+"<br></td><td class=\"tg-0lax\">"+''.join(value[0])+"<br></td></tr>"+"<tr><td class=\"tg-0pky\">"+''.join(key[1])+"<br></td><td class=\"tg-0lax\">"+''.join(value[1])+"<br></td></tr>"+"<tr><td class=\"tg-0pky\">"+''.join(key[2])+"<br></td><td class=\"tg-0lax\">"+''.join(value[2])+"<br></td></tr>"+"<tr><td class=\"tg-0pky\">"+''.join(key[3])+"<br></td><td class=\"tg-0lax\">"+''.join(value[3])+"<br></td></tr>"+"</table>"

clipboard.copy(html)

#with open("%s.txt" % title, "w") as f:
    #f.write(html)
