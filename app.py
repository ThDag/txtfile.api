# TODO: add to github, add read function
from flask import Flask, request
import json

app = Flask(__name__)

# request_num = 0

@app.route('/write', methods = ['GET'])
def root():
    data = request.args

    # error handling
    if 'line' not in data or 'text' not in data:
        return 'missing headers'
    elif not data.get('line', default='None').isdigit():
        return 'line header only takes numbers'
    # checks if text has special characters
    elif not data.get('text', default='None').isalnum():
        # detects if the special characters is space and ignores it
        if not str(data.get('text', default='None')).replace(' ', 'x').isalnum():
            if str(data.get('text', default='None')).replace('%', 'x').isalnum():
                return 'text header doen\'t take special characters'

    # opens datas to get the text inside
    with open('datas.txt', 'r') as file:
        lines = file.readlines()
        print(lines)

    # if line exceeds datas size new lines is inserted
    if int(data.get('line', default='None')) >= len(lines):
        lines_to_add = int(data.get('line', default='None')) - len(lines) 
        lines_to_add += 1 
        for  i in range(lines_to_add):
            lines.append('\n')

    # opens datas to update the text
    with open('datas.txt', 'w') as file:
        try:
            
            lines[int(data.get('line', default='0', type=int))] = data.get('text', default='null', type=str) + '\n' # changes the desired line to desired text 
            file.writelines(lines) # updates the datas file

        except Exception as e:
            return f'Unexpected Error: {repr(e)}'

    return 'ok' 

@app.route('/read', methods=['GET'])
def read():
    data = request.args

    # error handling
    if 'line' not in data:
        return 'missing headers'
    elif not data.get('line', default='None').isdigit():
        return 'line header only takes numbers'

    # opens datas to get the text inside
    with open('datas.txt', 'r') as file:
        lines = file.readlines()
    
    result = {'result': lines[int(data.get('line', default='None'))]}
    print(type(json.dumps(result)))
    return json.dumps(result).replace('\\n', '')
    

if __name__ == '__main__':
    app.run(debug = True, port = 5001, host = '0.0.0.0')
