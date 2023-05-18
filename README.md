# txtFile.API
API that lets edit/access lines in a txt file in API hosting computer with headers

## Note
Currently there isn't support for special characters only letters, numbers and space.

## Usage
Designed to only be used with "GET" method and use headers
### Write
```http://192.169.1.45:5000/write```
Header|value|explanation
---|---|---
*write*|str(no special characters)|The text that will be put in txt file.
*line*|integer|The line number the text will be put old one will be repleaced.

**Responses:**  \
*ok:* "ok"  \
*not ok:* "missing header" (line header is not given)  \
, "line header only takes numbers" (line header didn't take number)  \
, "text header dosen't take special characters" (text header took special characters)

### Read
```http://192.169.1.45:5000/read```
Header|value|explanation
---|---|---
*line*|integer|The line number of the text that will be returned

**Responses:**  \
*ok:* {"result": "<the_result>"}  \
*not ok:* "missing header" (line header is not given)  \
, "line header only takes numbers" (line header didn't take number)
