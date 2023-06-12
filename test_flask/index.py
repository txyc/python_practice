from flask import Flask, request, render_template, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Tianxin_2015@localhost:3306/test_userinfo' # 连接到您的数据库
db = SQLAlchemy(app)

class userinfo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.String(50), nullable=False)
    contact_info = db.Column(db.String(200), nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/page1')
def page1():
    return render_template('page1.html')

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/add_info_form')
def add_info_form():
    return render_template('add_info_form.html')

@app.route('/back')
def back():
    return redirect('/')  # 返回主页

# 用户输入存数据库的界面
@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    contact_info = request.form.get('contact_info')

    contact = userinfo(id=6, user=name, contact_info=contact_info)
    db.session.add(contact)  # 将新的test_userinfo实例添加到会话中以进行持久化操作
    db.session.commit()  # 提交更改到数据库

    # 返回执行结果
    return f"执行成功！用户{name}的联系方式{contact_info}已添加到数据库"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)