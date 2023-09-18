from flask_test1 import app,db
import flask_test1
app.app_context().push()
db.create_all()
item1=flask_test1.Item(name='redmi',price='13000',barcode='23432566',description='#')
db.session.add(item1)
db.session.commit()
item2=flask_test1.Item(name='samsung',price='250000',barcode='23435456',description='##')
db.session.add(item2)
db.session.commit()
item3=flask_test1.Item(name='realme',price='17000',barcode='1223245',description='3##')
db.session.add(item3)
db.session.commit()
