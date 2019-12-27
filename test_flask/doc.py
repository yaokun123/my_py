# coding:utf-8
from flask import Flask
app = Flask(__name__)



'''
1、路由
'''
# route() 装饰器把一个函数绑定到对应的 URL 上。
# 这里是一些基本的例子:
@app.route('/')
def index():
    return 'Index Page'



'''
2、变量规则
'''
# 要给 URL 添加变量部分，你可以把这些特殊的字段标记为 <variable_name> ，
# 这个部分将会作为命名参数传递到你的函数。
# 规则可以用 <converter:variable_name> 指定一个可选的转换器(int接受整数/float接受浮点数/path)。
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id


'''
3、唯一 URL / 重定向行为
'''
# Flask 的 URL 规则基于 Werkzeug 的路由模块。
# 这个模块背后的思想是基于 Apache 以及更早的 HTTP 服务器主张的先例，保证优雅且唯一的 URL。
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
# 虽然它们看起来着实相似，但它们结尾斜线的使用在 URL 定义 中不同。
#  第一种情况中，指向 projects 的规范 URL 尾端有一个斜线。
# 这种感觉很像在文件系统中的文件夹。
# 访问一个结尾不带斜线的 URL 会被 Flask 重定向到带斜线的规范 URL 去。

# 然而，第二种情况的 URL 结尾不带斜线，类似 UNIX-like 系统下的文件的路径名。
# 访问结尾带斜线的 URL 会产生一个 404 “Not Found” 错误。

# 这个行为使得在遗忘尾斜线时，允许关联的 URL 接任工作，与 Apache 和其它的服务器的行为并无二异。
# 此外，也保证了 URL 的唯一，有助于避免搜索引擎索引同一个页面两次。



'''
4、构造 URL
'''
# 如果 Flask 能匹配 URL，那么 Flask 可以生成它们吗？
# 当然可以。你可以用 url_for() 来给指定的函数构造 URL。
# 它接受函数名作为第一个参数，也接受对应 URL 规则的变量部分的命名参数。
# 未知变量部分会添加到 URL 末尾作为查询参数。

from flask import url_for
@app.route('/')
def index(): pass

@app.route('/login')
def login(): pass

@app.route('/user/<username>')
def profile(username): pass

with app.test_request_context():
    print url_for('index')# /
    print url_for('login')# /login
    print url_for('login', next='/') # /login?next=/
    print url_for('profile', username='John Doe')# /user/John%20Doe

# 为什么你要构建 URL 而非在模板中硬编码？这里有三个绝妙的理由：
# 1、反向构建通常比硬编码的描述性更好。更重要的是，它允许你一次性修改 URL， 而不是到处边找边改。
# 2、URL 构建会转义特殊字符和 Unicode 数据，免去你很多麻烦。
# 3、如果你的应用不位于 URL 的根路径（比如，在 /myapplication 下，而不是 / ）， url_for() 会妥善处理这个问题。



'''
5、HTTP 方法
'''
# HTTP （与 Web 应用会话的协议）有许多不同的访问 URL 方法。默认情况下，路由只回应 GET 请求，
# 但是通过 route() 装饰器传递 methods 参数可以改变这个行为。这里有一些例子:
from flask import request
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        pass
        #do_the_login()
    else:
        pass
        #show_the_login_form()



'''
6、静态文件
'''
# 动态 web 应用也会需要静态文件，通常是 CSS 和 JavaScript 文件。
# 理想状况下， 你已经配置好 Web 服务器来提供静态文件，但是在开发中，Flask 也可以做到。
# 只要在你的包中或是模块的所在目录中创建一个名为 static 的文件夹，在应用中使用 /static 即可访问。
# 给静态文件生成 URL ，使用特殊的 'static' 端点名:
url_for('static', filename='style.css')#这个文件应该存储在文件系统上的 static/style.css 。



'''
7、模板渲染
'''
# 用 Python 生成 HTML 十分无趣，而且相当繁琐，因为你必须手动对 HTML 做转义来保证应用的安全。
# 为此，Flask 配备了 Jinja2 模板引擎。

