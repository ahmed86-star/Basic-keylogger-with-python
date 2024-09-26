# Basic-keylogger-with-python

![keylogger](https://github.com/ahmed86-star/Basic-keylogger-with-python/assets/113064932/34d9724d-2785-49ee-8725-7e8e4471e3ae)


# Python Keylogger

A **keylogger** is a type of software that records and captures the keys pressed on a computer keyboard. It runs silently in the background, monitoring and logging every keystroke made on the keyboard without the user's knowledge.

This Python keylogger leverages the `pynput` library to detect and capture keyboard events, such as when a key is pressed or released. It records the captured keystrokes and stores them in a text file. Optionally, the recorded data can be sent to an email address via `smtplib` using secure SSL.

## Features
- Logs all keypresses including special keys like **Enter**, **Backspace**, and **Tab**.
- Runs in the background.
- Sends the keylog via email after the user exits the logger.
- Customizable email configuration for sending logs securely.


  ![image](https://github.com/user-attachments/assets/3885661f-b1c8-43fa-a2b0-3218950fcbd7)


## Installation

To get started, you'll need to install the required libraries. While Python comes with `smtplib` and `ssl` pre-installed, you'll need to install `pynput` separately:

```bash
pip install pynput
```

## Usage

1. Clone or download the repository to your local machine.
2. Open the script file and update the following variables with your email details:
   - **`sender_mail`**: Your email address.
   - **`receiver_mail`**: The recipient email (can be the same as the sender).
   - **`password`**: Your email account password or app-specific password.
   
3. Run the script using Python:

```bash
python keylogger.py
```

4. Press the `ESC` key to exit the keylogger.

**Note**: Ensure your email service provider allows sending emails via SMTP. If you're using Gmail, you may need to enable "Less Secure Apps" or use an app-specific password.

## Code Overview

This keylogger script:
1. Captures keystrokes using the `pynput` library.
2. Writes the recorded keys to a file (`keylogger.txt`).
3. Sends the logged keystrokes via email using `smtplib` and `ssl` when the program exits.
4. The keylogger stops when the `ESC` key is pressed.

### Command to Run:
```bash
python keylogger.py
```

## Requirements

- Python 3.x
- `pynput` library for capturing keystrokes:
  ```bash
  pip install pynput
  ```
- Internet access to send emails.

## Important Notes

- **This keylogger is for educational purposes only.** Please use it responsibly and ethically. Running keyloggers without consent is illegal and unethical.
- The script works with any email provider that supports SMTP (e.g., Gmail, Yahoo, Outlook).
- The `ESC` key is used to stop the keylogger, so remember to press it to terminate the process.
