# -*- encoding: utf-8 -*-
import base64
import os
import smtplib
from Core.ConfigOperation import ConfigOperation
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from Utils.Log import log


class Mail(object):
    def __init__(self, ssl=True):
        """
        Constructor Method
        :param ssl: Whether need ssl login.
        """
        self.config = ConfigOperation.load_config('./Core/config.ini')
        # 用户名
        self.username = self.config.get('Mail', 'mail_sender')
        # 密码
        self.password = self.config.get('Mail', 'mail_password')
        # 收件人，多个要传list ['a@qq.com','b@qq.com]
        self.recv = self.config.get('Mail', 'mail_receiver').split(',')
        # smtp服务器地址
        self.email_host = self.config.get('Mail', 'mail_host')
        # 普通端口
        self.port = self.config.get('Mail', 'mail_port')
        # 是否安全链接
        self.ssl = ssl
        # 收件人列表
        self.receiver = self.recv
        # 抄送人列表
        try:
            self.cc = self.config.get('Mail', 'mail_cc').split(',')
        except KeyError as error:
            self.cc = []
            log('No mail cc property.')

        if self.cc is not None and self.cc != []:
            self.receiver += self.cc

        # 安全链接端口
        self.ssl_port = self.config.get('Mail', 'mail_ssl_port')
        # 图片ID
        self.image_id = '0'

        # 根据SSL类型，创建SMTP链接
        if self.ssl:
            self.smtp = smtplib.SMTP_SSL(self.email_host, port=self.ssl_port)
        else:
            self.smtp = smtplib.SMTP(self.email_host, port=self.port)
        # 设置SMTP debug等级
        self.smtp.set_debuglevel(0)

    def send_mail(self, title, content, img_path=None, file_path=None):
        """
        Generate mail according to attachments.
        :param title: mail title
        :param content: mail content
        :param img_path: the path of mail attachment of summary image
        :param file_path: the path of mail attachment of test scenario details file
        """
        # 创建要发送的邮件正文及附件
        # related 使用邮件内嵌资源，可以把附件中的图片等附件嵌入到正文中
        msg = MIMEMultipart()

        # 设置邮件正文
        msg_text = MIMEText(content, 'html', 'utf-8')
        msg.attach(msg_text)

        if img_path is not None:
            self.__img_attach_content_converter__(msg, img_path, self.image_id)

        if file_path is not None:
            self.__file_attachment_handler__(msg, file_path)

        self.__set_email_properties__(msg, title)

        self.__smtp_handler__(msg)

    @staticmethod
    def __img_attach_content_converter__(msg, img_path, img_id):
        """
        Converter image to mail attachment.
        :param img_path: image path
        :param img_id: image id in mail html
        :return:
        """
        with open(img_path, 'rb') as img_content:
            msg_img = MIMEImage(img_content.read())

        msg_img.add_header('Content-ID', img_id)

        # 添加邮件正文，嵌入图片
        msg.attach(msg_img)

    @staticmethod
    def __file_attachment_handler__(msg, file_path_list):
        # 发送内容的对象
        if file_path_list:  # 处理附件的
            for file_path in file_path_list:
                file_name = os.path.split(file_path)[-1]  # 只取文件名，不取路径
                try:
                    f = open(file_path, 'rb').read()
                except Exception as e:
                    raise Exception('附件打不开！！！！')
                else:
                    att = MIMEText(f, "base64", "utf-8")
                    att["Content-Type"] = 'application/octet-stream'
                    # base64.b64encode(file_name.encode()).decode()
                    new_file_name = '=?utf-8?b?' + base64.b64encode(file_name.encode()).decode() + '?='
                    # 这里是处理文件名为中文名的，必须这么写
                    att["Content-Disposition"] = 'attachment; filename="%s"' % new_file_name
                    msg.attach(att)

    def __set_email_properties__(self, msg, title):
        msg['Subject'] = title  # 邮件主题
        msg['From'] = self.username  # 发送者账号
        msg['To'] = ','.join(self.recv)  # 接收者账号列表
        msg['Cc'] = ','.join(self.cc)

    def __smtp_handler__(self, msg):
        # 发送邮件服务器的对象
        try:
            self.smtp.login(self.username, self.password)
            result = self.smtp.sendmail(self.username, self.receiver, msg.as_string())
            log(result)
        except smtplib.SMTPAuthenticationError as e:
            if str(e).__contains__('535'):
                log('Mail Error: authentication failed, please check your username and password')
        except Exception as e:
            log(str(e))
            log('邮件发送失败！')
        else:
            log('The mail has sent successfully.')
        self.smtp.quit()
