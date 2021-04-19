import os
from sqlalchemy import create_engine, Table, Column, Float, Integer, String, MetaData
# from app import db
​
# # db.drop_all()
# db.create_all()
​
meta = MetaData()
​
connection = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"
​
print("connection to databse")
engine = create_engine(connection)
​
if not engine.has_table("pets"):
    print("Creating Table")
​
    new_table = Table(
        'electoral_division', meta,
        Column('state', String),
        Column('electoral_division', String),
        Column('division_id', Integer, primary_key=True),
    )
​
    meta.create_all(engine)
​
    print("Table created")
​
    seed_data = [
        {"state": "SA", "electoral_division": "Adelaide", "division_id": "179"}, 
    ]
​
    with engine.connect() as conn:
        conn.execute(new_table.insert(), seed_data)
​
    print("Seed Data Imported")
else:
    print("Table already exists")
print("initdb complete")