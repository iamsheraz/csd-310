import pymongo
from pymongo import MongoClient


client = pymongo.MongoClient("mongodb+srv://admin:admin@cluster0.x0xge.mongodb.net/pytech?retryWrites=true&w=majority")
db = client.pytech
collection = db.students

user1 = {"student_id": 1007, "first_name": "Jhon", "last_name": "Cena", "enrollment": [{
    "term": "spring 2020", "gpa": 3.80, "start_date": "01/01/2020", "end_date": "06/15/2021", 
    "course_id": 112233}], "course": [{"course_id": 112233, "description": "CSD 310", "instructor":
     "chris soriano", "grade": "A"}]}

user1_id = collection.insert_one(user1).inserted_id

user2 = {"student_id": 1008, "first_name": "Dave", "last_name": "Batista", "enrollment": [{
    "term": "spring 2020", "gpa": 3.99, "start_date": "01/01/2020", "end_date": "06/15/2021", 
    "course_id": 112233}], "course": [{"course_id": 112233, "description": "CSD 310", "instructor":
     "chris soriano", "grade": "A"}]}

user2_id = collection.insert_one(user2).inserted_id

user3 = {"student_id": 1009, "first_name": "Peter", "last_name": "Parker", "enrollment": [{
    "term": "spring 2020", "gpa": 3.85, "start_date": "01/01/2020", "end_date": "06/15/2021", 
    "course_id": 112233}], "course": [{"course_id": 112233, "description": "CSD 310", "instructor":
     "chris soriano", "grade": "B"}]}

user3_id = collection.insert_one(user3).inserted_id


print(f'\nInserted student record Jhon Cena into the students collection with document_id {user1_id}')
print(f'Inserted student record Dave Batista into the students collection with document_id {user2_id}')
print(f'Inserted student record Peter Parker into the students collection with document_id {user3_id}\n')
