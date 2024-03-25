from spyne import ServiceBase, rpc, Integer, Application
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from math import gcd

class ImageService(ServiceBase):
    @rpc(Integer, Integer, _returns=Integer)
    def calculate_mdc(ctx, width, height):
        return gcd(width, height)

application = Application([ImageService],
                          tns='http://tempuri.org/',
                          in_protocol=Soap11(validator='lxml'),
                          out_protocol=Soap11())

if __name__ == '__main__':
    wsgi_application = WsgiApplication(application)
    from wsgiref.simple_server import make_server
    server = make_server('0.0.0.0', 8000, wsgi_application)
    server.serve_forever()
