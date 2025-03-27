import os
import pymysql
from urllib.request import urlopen
import subprocess
import re

db_config = {
    'host': os.getenv('DB_HOST'),
    'user': os.getenv('DB_USER'),
    'password': os.getenv('DB_PASSWORD')
}

import re

def get_user_input():
    user_input = input('Enter your name: ')
    if not re.match("^[a-zA-Z0-9_ -]+$", user_input):
        raise ValueError("Invalid input! Only letters, numbers, spaces, underscores, and hyphens are allowed.")
    return user_input


def send_email(to, subject, body):
    subprocess.run(["mail", "-s", subject, to], input=body, text=True)

def get_data():
    url = 'https://secure-api.com/get-data'
    data = urlopen(url).read().decode()
    return data

def save_to_db(data):
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()
    query = "INSERT INTO mytable (column1, column2) VALUES (%s, %s)"
    cursor.execute(query, (data, 'Another Value'))
    connection.commit()
    cursor.close()
    connection.close()


if __name__ == '__main__':
    user_input = get_user_input()
    data = get_data()
    save_to_db(data)
    send_email('admin@example.com', 'User Input', user_input)
