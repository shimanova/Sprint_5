import time

def generate_unique_email():
    return f"test_user_{int(time.time() * 1000)}@test.ru"