import mongoengine as mg
import datetime


class User(mg.Document):
    email = mg.StringField(max_length=200, required=True, unique=True)
    password = mg.StringField(max_length=256, required=True)
    ip = mg.StringField(max_length=200)
    added_at = mg.DateTimeField(default=datetime.datetime.utcnow)

    is_trial = mg.BooleanField(default=True)
    api_key = mg.StringField(max_length=256, required=True)
    successful_requests = mg.IntField(default=0)

    meta = {
        'indexes': [
            'email',
            'is_trial',
            'api_key',
            ('email', 'is_trial'),
            ('email', 'api_key'),
        ]
    }