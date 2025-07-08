import json
import time
import os

LOCK_FILE = 'data/lock.json'
USERNAME = 'admin'
PASSWORD = 'admin'
MAX_TRY = 3
LOCK_DURATION = 300

def load_lock_data():
    if os.path.exists(LOCK_FILE):
        with open(LOCK_FILE,'r') as f:
            try:
                return json.load(f)
            except json.JSONDecodeError:
                return {'attempts': 0,'last_failed':0}
    else:
        return {'attempts': 0,'last_failed':0}

def save_lock_data(data):
    os.makedirs(os.path.dirname(LOCK_FILE),exist_ok=True)
    with open(LOCK_FILE,'w') as f:
        json.dump(data,f)



def islocked(lock_data):
    if lock_data['attempts'] >= MAX_TRY:
        elapsed = time.time() - lock_data['last_failed']
        if elapsed < LOCK_DURATION:
            remaining = int(LOCK_DURATION - elapsed)
            print(f"Too many attempts try again after {remaining} seconds")
            return True
        else:
            lock_data['last_failed'] = 0
            save_lock_data(lock_data)
    return False

def login():
    lock_data = load_lock_data()
    if islocked(lock_data):
        return
    username = input("Enter Username: ")
    password = input("Enter Password: ")
    if username == USERNAME and password == PASSWORD:
        print("Login sucessful")
        lock_data['attempts']=0
        save_lock_data(lock_data)
        return True
    else:
        print("Invalid")
        lock_data['attempts']+=1
        lock_data['last_failed']=time.time()
        save_lock_data(lock_data)
        if lock_data['attempts'] > MAX_TRY:
            print("Account blocked for 5 mins")
        return False
    

