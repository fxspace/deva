

from .stream import Stream,namespace
from tornado.ioloop import IOLoop

def create_cps(stream_name,**kwargs):
    namespace[stream_name]=Stream.from_share(stream_name,**kwargs)
    namespace[stream_name].emit = Stream().to_share(stream_name).emit
    return namespace[stream_name]
    


bus = create_cps('bus',cache_max_len=1)

bus.__doc__ = """
    跨进程的消息流任务驱动


@bus.route(lambda x:type(x)==str)
def foo(x):
    x*2>>log


'aa'>>pbus
如果是单独进程中使用,需要固定一个循环来hold主线程
from tornado import ioloop
ioloop.IOLoop.current().start()

"""
