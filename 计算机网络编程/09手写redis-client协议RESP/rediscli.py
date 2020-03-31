# coding:utf8

# redis-client模型抽象
# api-Client  <-   Protocol(Resp协议)   <-   Connection

# RESP协议在redis中用作请求-响应协议的方式如下：
# 1、客户端将命令作为字符串数组发送到Redis服务器
# 2、服务器根据命令实现回复一种RESP类型数据

# 在RESP中，一些数据的类型通过他的第一个字节进行判断
# 1、单行回复：回复的第一个字节是"+"
# 2、错误信息：回复的第一个字节是"-"
# 3、整型数字：回复的第一个字节是":"
# 4、多行字符串：回复的第一个字节是"$"
# 5、数组：回复的第一个字节是"*"
# 此外，RESP能够使用稍微指定的Bulk Strings或Array的特殊变体来表示Null值
# 在RESP中，协议的不同部分始终以"\r\n"(CRLF)结束
# 具体文档:https://redis.io/topics/protocol

from redis import Redis

conn = Redis(**{
    'host': '127.0.0.1',
    'port': '6379'
})

# conn.set('name', 'test')


# *3    代表数组长度为3，代表当前参数的长度

# $3    |第一组，字符串长度为3
# SET   |

# $4    |第二组，字符串长度为4
# name  |

# $4    |第三组，字符串长度为4
# test  |


conn.set('name', 'test2', 'NX')

# *5

# $3
# SET

# $4
# name

# $5
# test2

# $2
# EX

# $2
# NX