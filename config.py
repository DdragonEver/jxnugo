#-*- coding: UTF-8 -*-
import os
basedir=os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY=os.environ.get('SECRET_KEY') or 'the string was hard to guess'
    SQLALCHEMY_COMMIT_ON_TEARDOWN=True
    JXNUGO_MAIL_SUBJECT_PREFIX='[JxnuGo]'
    JXNUGO_MAIL_SENDER='JXNUGO Admin <jxnugo@163.com>'
    JXNUGO_ADMIN='jxnugo@163.com'
    SQLALCHEMY_DATABASE_URI= 'mysql://root:laidaolong@localhost:3306/jxnugo'
    @staticmethod
    def init_app(app):
        pass

class DevelopmentConfig(Config):
    DEBUG=True
    MAIL_SERVER='smtp.163.com'
    MAIL_PORT='25'
    MAIL_USE_TLS=True
    MAIL_USERNAME='jxnugo@163.com'
    MAIL_PASSWORD='ldlmecon419'
    SQLALCHEMY_DATABASE_URL='mysql://root:laidaolong@localhost:3306/jxnugo'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

class TestingConfig(Config):
    TESTING=True
    SQLALCHEMY_DATABASE_URL='mysql://root:laidaolong@localhost:3306/jxnugo'



class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URL='mysql://root:laidaolong@localhost:3306/jxnugo'


config={
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default':DevelopmentConfig

}