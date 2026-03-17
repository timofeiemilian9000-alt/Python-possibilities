username = "GiovannyVP"
password = "Safety1st!"
locked = False
attempt = "Safety1st!"
code_sent = 836027  
code_entered = 836027

unlocked = locked == False
attempt_ok = attempt == password
code_ok = code_sent == code_entered
login_success = unlocked and attempt_ok and code_ok

if login_success:
    print("Login successful!")
else: 
    print("Login failed!")