from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <html>
            <body>
                <form action="/submit" method="post">
                    参数1: <input type="text" name="param1"><br>
                    参数2: <input type="text" name="param2"><br>
                    <input type="submit" value="提交">
                </form>
            </body>
        </html>
    '''

@app.route('/submit', methods=['POST'])
def submit():
    param1 = request.form.get('param1')
    param2 = request.form.get('param2')

    # 调用Python程序执行
    result = my_python_function(param1, param2)

    # 返回执行结果
    return result

def my_python_function(param1, param2):
    # 在此处编写你的Python程序，并返回执行结果
    return f"执行成功！参数1为{param1}，参数2为{param2}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)