# 你可以使用 render_template() 方法来渲染模板。
# 你需要做的一切就是将模板名和你想作为关键字的参数传入模板的变量。
# 这里有一个展示如何渲染模板的简例:
from flask import render_template
@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

# Flask 会在 templates 文件夹里寻找模板。
# 所以，如果你的应用是个模块，这个文件夹应该与模块同级；
# 如果它是一个包，那么这个文件夹作为包的子目录:

# 情况 1: 模块:
# /application.py
# /templates
#     /hello.html

# 情况 2: 包:
# /application
#     /__init__.py
#     /templates
#         /hello.html

# 关于模板，你可以发挥 Jinja2 模板的全部实例。更多信息请见 Jinja2 模板文档 。
# 这里有一个模板实例：
'''
<!doctype html>
<title>Hello from Flask</title>
{% if name %}
  <h1>Hello {{ name }}!</h1>
{% else %}
  <h1>Hello World!</h1>
{% endif %}
'''
# 在模板里，你也可以访问 request 、 session 和 g [1] 对象，
# 以及 get_flashed_messages() 函数。



'''
8、访问请求数据
'''
# 对于 Web 应用，与客户端发送给服务器的数据交互至关重要。
# 在 Flask 中由全局的 request 对象来提供这些信息。
# 如果你有一定的 Python 经验，你会好奇，为什么这个对象是全局的，为什么 Flask 还能保证线程安全。
# 答案是环境作用域



'''
9、环境局部变量
'''



'''
10、请求对象
'''
# 当前请求的 HTTP 方法可通过 method 属性来访问。
@app.route('/login', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],request.form['password']):
            return log_the_user_in(request.form['username'])
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('login.html', error=error)
def valid_login(username,password):
    pass
def log_the_user_in(username):
    pass

# 当访问 form 属性中的不存在的键会发生什么？会抛出一个特殊的 KeyError 异常。
# 你可以像捕获标准的 KeyError 一样来捕获它。
# 如果你不这么做，它会显示一个 HTTP 400 Bad Request 错误页面。
# 所以，多数情况下你并不需要干预这个行为。

# 你可以通过 args 属性来访问 URL 中提交的参数 （ ?key=value ）:
searchword = request.args.get('q', '')
# 我们推荐用 get 来访问 URL 参数或捕获 KeyError ，
# 因为用户可能会修改 URL，向他们展现一个 400 bad request 页面会影响用户体验。

# 欲获取请求对象的完整方法和属性清单，请参阅 request 的文档。



'''
11、文件上传
'''
# 用 Flask 处理文件上传很简单。只要确保你没忘记在 HTML 表单中设置
#  enctype="multipart/form-data" 属性，不然你的浏览器根本不会发送文件。

# 已上传的文件存储在内存或是文件系统中一个临时的位置。
# 你可以通过请求对象的 files 属性访问它们。
# 每个上传的文件都会存储在这个字典里。
# 它表现近乎为一个标准的 Python file 对象，
# 但它还有一个 save() 方法，这个方法允许你把文件保存到服务器的文件系统上。
# 这里是一个用它保存文件的例子:
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/uploaded_file.txt')

# 如果你想知道上传前文件在客户端的文件名是什么，你可以访问 filename 属性。
# 但请记住， 永远不要信任这个值，这个值是可以伪造的。
# 如果你要把文件按客户端提供的文件名存储在服务器上，
# 那么请把它传递给 Werkzeug 提供的 secure_filename() 函数:
from werkzeug import secure_filename
@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['the_file']
        f.save('/var/www/uploads/' + secure_filename(f.filename))
# 一些更好的例子，见 上传文件 模式。



'''
12、Cookies
'''
# 你可以通过 cookies 属性来访问 Cookies，用响应对象的 set_cookie 方法来设置 Cookies。
# 请求对象的 cookies 属性是一个内容为客户端提交的所有 Cookies 的字典。
# 如果你想使用会话，请不要直接使用 Cookies，请参考 会话 一节。
# 在 Flask 中，已经注意处理了一些 Cookies 安全细节。

# 读取 cookies:
@app.route('/')
def index():
    username = request.cookies.get('username')

