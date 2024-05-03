from flask_mongoengine import MongoEngine
from mongoengine import DecimalField

# from mongoengine import Document, DateTimeField, StringField,ReferenceField,ListField
from datetime import datetime,timezone
import pytz

db = MongoEngine()
class User(db.Document):
    user_id = db.StringField(primarykey = True)
    user_name = db.StringField(required = True)
    logo =db.FileField()  #file field for storing images
    timestamp = db.DateTimeField(default=lambda: datetime.now(timezone.utc))

class Assistant_Gaian(db.Document):
    assistant_name = db.StringField(required = True,primarykey = True)
    assistant_id = db.StringField(required = True,primarykey= True)
    created_timestamp = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    updation_timestamp = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    logo  =db.FileField() 

class Assistant_User(db.Document):
    user_id=db.StringField()
    assistant_user_id = db.StringField()
    assistant_user_name=db.StringField()
    timestamp = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    updated_timestamp=db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    logo = db.StringField()

    
class Thread(db.Document):
    user_id =db.StringField()
    assistant_id =db.StringField()
    thread_id =db.StringField(required=True)
    timestamp = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    title =db.StringField()

class Payment(db.Document):
    user_id =db.StringField()
    assistant_id =db.StringField()
    thread_id =db.StringField(required=True)
    token_consumed = db.IntField()
    unit_price = db.IntField()
    total_price = db.IntField()
    timestamp = db.DateTimeField(default=lambda: datetime.now(timezone.utc))

class Annotations(db.Document):
    assistant_id = db.StringField(required = True,primarykey= True)
    annotations_name = db.StringField(required = True)
    parameters = db.StringField()
    created_timestamp = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
    updation_timestamp = db.DateTimeField(default=lambda: datetime.now(timezone.utc))
'''This collection is used for storing user credentials data'''
class UserCredentials(db.Document):
    username = db.StringField(required=True, unique=True)
    password = db.StringField(required=True)
    created_timestamp = db.DateTimeField(default=lambda: datetime.now(timezone.utc))

'''This collection is used for storing tokens consumed'''
class Tokens(db.Document):
    user_id = db.StringField(default ='xyz')
    total_tokens = db.IntField(required=True)
    timestamp = db.DateTimeField(default=lambda: datetime.now(timezone.utc))