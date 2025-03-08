import peewee

from fme.paths import paths


database = peewee.SqliteDatabase(paths.math_search_database)


class BaseModel(peewee.Model):

    class Meta:

        database = database


class Entry(BaseModel):

    name = peewee.TextField(index = True)
    type = peewee.TextField(index = True)
    content = peewee.TextField()


class Alias(BaseModel):

    alias = peewee.TextField(index = True)
    name = peewee.TextField()


paths.math_search_database.ensure_parent()
tables = [Entry, Alias]
database.drop_tables(tables)
database.create_tables(tables)