# 存储 cookies:
from flask import make_response
@app.route('/')
def index():
    resp = make_response(render_template())
    resp.set_cookie('username', 'the username')
    return resp
# 可注意到的是，Cookies 是设置在响应对象上的。
# 由于通常视图函数只是返回字符串，之后 Flask 将字符串转换为响应对象。
# 如果你要显式地转换，你可以使用 make_response() 函数然后再进行修改。

# 为此，也可以阅读 关于响应 。



'''
13、重定向和错误
'''
# 你可以用 redirect() 函数把用户重定向到其它地方。
# 放弃请求并返回错误代码，用 abort() 函数。
# 这里是一个它们如何使用的例子:
from flask import abort, redirect
@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login')
def login():
    abort(401)
    #this_is_never_executed()

# 默认情况下，错误代码会显示一个黑白的错误页面。
# 如果你要定制错误页面， 可以使用 errorhandler() 装饰器:

from flask import render_template
@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404



"""
14、关于响应
"""
# 视图函数的返回值会被自动转换为一个响应对象。
# 如果返回值是一个字符串， 它被转换为该字符串为主体的、状态码为 200 OK``的 、 MIME 类型是 ``text/html 的响应对象。
# Flask 把返回值转换为响应对象的逻辑是这样

'''
1、如果返回的是一个合法的响应对象，它会从视图直接返回。
2、如果返回的是一个字符串，响应对象会用字符串数据和默认参数创建。
3、如果返回的是一个元组，且元组中的元素可以提供额外的信息。这样的元组必须是 
(response, status, headers) 的形式，且至少包含一个元素。 
status 值会覆盖状态代码， headers 可以是一个列表或字典，作为额外的消息标头值。
4、如果上述条件均不满足， Flask 会假设返回值是一个合法的 WSGI 应用程序，并转换为一个请求对象。
'''
# 如果你想在视图里操纵上述步骤结果的响应对象，可以使用 make_response() 函数。
# 譬如你有这样一个视图:
@app.errorhandler(404)
def not_found(error):
    return render_template('error.html'), 404
# 你只需要把返回值表达式传递给 make_response() ，获取结果对象并修改，然后再返回它:
@app.errorhandler(404)
def not_found(error):
    resp = make_response(render_template('error.html'), 404)
    resp.headers['X-Something'] = 'A value'
    return resp



'''
15、会话
'''
# 除请求对象之外，还有一个 session 对象。它允许你在不同请求间存储特定用户的信息。
# 它是在 Cookies 的基础上实现的，并且对 Cookies 进行密钥签名。
# 这意味着用户可以查看你 Cookie 的内容，但却不能修改它，除非用户知道签名的密钥。

# 要使用会话，你需要设置一个密钥。这里介绍会话如何工作:
from flask import session,escape
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

# 这里提到的 escape() 可以在你模板引擎外做转义（如同本例）。



'''
16、消息闪现
'''



'''
17、日志记录
'''
# 有时候你会处于这样一种境地，你处理的数据本应该是正确的，但实际上不是。
#  比如，你会有一些向服务器发送请求的客户端代码，但请求显然是畸形的。
# 这可能是用户篡改了数据，或是客户端代码的粗制滥造。
# 大多数情况下，正常地返回 400 Bad Request 就可以了，但是有时候不能这么做，并且要让代码继续运行。

# 你可能依然想要记录下，是什么不对劲。这时日志记录就派上了用场。从 Flask 0.3 开始，Flask 就已经预置了日志系统。
app.logger.debug('A value for debugging')
app.logger.warning('A warning occurred (%d apples)', 42)
app.logger.error('An error occurred')



'''
18、整合 WSGI 中间件
'''
# 如果你想给你的应用添加 WSGI 中间件，你可以封装内部 WSGI 应用。
# 例如若是你想用 Werkzeug 包中的某个中间件来应付 lighttpd 中的 bugs ，可以这样做:
from werkzeug.contrib.fixers import LighttpdCGIRootFix
app.wsgi_app = LighttpdCGIRootFix(app.wsgi_app)



'''
19、
'''