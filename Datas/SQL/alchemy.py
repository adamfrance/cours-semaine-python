""" from sqlalchemy import create_engine,text
engine = create_engine('sqlite:///books.db')
connection = engine.connect()

query = text("select * from books_sales")
result = connection.execute(query)



for row in result:
    print(row) """

from sqlalchemy import MetaData, Table, create_engine
from sqlalchemy.sql import select
engine = create_engine('sqlite:///books.db')

metadata = MetaData(engine)

voitures_table = Table('voitures', metadata, autoload = True)

connection = engine.connect()

insertVoiture1 = voitures_table.insert().values(
    marque_voiture='renault',
    prix='70.000'
)

connection.execute(insertVoiture1)