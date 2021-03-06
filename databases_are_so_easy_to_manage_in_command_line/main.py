import sys
import peewee
import sqlite3
from models import *

my_models_db.connect()

args = ['create', 'print', 'insert', 'delete', 'print_batch_by_school', 'print_student_by_batch']

def create_tables():
    my_models_db.create_tables([School, Batch, User, Student])
    print "Creating all tables.."

def print_models():
    all_models = { 'school': School, 'batch': Batch, 'user': User, 'student': Student }
    if len(sys.argv) < 3:
        print "Format: print <model>"
    elif sys.argv[2] == 'student':
        row = all_models[sys.argv[2]].select()
        for i in row:
            batch_id = Batch.get()
            print "%s part of batch: %s" % (i, batch_id)
    else:
        row = all_models[sys.argv[2]].select()
        for i in row:
            print i

def insert():
    if len(sys.argv) < 3:
        print "Format: insert <model name> [Choices: school, batch, student]"
    else:
        if sys.argv[2] == 'school':
            if len(sys.argv) < 4:
                print "Format: school <name>"
            else:
                insert_new_school = School.create(name=sys.argv[3])
                print "New school: %s" % (insert_new_school)

        if sys.argv[2] == 'batch':
            if len(sys.argv) < 5:
                print "Format: batch <school id> <name> "
            else:
                insert_new_batch = Batch.create(school_id=sys.argv[3], name=sys.argv[4])
                print "New batch: %s" % (insert_new_batch)

        if sys.argv[2] == 'student':
            if len(sys.argv) < 6:
                print "Format: student <batch id> <age> <last_name> <first_name>"
            elif len(sys.argv) == 6:
                insert_new_student = Student.create(batch_id=sys.argv[3], age=sys.argv[4], last_name=sys.argv[5], first_name="")
                student_id = Batch.get()
                print "New student: %s part of the batch: %s" % (insert_new_student, student_id)
            else:
                insert_new_student = Student.create(batch_id=sys.argv[3], age=sys.argv[4], last_name=sys.argv[5], first_name=sys.argv[6])
                student_id = Batch.get()
                print "New student: %s part of the batch: %s" % (insert_new_student, student_id)


def delete():
    if len(sys.argv) < 3:
        print "Format: delete <model name> <id to object>"
    else:
        if sys.argv[2] == "school":
            if len(sys.argv) < 4:
                print "Format: delete <model name> <id to object>"
            else:
                try:
                    school = School.get(School.id == sys.argv[3])
                    School.delete_instance(school)
                    print "Delete: %s" % (school)
                except:
                    print "Nothing to delete"
        elif sys.argv[2] == "batch":
            if len(sys.argv) < 4:
                print "Format: delete <model name> <id to object>"
            else:
                try:
                    batch = Batch.get(Batch.id == sys.argv[3])
                    Batch.delete_instance(batch)
                    print "Delete: %s" % (batch)
                except:
                    print "Nothing to delete"
        elif sys.argv[2] == "student":
            if len(sys.argv) < 4:
                print "Format: delete <model name> <id to object>"
            else:
                try:
                    student = Student.get(Student.id == sys.argv[3])
                    batch = Batch.get()
                    Student.delete_instance(student)
                    print "Delete: %s part of the batch: %s" % (student, batch)
                except:
                    pass
                    print "Nothing to delete"

def batch_by_school():
    if len(sys.argv) < 3:
        print "Format: print_batch_by_school <school id>"

def student_by_batch():
    if len(sys.argv) < 3:
        print "Format: print_student_by_batch <batch id>"


'''
the second argument of your program should be a batch id
if your database doesn't contains a Batch with the batch id, your program should print Batch not found
your program should fetch from the DB all Student objects attached to this batch
print the list one object per line
'''

if len(sys.argv) < 2:
    print "Please enter an action: [Options: create, print, insert, delete, print_batch_by_school, print_student_by_batch]"
elif sys.argv[1] not in args:
    print "Undefined action %s" % sys.argv[1]
else:
    if sys.argv[1] == 'create':
        create_tables()
    elif sys.argv[1] == 'print':
        print_models()
    elif sys.argv[1] == 'insert':
        insert()
    elif sys.argv[1] == 'delete':
        delete()
    elif sys.argv[1] == 'print_batch_by_school':
        batch_by_school()
    elif sys.argv[1] == 'print_student_by_batch':
        student_by_batch()
