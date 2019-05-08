import requests
from bs4 import BeautifulSoup
import html5lib
import clipboard
url = input("주소를 입력하세요 : ")
r = requests.get(url)
soup=BeautifulSoup(r.text,'html5lib')
title=soup.find("title").text

body=[]

for wrapper in soup.find_all('li',{"class":"search-product"}):
    body.append(wrapper)


html="<script src=\"http://code.jquery.com/jquery-latest.js\"></script><script>$(document).ready(function() { $(\'#AnnotationContent\').css(\"overflow-y\", \"scroll\");});</script><style type=\"text/css\">.tg  {border-collapse:collapse;border-spacing:0;}.tg td{font-family:Arial, sans-serif;font-size:14px;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}.tg th{font-family:Arial, sans-serif;font-size:14px;font-weight:normal;padding:10px 5px;border-style:solid;border-width:1px;overflow:hidden;word-break:normal;border-color:black;}.tg .tg-vv3i{font-weight:bold;background-color:#f56b00;border-color:#333333;text-align:center}.tg .tg-oma9{background-color:#ffce93;border-color:#333333;text-align:center}  a:link { color: black; text-decoration: none;}a:visited { color: black; text-decoration: none;}a:hover { color: blue; text-decoration: underline;}</style><table class=\"tg\">  <tr>    <th class=\"tg-vv3i\">"+title+"</th></tr><tr><td class=\"tg-oma9\">"+body[0].prettify().replace("/vp/products/","https://www.coupang.com/vp/products/")+"</td></tr><tr><td class=\"tg-oma9\">"+body[1].prettify().replace("/vp/products/","https://www.coupang.com/vp/products/")+"</td>  </tr></table>"

clipboard.copy(html)
