# coding=utf-8
from message.api import MessageService
# 基于thrift的python 模块
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol
from thrift.server import TServer

import smtplib
from email.mime.text import MIMEText
from email.header import Header

sender = '18206296783@163.com'
authCode = 'weishixin123'
class MessageServiceHandler:

    def sendMobileMessage(self, mobile, message):
        """
        Parameters:
         - mobile
         - message

        """
        print "sendMobileMessage, mobile:"+ mobile +", message:" + message
        return True

    def sendEmailMessage(self, email, message):
        self.message_ = """
        Parameters:
         - email
         - message

        """
        print "sendEmailMessage, email:" + email + ", message:" + message
        # 第一个参数：邮件内容，第二个参数：邮件类型，第三参数：字符编码
        messageObj = MIMEText(message, "plain", "utf-8")
        messageObj['From'] = sender
        messageObj['To'] = email
        messageObj['Subject'] = Header('慕课网微服务实践Demo邮件', 'utf-8')
        try:
            smtpObj = smtplib.SMTP('smtp.163.com')
            smtpObj.login(sender, authCode)
            smtpObj.sendmail(sender, [email], messageObj.as_string())
            print "send mail success"
            return True
        except smtplib.SMTPException, ex:
            print "send mail failed!"
            print ex
            return False

if __name__ == '__main__':
    handler = MessageServiceHandler()
    processor = MessageService.Processor(handler)
    transport = TSocket.TServerSocket("127.0.0.1", "9090")
    # 设置帧传输 方式，按照报文 一帧一帧地传输
    tfactory = TTransport.TFramedTransportFactory()
    # 设置使用二进制的传输协议
    pfactory = TBinaryProtocol.TBinaryProtocolFactory()

    # 第一个参数 是谁实现了我的具体服务，processor封装了刚刚定义的handler
    # 第二个参数 是 谁负责监听网络请求,端口
    # 第三个参数 是 传输的方式
    # 第四个参数 是 传输的协议
    server = TServer.TSimpleServer(processor, transport, tfactory, pfactory)
    print "python thrift server start"
    server.serve()
    print "python thrift server exit"
