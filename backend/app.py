from flask import Flask, jsonify, request, render_template, url_for, redirect
from backend.todolist.controller import Controller
from flask_cors import CORS
import json

# from forms import SignUpForm
# import cgi

app = Flask(__name__)
CORS(app)
controller = Controller(table_name="TodoListTest")


# html_form = cgi.FieldStorage()
# html_data = html_form.getvalue("content")
# print(html_data)

# 查看
@app.route('/')
def index():
    # return 'TodoList'
    result = controller.index()
    return jsonify(result)


# def pagination(page, limit):
#     db_len = controller.table_length()['length']
#     offset = limit * (page - 1)
#
#     # find the maximum page number
#     if db_len % limit == 0:
#         max_page = int(db_len / limit)
#     else:
#         max_page = int(db_len / limit) + 1
#
#     # print(f"max page for limit={limit}: {max_page} ")
#
#     if page <= max_page:
#         result = controller.paged_index(limit=limit, offset=offset)
#         return jsonify({'data': result, 'db_len': db_len})
#     else:
#         return "no data available"


# 檢索（分頁）
@app.route('/index')
def paged_index():
    page = controller.pagination(page=int(request.args['page']), limit=int(request.args['limit']))
    return jsonify(page)


# 新增
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        data = request.get_data()
        data = json.loads(data)
        data = data["content"]
        controller.add_task(data=data)
        page = controller.pagination(page=int(request.args['page']), limit=int(request.args['limit']))
        return jsonify(page)

    else:
        return render_template('add.html')


# 刪除
@app.route('/delete/<int:task_id>', methods=['GET', 'DELETE'])
def delete_task(task_id):
    if request.method == 'DELETE':
        controller.delete_task(task_id)
        page = controller.pagination(page=int(request.args['page']), limit=int(request.args['limit']))
        return jsonify(page)

    else:
        err_msg = {'code': 1, 'msg': 'ERROR: please use DELETE method'}
        return jsonify(err_msg)


# 編輯
@app.route('/edit/<int:task_id>', methods=['GET', 'PUT'])
def edit_task(task_id):
    if request.method == 'PUT':
        data = request.get_data()
        data = json.loads(data)
        data = data["content"]
        controller.edit_task(task_id=task_id, data=data)
        page = controller.pagination(page=int(request.args['page']), limit=int(request.args['limit']))
        return jsonify(page)

    else:
        err_msg = {'code': 1, 'msg': 'ERROR: please use PUT method'}
        return jsonify(err_msg)


# 標註為完成
@app.route('/done/<int:task_id>', methods=['GET', 'PUT'])
def task_done(task_id):
    if request.method == 'PUT':
        controller.task_done(task_id)
        page = controller.pagination(page=int(request.args['page']), limit=int(request.args['limit']))
        return jsonify(page)

    else:
        err_msg = {'code': 1, 'msg': 'ERROR: please use PUT method'}
        return jsonify(err_msg)


# 標註為未完成
@app.route('/undo/<int:task_id>', methods=['GET', 'PUT'])
def task_undo(task_id):
    if request.method == 'PUT':
        controller.task_undo(task_id)
        page = controller.pagination(page=int(request.args['page']), limit=int(request.args['limit']))
        return jsonify(page)

    else:
        err_msg = {'code': 1, 'msg': 'ERROR: please use PUT method'}
        return jsonify(err_msg)


@app.route('/count')
def table_length():
    result = controller.table_length()
    return jsonify(result)


# 開啟編輯
# @app.route('/editon/<int:task_id>', methods=['GET', 'PUT'])
# def edit_on(task_id):
#     if request.method == 'PUT':
#         result = controller.edit_on(task_id)
#         return jsonify(result)
#     else:
#         err_msg = {'code': 1, 'msg': 'ERROR: please use PUT method'}
#         return jsonify(err_msg)


# 關閉編輯
# @app.route('/editoff/<int:task_id>', methods=['GET', 'PUT'])
# def edit_off(task_id):
#     if request.method == 'PUT':
#         result = controller.edit_off(task_id)
#         return jsonify(result)
#     else:
#         err_msg = {'code': 1, 'msg': 'ERROR: please use PUT method'}
#         return jsonify(err_msg)


@app.route('/create_table')
def create_table():
    controller.create_table()
    return "success"


if __name__ == '__main__':
    app.run()
