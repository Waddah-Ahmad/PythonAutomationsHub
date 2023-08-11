
# Project: Automated test receiving Email

"""
Description: Checking if you received an email within a minute involves interacting with your email server's IMAP (Internet Message Access Protocol) to fetch the latest emails and check their timestamps.
Below is a script that uses the imaplib library in Python to connect to an IMAP server and check if you have received any new emails within the last minute:
"""
import imaplib
import email
from datetime import datetime, timedelta
import time

def check_email_within_timeframe(email_address, password, imap_server, timeframe_minutes):
    try:
        mail = imaplib.IMAP4_SSL(imap_server)
        mail.login(email_address, password)
        mail.select("inbox")

        since_time = datetime.now() - timedelta(minutes=timeframe_minutes)
        since_time_str = since_time.strftime("%d-%b-%Y %H:%M:%S")
        
        result, data = mail.search(None, f'(SINCE "{since_time_str}")')
        if result == 'OK':
            email_ids = data[0].split()
            if email_ids:
                return True
            else:
                return False

    except Exception as e:
        print("An error occurred:", e)
        return False
    finally:
        mail.logout()

if __name__ == "__main__":
    email_address = "your_email@example.com"  # Replace with your email address
    password = "your_email_password"  # Replace with your email password
    imap_server = "imap.example.com"  # Replace with your IMAP server address
    timeframe_minutes = 1

    received_within_timeframe = check_email_within_timeframe(email_address, password, imap_server, timeframe_minutes)
    if received_within_timeframe:
        print("You have received an email within the last minute.")
    else:
        print("No new emails received within the last minute.")