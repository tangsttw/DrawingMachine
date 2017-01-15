from main_program import app
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
app.config['SECRET_KEY'] = "random string"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///items.db'

db = SQLAlchemy(app)

class items(db.Model):
    __tablename__ = 'items'
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    group_name = db.Column(db.String(50))


    def __init__(self, name, group_name):
        self.name = name
        self.group_name = group_name

class draw_histories(db.Model):
    __tablename__ = 'draw_histories'
    draw_histories_id = db.Column('draw_histories_id', db.Integer, primary_key=True)
    itemid = db.Column(db.Integer, db.ForeignKey('items.id'))
    time = db.Column(db.DATETIME, default=datetime.now)
    item = db.relationship('items', foreign_keys=itemid)

def showData(selectGroup_name):
    if selectGroup_name == 'ALL' or selectGroup_name is None:
        selectitems = items.query.all()
    else:
        selectitems = items.query.filter_by(group_name=selectGroup_name).all()
    return selectitems


def addData(n, g_name):
    if n is not None or g_name is not None:
        item = items(name=n, group_name=g_name)
        print(item.name, '+', item.group_name)
        db.session.add(item)
        db.session.commit()


def deleteData(select_name):
    item = items.query.filter_by(name=select_name)

    # two way to delete record
    # db.session.query(items).filter(items.name == item[0].name).delete()
    db.session.query(items).filter_by(name=item[0].name).delete()
    db.session.commit()


def updateData(n, g_name):
    item = items.query.filter_by(name=n)
    # db.session.query(items).filter(items.name == item[0].name).update({'group_name': request.form.get('group_name')})
    db.session.query(items).filter_by(name=item[0].name).update({"group_name": g_name})
    db.session.commit()

def showHistories():
    histories = draw_histories.query.all()
    return histories

def getDataById(mId):
    if mId == 'ALL' or mId is None:
        selectitems = items.query.all()
    else:
        selectitems = items.query.filter_by(
            id=mId).all()
    return selectitems

def addHistory(m):
    if m is not None:
        drawHistory = draw_histories(itemid=m[0].id)
        db.session.add(drawHistory)
        db.session.commit()
