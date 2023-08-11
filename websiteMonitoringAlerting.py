
# Project: Website Monitoring and Alerting

""" 
Description: This project automates the monitoring of a website's availability and performance. 
It sends periodic HTTP requests to the website and checks the response time and status code.
If the website is down or responding slowly, it sends an alert notification via email or other means.
"""

import requests
import smtplib
from email.message import EmailMessage
import time

def send_email_alert(sender_email, sender_password, receiver_email, subject, body):
    msg = EmailMessage()
    msg.set_content(body)

    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)
        smtp.send_message(msg)

def website_monitoring(url, response_time_threshold, status_code_threshold, sender_email, sender_password, receiver_email):
    while True:
        start_time = time.time()
        try:
            response = requests.get(url)
            response_time = time.time() - start_time
            status_code = response.status_code

            if response_time > response_time_threshold:
                alert_subject = f"Website Response Time Alert: {url}"
                alert_body = f"The response time for {url} is exceeding the threshold. Current response time: {response_time:.2f} seconds."
                send_email_alert(sender_email, sender_password, receiver_email, alert_subject, alert_body)

            if status_code != status_code_threshold:
                alert_subject = f"Website Status Code Alert: {url}"
                alert_body = f"The status code for {url} is {status_code}."
                send_email_alert(sender_email, sender_password, receiver_email, alert_subject, alert_body)

        except requests.exceptions.RequestException:
            alert_subject = f"Website Down Alert: {url}"
            alert_body = f"The website {url} is down or not responding."
            send_email_alert(sender_email, sender_password, receiver_email, alert_subject, alert_body)

        time.sleep(300)  # Check the website every 5 minutes

if __name__ == "__main__":
    website_url = "https://www.example.com"  # Replace with the URL of the website to monitor
    response_time_threshold = 2  # Set the maximum acceptable response time in seconds
    status_code_threshold = 200  # Set the expected status code for the website
    sender_email = "your_sender_email@gmail.com"  # Replace with your sender email
    sender_password = "your_sender_email_password"  # Replace with your sender email password
    receiver_email = "your_receiver_email@gmail.com"  # Replace with your receiver email

    website_monitoring(website_url, response_time_threshold, status_code_threshold, sender_email, sender_password, receiver_email)

