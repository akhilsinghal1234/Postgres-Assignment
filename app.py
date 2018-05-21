import random
import psycopg2
import names


def populate():
    courses = [i for i in range(0, 10)]
    students = [i for i in range(0, 100)]
    faculty = [i for i in range(0, 100)]

    conn = psycopg2.connect(database="postgres", user="postgres", password="postgres", host="127.0.0.1", port="5432")
    cur = conn.cursor()

    cur.execute('DROP TABLE IF EXISTS COURSES')
    cur.execute('DROP TABLE IF EXISTS STUDENTS')
    cur.execute('DROP TABLE IF EXISTS FACULTY')
    cur.execute("CREATE TABLE IF NOT EXISTS COURSES (CID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS STUDENTS (SID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, AGE INT NOT NULL)")
    cur.execute("CREATE TABLE IF NOT EXISTS FACULTY (FID INT PRIMARY KEY NOT NULL, NAME TEXT NOT NULL, FIELD TEXT NOT NULL)")
    for i in courses:
        j = random.randint(0,4)
        pre = ['CSE', 'EE', 'ME', 'CE', 'IC']
        name = pre[j] + str(i)
        cur.execute("INSERT INTO COURSES (CID, NAME) VALUES (" + str(i) + ", '" + name + "')")
    for i in students:
        name = names.get_full_name()
        age = random.randint(18, 25)
        cur.execute("INSERT INTO STUDENTS (SID, NAME, AGE) VALUES (" + str(i) + ", '" + name + "', " + str(age) + ")")
    for i in faculty:
        name = names.get_full_name()
        j = random.randint(0,3)
        field = ['CSE', 'EE', 'ME', 'CE']
        cur.execute("INSERT INTO FACULTY (FID, NAME, FIELD) VALUES (" + str(i) + ", '" + name + "', '" + str(field[j]) + "')")
    conn.commit()
    conn.close()

if __name__ == '__main__':
    populate()



# Some expensive Queries to test 
# SELECT COURSES.NAME, STUDENTS.NAME FROM COURSES, STUDENTS;
# SELECT COURSES.NAME, STUDENTS.NAME, STUDENTS.AGE, FACULTY.NAME, FACULTY.FIELD FROM COURSES, STUDENTS, FACULTY LIMIT 500000;

# Get rejected if queried again within 30s and execution time greater than 5s.  