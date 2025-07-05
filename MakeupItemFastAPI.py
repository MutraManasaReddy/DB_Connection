import uvicorn
from fastapi import FastAPI
import mysql .connector

app = FastAPI()

class Makeupitem:
    def __init__(self, hairdryer:str, color:str, brand:str):
        self.hairdryer = hairdryer,
        self.color = color,
        self.brand = brand
        pass
    def __repr__(self):
        return f"Makeupitem(hairdryer ={self.hairdryer}, color ={self.color}, brand ={self.brand})"
        pass

Makeupitem_list = []
db = mysql.connector.connect(
    host = "localhost",
    username = "root",
    password ="Manasa@123"
)

mycursor = db.cursor

#mycursor.execute("CREATE DATABASE MAKEUPITEM")
#print(db)

#mycursor.execute("CREATE TABLE makeupitemdata(hairdryer VARCHAR(220), color VARCHAR(222), brand VARCHAR(224))")
#mycursor.execute("SHOW TABLE")
#for x in mycursor:
 #   print(x)

@app.get("/")
def read_root():
    return{"message":"makeupiten API"}


@app.post("/create_makeupitem/")
def add_makeupitem(hairdryer: str, color: str, brand: str):
    sql = "INSERT INTO makeupitems(hairdryer, color, brand) VALUES(%s,%s,%s)"
    val = ("hairdryer","color","brand")
    mycursor.execute(sql,val)
    db.commit()
    mycursor.execute("SELETE * FROM makeupiten WHERE hairdryer = %s",(hairdryer,))
    create_makeupitem = mycursor.fetchall()
    return create_makeupitem

@app.get("/list_makeupitem/")
def list_makeupitem():
    mycursor.execute("SELETE * FROM makeupites")
    list_of_makeupitem = mycursor.fetchall()
    return list_of_makeupitem

@app.get("/makeupitem_deatils/{hairdryer}")
def get_makeupitem(hairdryer: str): 
    mycursor.exxecute("SELECT * FROM  makeupitemdata WHERE hairdryer = %s",(hairdryer,))
    result = mycursor.fetchall()
    return result

@app.patch("/update_makeupitem/{hairdryer}")
def update_makeupitem(hairdryer : str, color:str = None, brand: str = None):
    makeupitem = get_makeupitem(color)
    if not makeupitem:
        return {"makeupitem is not found"}
    if color:
        sql = "UPDATE makeupitem SET hairdryer  = %s WHERE hairdryer = %s"
        val = color,hairdryer
        mycursor.execute(sql,val)
        db.commit()
    if brand:
        sql = "UPDATE makeupitem SET brand = %s WHERE hairdryer = %s"
        val = brand , hairdryer
        mycursor.execute(sql,val)
        db.commit()
    mycursor.execute("SELECT * FROM makeupitem  WHERE  hairdryer = %s", (hairdryer,))
    update_makeupitem = mycursor.fetchall()
    return update_makeupitem

@app.delete("/delete makeupitem/{hairdryer}")
def delete_makeupitem(hairdryer : str):
    mycursor.execute("DELETE FROM makeupitem WHERE  hairdryer = %s", (hairdryer,))
    db.commit()
    return{"makeupitem is delete"}




