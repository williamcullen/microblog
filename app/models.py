# _*_ encoding:utf-8 _*_
__author__ = 'williamcullen'
__date__ = '2017/7/9 16:02'

from app import db


ROLE_USER = 0
ROLE_ADMIN = 1


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(64), unique=True)
    email = db.Column(db.String(120), unique=True)
    role = db.Column(db.Integer, default=ROLE_USER)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    # def is_authenticated(self):
    #     return True

    is_authenticated = True

    is_active = True

    is_anonymous = True

    def get_id(self):
        try:
            return unicode(self.id)  # python 2
        except NameError:
            return str(self.id)  # python 3

    def __repr__(self):
        return '<User %r>' % (self.nickname)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return '<Post %r>' % (self.body)
