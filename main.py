import mysql.connector

# First init the connection
connection = mysql.connector.connect(
    host="localhost",
    user="root",
    # password="root",
    database="mysqltestdb"
)
# print(connection)

# Secondly init the executor [cursor]
cursor = connection.cursor()

# Create a db then add it to the connection object
# cursor.execute("CREATE DATABASE IF NOT EXISTS mysqltestdb")

# Create a tables then add it to the connection object
# cursor.execute("CREATE TABLE IF NOT EXISTS person (id INT PRIMARY KEY, name VARCHAR(64), email VARCHAR(64))")
# cursor.execute("CREATE TABLE IF NOT EXISTS thing (id INT PRIMARY KEY, name VARCHAR(64), description VARCHAR(256))")

# Big table
# cursor.execute(
#     """
#     CREATE TABLE IF NOT EXISTS ownership (
#         person INT,
#         thing INT,
#         FOREIGN KEY (person) REFERENCES person(id),
#         FOREIGN KEY (thing) REFERENCES thing(id)
#     );
# """)

# Show tables
# cursor.execute("SHOW TABLES")
# for table in cursor:
#     print(table)


# Insert data into the person table
# cursor.execute("""
# INSERT INTO person (id ,name, email) VALUES
#     (1,"Amr", "amr@amr"),
#     (2,"Ali", "ali@ali"),
#     (3,"Hassan", "hassan@hassan")
# """)
#
# # Insert data into the thing table
# cursor.execute("""
# INSERT INTO thing (id,name, description) VALUES
#     (1,"thing1", "description1"),
#     (2,"thing2", "description2"),
#     (3,"thing3", "description3")
# """)
#
# # Insert data into the ownership table
# cursor.execute("""
# INSERT INTO ownership (person, thing) VALUES
#     (2, 1),
#     (2, 3),
#     (1, 2)
# """)


class Person:
    def __init__(self, _id=None, _name=None, _email=None):
        self.id = _id
        self.name = _name
        self.email = _email

    def print_info(self):
        if self.id is None or self.name is None or self.email is None:
            print("Error: Person object is not initialized correctly")
            return
        print(self.id, self.name, self.email)

    # @staticmethod
    def from_result(self,result):
        self.id = result[0]
        self.name = result[1]
        self.email = result[2]
        return self

    def to_database(self, cursor):
        #! NOT RECOMMENDED TO USE THIS METHOD

        cursor.execute(f"INSERT INTO person (id, name, email) VALUES ({self.id}, '{self.name}', '{self.email}')")

#! Add data to person in database, NOT RECOMMENDED
# person2 = Person(15, "Alaamer", "amrsds@amr")
# person2.to_database(cursor)

# High injection vulnerability
# danger_person = Person(13, "Alaamer", "alsdsdaamer@amr' OR '1'='1")
# danger_person.to_database(cursor)
# danger_person2 = Person(14, "Alaamsdser'); DROP DATABASE mysqltestdb; --", "alaamerassd@amr")
# danger_person2.to_database(cursor)

# Fetch data from person
cursor.execute("SELECT * FROM mysqltestdb.person;")
results = cursor.fetchall()

# for row in results:
#     print(row)
#     person = Person()
#     person.from_result(row)
#     person.print_info()
#
connection.commit()