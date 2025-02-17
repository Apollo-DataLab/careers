import pymysql
import os

timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db="defaultdb",
    host=os.environ['db_host'],
    password=os.environ['db_password'],
    read_timeout=timeout,
    port=26638,
    user=os.environ['db_user'],
    write_timeout=timeout,
)
    
cursor = connection.cursor()

def load_jobs_from_db():
  cursor.execute("SELECT * FROM jobs")
  results=cursor.fetchall()
  return results

def load_job_from_db(id):
  cursor.execute("SELECT * FROM jobs WHERE id = %s", id)
  results=cursor.fetchall()
  return results

def add_application_to_db(job_id, data):


