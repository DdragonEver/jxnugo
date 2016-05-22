# coding: utf-8
from flask.ext.script import Manager,Shell
from app import create_app, db
from app.models import Role, User, Post, Follow, bbsPost,collectionPosts
from flask.ext.migrate import Migrate, MigrateCommand
from dateutil import tz
from datetime import datetime

app = create_app()
manager = Manager(app)
migrate = Migrate(app, db)

@app.template_filter('changToUserAvatar')
def change(pid):
    return User.query.filter_by(id=pid).first().avatar
app.jinja_env.filters['changeToUserAvatar'] = change


@app.template_filter('changeToUserName')
def changeUserName(pid):
    return User.query.filter_by(id=pid).first().userName
app.jinja_env.filters['changeToUserName'] = changeUserName



@app.template_filter('utcChangeToCst')
def changeTime(utcTime):
    from_zone = tz.gettz('UTC')
    to_zone = tz.gettz('CST')
    utc =utcTime
    utc = utc.replace(tzinfo=from_zone)
    local = utc.astimezone(to_zone)
    return datetime.strftime(local, "%Y-%m-%d %H:%M:%S")
app.jinja_env.filters['utcChangeToCst'] = changeTime

@app.template_filter('getFirstKey')
def firstKey(keys):
    key=keys.split(":")
    return key[0]
app.jinja_env.filters['getFirstKey'] = firstKey





def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Post=Post, bbsPost=bbsPost, Follow=Follow,collectionPosts= collectionPosts)
manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
