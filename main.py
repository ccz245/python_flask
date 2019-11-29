from flask import Flask, request


employees = {'charles': {'age': 31, 'weight': 90},
            'william': {'age':29, 'weight': 82}}

app = Flask(__name__)

# get, read info
@app.route('/<name>')
def get_employee_info(name):
    return employees[name]

# get all, read info
@app.route('/all')
def get_all_employee_info():
    return employees

# post, add info
@app.route('/<name>', methods=['POST']) 
def add_new_employee(name):
    employees[name]=request.json
    return employees[name]

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug = True)    # auto reload after change, POST will not last
