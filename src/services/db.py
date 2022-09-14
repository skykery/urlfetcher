from models.db import User


class DatabaseService:
    alias = 'urlworker'

    @classmethod
    def connect(cls):
        from mongoengine import connect
        connect(cls.alias, host='mongodb')

    @classmethod
    def disconnect(cls):
        from mongoengine import disconnect
        disconnect(cls.alias)

    @classmethod
    def get_user(cls, key):
        cls.connect()
        try:
            user = User.objects.only('id').get(api_key=key)
        except User.DoesNotExist:
            user = None
        cls.disconnect()
        return user

    @classmethod
    def make_test_user(cls):
        cls.connect()
        user = User(email='doingmagic@randomemail.com', password='test', api_key='test')
        user.save()
        cls.disconnect()

    @classmethod
    async def increase_number_of_requests(cls, user_id):
        # BlogPost.objects(id=post.id).update_one(inc__page_views=1)
        print(user_id)
        User.objects(id=user_id).update_one(inc__successful_requests=1)
