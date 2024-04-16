from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, select

# Step 1: Create a SQLite database engine
engine = create_engine('sqlite:///with_builder.db', echo=True)

# Step 2: Create a table
metadata = MetaData()
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer)
)
metadata.create_all(engine)

# Step 3: Insert data
with engine.connect() as conn:
    conn.execute(users.insert().values(name='Alice', age=30))
    conn.execute(users.insert().values(name='Bob', age=25))
    conn.commit()

# Step 4: Use a SQL builder to query data
with engine.connect() as conn:
    query = select(users.c.name, users.c.age)
    result = conn.execute(query)
    for row in result:
        print(row)
