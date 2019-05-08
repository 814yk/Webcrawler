import requests
from bs4 import BeautifulSoup
import html5lib
import clipboard
url = input("주소를 입력하세요 : ")
r = requests.get(url)
soup=BeautifulSoup(r.text,'html.parser')
title=soup.find("title").text

body=[]

for wrapper in soup.find_all('p'):
    A=wrapper.text
    body.append(A)
    
try:
    body.remove("\n")
except ValueError:
    pass

html="<script src=\"http://code.jquery.com/jquery-latest.js\"></script><script>$(document).ready(function() { $(\'#AnnotationContent\').css(\"overflow-y\", \"scroll\");});</script><style type=\"text/css\">.tg  {border-collapse:collapse;border-spacing:0;border-color:#aabcfe;}.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aabcfe;color:#000000;background-color:#e8edff;}.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:#aabcfe;color:#000000;background-color:#b9c9fe;}.tg .tg-s268{text-align:left}</style><table class=\"tg\"><tr><th class=\"tg-s268\">"+title+"</th></tr><tr><td class=\"tg-s268\">"+body[0]+"</td></tr></table>"

clipboard.copy(html)
