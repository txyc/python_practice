# @click.command()装饰指定函数，是指成为命令行接口
# @click.argument('param-name')指定必备参数，click会将参数名解析为"param_name"
#   type——表示参数的类型
# @click.option()通过指定命令行选项的名称，从命令行读取参数值，再将其传递给函数。
#   --para——第一个参数值，用于指定命令行选项的名字，转化为para给后续的程序使用
#   type——表示参数的类型
#   prompt——参数用于提示用户需要输入的参数
#   default——提供默认值
#   help——参数的说明
#   nargs——指定命令行参数接收值的个数
#   metavar——如何在帮助页面表示值
#   hide_input——隐藏输入，常用于密码输入
#   confirmation_prompt——重复输入，常用于密码输入
# click.echo()的输出可以在不同python版本之间获得更好的兼容性
# @click.group()用于创建一个命令行组，将add_command()加入的函数
import click

@click.command() 
@click.option('--count', prompt='count', default=1, help='Number of greetings.')
@click.option('--name', prompt='Your name', help='user name')
@click.option('--password', prompt='Password', hide_input=True, confirmation_prompt=True, help='password')
def hello(count, name, password):
    for x in range(count):
        click.echo('Hello {:s}!'.format(name))
        click.echo(password)

@click.command() 
@click.argument('count1', type=int)
@click.argument('user-name')
def hello1(count1, user_name):
    for x in range(count1):
        click.echo("Hello {:s}".format(user_name))

@click.command()
def initdb():
    click.echo("Initialized the database")

@click.group()
def excute_click():
    pass

excute_click.add_command(initdb)
excute_click.add_command(hello)
excute_click.add_command(hello1)

if __name__ == "__main__":
    excute_click()
