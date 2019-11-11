from flask import Flask, render_template, g, request, redirect
from priority import Priority
from task import Task
import json
import os.path

app = Flask(__name__)

TASKS_LIST = list()
id = 0


@app.route('/')
def get_task_list():

    return render_template('index.html', tasks=TASKS_LIST)


@app.route('/submit', methods=['POST'])
def add():

    global id
    id += 1
    desc = request.form['task']
    email = request.form['email']

    p = lambda x: Priority.high.value if x == "High" else Priority.medium.value if x == "Medium" else Priority.low.value
    priority = p(request.form['priority'])

    if desc is not None and email is not None:
        task = Task(id, desc, email, priority)
        TASKS_LIST.append(task)

    return redirect('/')


@app.route('/save')
def save():

    with open('tasks.json', 'w') as j_file:
        json_str = json.dumps(TASKS_LIST, default=obj_dict)
        j_file.write(json_str)

    # Store id Counter
    with open('counter.txt', 'w') as id_file:
        id_file.write(str(id))

    return redirect('/')


@app.route('/delete/<id>')
def delete(id=None):
    print(id)
    return redirect('/')


@app.route('/clear')
def clear():
    TASKS_LIST.clear()
    global id
    id = 0

    return redirect('/')


@app.route('/status')
def updateStatus():
    print("Under Construction")
    return redirect('/')


def obj_dict(obj):
    return obj.__dict__


if __name__ == '__main__':

    # Check is json task file exists
    isFile = os.path.exists('tasks.json')

    if isFile:
        with open('tasks.json', 'r') as json_file:
            TASKS_LIST = json.load(json_file)

        with open('counter.txt', 'r') as file:
            temp = str(file.read())
            id = int(temp)

    app.run()
