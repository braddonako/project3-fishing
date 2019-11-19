from peewee import *

DATABASE = SqliteDatabase('fish.sqlite')

class User(Model):
    email = CharField(unique=True)
    password = CharField()
    nickname = CharField()

    class Meta: 
        db_table = 'users'
        database = DATABASE

class Post(Model):
    img = CharField()
    nameOfFish = CharField()
    description = CharField()
    gear = CharField()

    class Meta:
        db_table ='posts'
        database = DATABASE

# class River(Model):
#     nameOfRiver = CharField()
#     location = CharField()



def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User, Post], safe=True)
    print('Tables created')
    DATABASE.close()