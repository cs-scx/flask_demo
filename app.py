from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
# 在项目根目录下生成text.db数据库
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

# 创建ToDo表，定义字段
class Todo(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    date_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return '<Task %r>' % self.id

@app.route('/', methods = ['POST', 'GET'])
def index():
    # 接受到GET请求时从数据库中查询所有数据，并将数据传送到index.html页面
    if request.method == 'GET':
        tasks = Todo.query.order_by(Todo.date_created).all()
        return render_template('index.html', tasks = tasks)

    # 接受到index.html页面的POST请求时，获取表单数据,生成一个Todo对象，添加到数据库中
    else:
        task_content = request.form['content']
        new_task = Todo(content = task_content)
        try:
            if task_content != '':
                db.session.add(new_task)
                db.session.commit()
            return redirect('/')
        except:
            return '添加任务失败'

# 获取页面传递的数据id,删除对应的对象,执行操作成功后重定向到 / 显示数据
@app.route('/delete/<int:id>')
def delete(id):
    task_to_delete = Todo.query.get_or_404(id)

    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return "删除任务失败"

# GET请求时update.html页面获取传入的id显示task content属性,
@app.route('/update/<int:id>', methods = ['POST', 'GET'])
def update(id):
    task_to_update = Todo.query.get_or_404(id)
    if request.method == 'GET':
        return render_template('update.html', task = task_to_update)

    # 接受POST请求时，获取表单数据，重新设置task content属性将complete属性设为默认值（0）,重定向至 / 显示数据
    else:
        task_to_update.content = request.form['content']
        task_to_update.completed = 0
        try:
            db.session.commit()
            return redirect('/')
        except:
            return "更新任务失败"

# 修改task complete属性的值为完成状态（1）,重定向值 / 显示数据
@app.route('/complete/<int:id>')
def complete(id):
    task_to_complete = Todo.query.get_or_404(id)
    task_to_complete.completed = 1
    try:
        db.session.commit()
        return redirect('/')
    except:
        return "修改任务状态失败"




if __name__ == '__main__':
    app.run(debug = True)
