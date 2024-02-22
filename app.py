import pymysql
from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}


@app.get("/conn")
####Connection to my sql server.
def create_connection():
    connection=pymysql.connect(
    host='mysql-de1c02f-ivychebet17-bd73.a.aivencloud.com',
    user='avnadmin',
    password='AVNS_ZC3ZpL1x2bXlbaTIWcP',
    database = 'Abdi2',
    port =26266
)

    cursor = connection.cursor()
    show_table_query="SELECT * FROM students1"
    cursor.execute(show_table_query)

# Fetch all rows
    data = cursor.fetchall()
    return(data)



@app.get("/table2")
def create_connection1():
    data = create_connection()
    return {data}
        
    # Your logic to read data goes here



 
    
