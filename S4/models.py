from peewee import SqliteDatabase, Model, CharField

db = SqliteDatabase('permissions.db')

class Permission(Model):
    name = CharField(max_length=100, unique=True, null=False, verbose_name="Название разрешения")
    resource = CharField(max_length=100, null=False, verbose_name="Ресурс")
    action = CharField(max_length=50, null=False, verbose_name="Действие")
    description = CharField(max_length=255, null=False, default='', verbose_name="Описание")

    class Meta:
        database = db
        table_name = 'permissions'

def init_db():
    db.connect()
    db.create_tables([Permission], safe=True)
    db.close()