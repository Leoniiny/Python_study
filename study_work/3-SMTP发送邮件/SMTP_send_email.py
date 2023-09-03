import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage

'''
使用Python及SMTP协议发送邮件（以163邮箱为例)
一是尝试封装成类，和支持with上下文管理器
二是构建了text和mutli两种类型的邮件
三是实现抄送和独立出附件添加。

'''


class My163():
    def __init__(self):
        self._mail_host = "smtp.163.com"  # 163邮箱服务器地址
        self._mail_user = "Leiyangp@163.com"  # 163用户名
        self._mail_pass = "JNRHATTEFWFJWKTW"  # 密码（邮箱授权码）
        # self._smtpobj = smtplib.SMTP()  #根据是否ssl 认证进行二选一
        self._smtpObj = smtplib.SMTP_SSL(self._mail_host, port=465)  # 根据是否ssl 认证进行二选一

    def __enter__(self):
        print("Info: Enter my163....")
        try:
            # 链接服务器
            self._smtpObj.connect(host=self._mail_host, port=465)
            # 登录服务器
            rest = self._smtpObj.login(user=self._mail_user, password=self._mail_pass)
            print(f"登录的的结果为{rest}")
        except  smtplib.SMTPException as e:
            print('163 email login failed with error:%s' % e)
        finally:
            return self  # 注意enter里面一定要返回类的对象self,否则无法调用run方法。

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("INFO: Exit 163")
        self._smtpObj.quit()

    def email_send(self,to_address,msg):
        try:
            rest = self._smtpObj.sendmail(from_addr=self._mail_user,to_addrs=to_address,msg=str(msg))
            print(f'rest:{rest}')
            return True
        except Exception as e:
            print('163 email login failed with error:%s' % e)
            return  False

    def textmail_send(self,from_addr = 'Cameback_Tang',to_addrs=['1962560722@qq.com'],cc_addrs=[],bcc_addrs=[],subject='emailtitle',content='message Text'):
        msg = MIMEText(content,"plain",'utf-8')
        msg["Subject"] = subject
        msg['From'] = from_addr
        msg['To'] = ';'.join(to_addrs)
        msg['Cc'] = ';'.join(cc_addrs)
        msg['Bcc'] = ';'.join(bcc_addrs)
        addresses = to_addrs + cc_addrs + bcc_addrs
        return self.email_send(to_address = addresses,msg = msg)

    def _add_image_attatchment(self,multimsg,filepath,filenameInEmail = None):
        if os.path.exists(filepath):
            pass
        else:
            print(f"找不到附件见{filepath}")
            print(f"请将附件上传到项目目录")
            return multimsg

        if filenameInEmail:
            pass
        else:
            filenameInEmail = os.path.basename(filepath)

        with open(filepath,"rb") as fp:
            picture = MIMEImage(fp.read())


if __name__ == '__main__':
    A = My163()
    A.email_send()

