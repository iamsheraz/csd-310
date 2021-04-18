#Muhammad Tariq
#April 17th, 2021
#A 6.2 Pytech_update

import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.x0xge.mongodb.net/pytech?retryWrites=true&w=majority")
db = client.pytech
collection = db.students

docs = collection.find({})

print(" -- DISPLAYING STUDENTS DOCUMENT FROM find() QUERY -- ")
for doc in docs:
    print(f" Student ID: {doc['student_id']} \n First Name: {doc['first_name']} \n Last Name: {doc['last_name']}\n")

updateDoc = collection.update_one({"student_id": 1007},{"$set":{"last_name":"carlos"}})

newDoc = collection.find_one({"student_id": 1007})

print("\n -- DISPLAYING STUDENT DOCUMENT update_one() QUERY: STUDENT_ID: 1007\n")

print(f" Student ID: {newDoc['student_id']} \n First Name: {newDoc['first_name']} \n Last Name: {newDoc['last_name']}\n")
