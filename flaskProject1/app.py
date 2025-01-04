from flask import Flask,request,render_template
from datetime import datetime
# 数据库
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import text

app = Flask(__name__)
# 配置数据库
# MySQL所在的主机名
HOSTNAME = '127.0.0.1'
PORT = 3306
USERNAME = 'root'
PASSWORD = '221266'
DATABASE = 'flask_demo'
DB_URI = 'mysql+pymysql://{}:{}@{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, DATABASE)
app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI

# 在app.config中配置数据库连接信息
# 然后使用db = SQLAlchemy(app)创建一个数据库对象
db = SQLAlchemy(app)

migrate = Migrate(app, db)
# 迁移三步
# 1.flask db init  执行一次
# 2.flask db migrate  生成迁移脚本
# 3.flask db upgrade  运行迁移脚本

# 测试数据库连接是否正常
# with app.app_context():
#     # 使用 text() 包装 SQL 查询
#     with db.engine.connect() as conn:
#         rs = conn.execute(text('SELECT 1'))
#         print(rs.fetchone())  # 打印查询结果(1,)

# 建表
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)

# 外键
class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))  #外键关联user表主键id
    # backref:会自动给user表加一个book属性，来获取book 如：user = user.query.get(1)  user.book就可以访问id为1的作者的全部书
    author = db.relationship('User', backref='book')  # 定义关系 可以直接Book.author访问User的数据

# 数据库迁移
# with app.app_context():
#     db.create_all()
# 添加数据
@app.route('/user/add')
def user_add():
    user = User(name='rzz', password='123456')
    # 将orm对象添加到session中
    db.session.add(user)
    # 将session中的数据提交到数据库
    db.session.commit()
    return '添加成功'
# get请求查找
@app.route('/user/query')
def user_get():
    # 根据主键查找
    # users = User.query.get(1)
    users = User.query.all()  #列表
    # filter查找
    user = User.query.filter(User.name == 'rzz') # query类型，类似一个列表
    for u in user:
        print(u.name)
    return render_template('user_query.html', users=users)
# update修改
@app.route('/user/update')
def user_update():
    user = User.query.filter(User.name == 'rzz').first()
    user.name = 'rzz2'
    db.session.commit()
    return '修改成功'
# delete删除
@app.route('/user/delete')
def user_delete():
    user = User.query.filter(User.name == 'rzz2').first()
    db.session.delete(user)
    db.session.commit()
    return '删除成功'


# 过滤器(filter.html)
def datetime_format(value):
    return value.strftime('%Y-%m-%d %H:%M:%S')
app.add_template_filter(datetime_format, 'datetime')


@app.route('/')
def hello_world():
    return render_template('demo.html')

# @app.route('/')
# def hello_world():  # put application's code here
#     return 'Hello Worlewdd!'

@app.route('/hello/<name>')
def hello_name(name):
    dict = {
        "name":"rzz",
        "age":18
    }

    return render_template('demo2.html', name=name, dict=dict)

# 过滤/控制语句
@app.route('/filter')
def hello_filter():
    dict = {
        "name":"rzz",
        "age":18
    }
    books = [
        {"name":"python","price":100},
        {"name":"java","price":200},
        {"name":"c++","price":300}
    ]
    mytime = datetime.now()
    return render_template('filter.html', dict=dict, mytime=mytime, books=books)


# 带参数
# @app.route('/hello/<name>')
# def hello_name(name):
#     return 'Hello %s!' % name

# 查询字符串方式传参
# 如/book/?page=2 获得第二页的图书
@app.route('/book/')
def hello_default():
    # request.args:类字典类型
    page = request.args.get('page', '1')  #默认为1
    return f'第{page}页图书'



#debug模式：
# python app.py
#
# 子模版
@app.route('/child1')
def child1():
    return render_template('child1.html')

# 加载静态文件
@app.route('/static')
def static_demo():
    return render_template('static.html')



if __name__ == '__main__':
    app.run(debug=True)
