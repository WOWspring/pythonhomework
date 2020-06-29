#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/6/20 19:44
# @Author  : Ryu
# @Site    : 
# @File    : requests_study.py.py
# @Software: PyCharm

#urllib抓取网页
import urllib
response = urllib.urlopen("http://www.baidu.com")
print(response.read())

#编写values用urllib编码，实现POST
import urllib import urllib2
values = {"username":"1016903103@qq.com","password":"XXXX"}
data = urllib.urlencode(values)
url = "https://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()

#POST的另一种方法
import urllib import urllib2
values = {}
values['username'] = "1016903103@qq.com"
values['password'] = "XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login?from=http://my.csdn.net/my/mycsdn"
request = urllib2.Request(url,data)
response = urllib2.urlopen(request)
print response.read()

#GET的实现
import urllib import urllib2
values={} values['username'] = "1016903103@qq.com"
values['password']="XXXX"
data = urllib.urlencode(values)
url = "http://passport.csdn.net/account/login"
geturl = url + "?"+data
request = urllib2.Request(geturl)
response = urllib2.urlopen(request)
print response.read()

#headers中agent设置
import urllib import urllib2
url = 'http://www.server.com/login'
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
values = {'username' : 'cqc', 'password' : 'XXXX' }
headers = { 'User-Agent' : user_agent }
data = urllib.urlencode(values)
request = urllib2.Request(url, data, headers)
response = urllib2.urlopen(request)
page = response.read()

#设置refer应对“反盗链”
headers = {'User-Agent': 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
           'Referer': 'http://www.zhihu.com/articles'}

# 另外headers的一些属性，下面的需要特别注意一下：
# User - Agent: 有些服务器或Proxy会通过该值来判断是否是浏览器发出的请求
# Content - Type: 在使用REST接口时，服务器会检查该值，用来确定HTTPBody中的内容该怎样解析。
# application / xml ： 在XMLRPC，如RESTful / SOAP调用时使用
# application / json ： 在JSONRPC调用时使用
# application / x - www - form - urlencoded ： 浏览器提交Web表单时使用在使用服务器提供的RESTful或SOAP
# 服务时， Content - Type设置错误会导致服务器拒绝服务
# 其他的有必要的可以审查浏览器的headers内容，在构建时写入同样的数据即可。


#设置proxy代理绕过ip访问次数限制
import urllib2
enable_proxy = True
proxy_handler = urllib2.ProxyHandler({"http" : 'http://some-proxy.com:8080'})
null_proxy_handler = urllib2.ProxyHandler({})
if enable_proxy:
    opener = urllib2.build_opener(proxy_handler)
else:
    opener = urllib2.build_opener(null_proxy_handler)
urllib2.install_opener(opener)

#设置timeout解决网站响应过慢的问题
import urllib2
#data为空时需要特别标注出timeout
response = urllib2.urlopen('http://www.baidu.com', timeout=10)
import urllib2
response = urllib2.urlopen('http://www.baidu.com',data, 10)

#使用http的put和delete方法
import urllib2
request = urllib2.Request(uri, data=data)
request.get_method = lambda: 'PUT'  # or 'DELETE'
response = urllib2.urlopen(request)

#DebugLog展示收发包的过程
import urllib2
httpHandler = urllib2.HTTPHandler(debuglevel=1)
httpsHandler = urllib2.HTTPSHandler(debuglevel=1)
opener = urllib2.build_opener(httpHandler, httpsHandler)
urllib2.install_opener(opener)
response = urllib2.urlopen('http://www.baidu.com')

#解决URLError
# 网络无连接，即本机无法上网
# 连接不到特定的服务器
# 服务器不存在
import urllib2
requset = urllib2.Request('http://www.xxxxx.com')
try:
    urllib2.urlopen(request)
except urllib2.URLError as e:
    print e.reason

#HTTPError
#     100：继续  客户端应当继续发送请求。客户端应当继续发送请求的剩余部分，或者如果请求已经完成，忽略这个响应。
#     101： 转换协议  在发送完这个响应最后的空行后，服务器将会切换到在Upgrade 消息头中定义的那些协议。只有在切换新的协议更有好处的时候才应该采取类似措施。
#     102：继续处理   由WebDAV（RFC 2518）扩展的状态码，代表处理将被继续执行。
#     200：请求成功      处理方式：获得响应的内容，进行处理
#     201：请求完成，结果是创建了新资源。新创建资源的URI可在响应的实体中得到    处理方式：爬虫中不会遇到
#     202：请求被接受，但处理尚未完成    处理方式：阻塞等待
#     204：服务器端已经实现了请求，但是没有返回新的信 息。如果客户是用户代理，则无须为此更新自身的文档视图。    处理方式：丢弃
#     300：该状态码不被HTTP/1.0的应用程序直接使用， 只是作为3XX类型回应的默认解释。存在多个可用的被请求资源。    处理方式：若程序中能够处理，则进行进一步处理，如果程序中不能处理，则丢弃
#     301：请求到的资源都会分配一个永久的URL，这样就可以在将来通过该URL来访问此资源    处理方式：重定向到分配的URL
#     302：请求到的资源在一个不同的URL处临时保存     处理方式：重定向到临时的URL
#     304：请求的资源未更新     处理方式：丢弃
#     400：非法请求     处理方式：丢弃
#     401：未授权     处理方式：丢弃
#     403：禁止     处理方式：丢弃
#     404：没有找到     处理方式：丢弃
#     500：服务器内部错误  服务器遇到了一个未曾预料的状况，导致了它无法完成对请求的处理。一般来说，这个问题都会在服务器端的源代码出现错误时出现。
#     501：服务器无法识别  服务器不支持当前请求所需要的某个功能。当服务器无法识别请求的方法，并且无法支持其对任何资源的请求。
#     502：错误网关  作为网关或者代理工作的服务器尝试执行请求时，从上游服务器接收到无效的响应。
#     503：服务出错   由于临时的服务器维护或者过载，服务器当前无法处理请求。这个状况是临时的，并且将在一段时间以后恢复。
import urllib2
req = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(req)
except urllib2.HTTPError as  e:
    print e.code
    print e.reason

#cookie追踪session生成的加密数据
#opener概念   urlopen的一般形式，可以添加cookie
#Cookielib概念 提供可储存的cookie，用于登陆

#获取cookie保存到变量
import urllib import cookielib #声明一个CookieJar对象实例来保存cookie
cookie = cookielib.CookieJar()
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler=urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#此处的open方法同urllib2的urlopen方法，也可以传入request
response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name = '+item.name
    print 'Value = '+item.value

#保存Cookie到文件
import cookielib import urllib2
#设置保存cookie的文件，同级目录下的cookie.txt
filename = 'cookie.txt'
#声明一个MozillaCookieJar对象实例来保存cookie，之后写入文件
cookie = cookielib.MozillaCookieJar(filename)
#利用urllib2库的HTTPCookieProcessor对象来创建cookie处理器
handler = urllib2.HTTPCookieProcessor(cookie)
#通过handler来构建opener
opener = urllib2.build_opener(handler)
#创建一个请求，原理同urllib2的urlopen
response = opener.open("http://www.baidu.com")
#保存cookie到文件
cookie.save(ignore_discard=True, ignore_expires=True)

#从文件中获取Cookie并访问