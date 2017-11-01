# coding=utf-8

from multiprocessing import cpu_count
import gevent.monkey

gevent.monkey.patch_all()

bind = '0.0.0.0:8000'  # 绑定的ip及端口号
workers = cpu_count() * 2 + 1  # 进程数
max_requests = 1000
backlog = 2048  # 监听队列
worker_class = "gevent"  # 使用gevent模式，还可以使用sync 模式，默认的是sync模式
debug = True
proc_name = 'labman'
timeout = 120
