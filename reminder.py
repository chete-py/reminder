import os
import smtplib
from email.message import EmailMessage
from email.utils import formataddr
from pathlib import Path
from flask import Flask, render_template, request, flash


app = Flask(__name__)
app.secret_key = '002supersecretkey'

from dotenv import load_dotenv  # pip install python-dotenv

PORT = 587  
EMAIL_SERVER = "smtp.gmail.com" 

# Load the environment variables
current_dir = Path(__file__).resolve().parent if "__file__" in locals() else Path.cwd()
envars = current_dir / ".env"
load_dotenv(envars)

# Read environment variables
sender_email = os.getenv("EMAIL")
receiver_email="collins.chetekei@ke.grassavoye.com"
password_email = os.getenv("PASSWORD")

def send_email(subject, receiver_email, name, reminder_date):
    # Create the base text message.
    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = formataddr(("Expiry Reminder.", f"{sender_email}"))
    msg["To"] = receiver_email
    msg["BCC"] = sender_email

    msg.set_content(
        f"""\
    <html>
      <body>
        <p>Good day Collins,</p>
        <p>I hope you are well and remembering promise to self.</p>
        <p> I just wanted to drop you a quick note to remind you that <strong>{name}'s cover</strong> is expiring tomorrow.</p>
        <br>
        <p>Best regards</p>
        <p>Dev</p>
      </body>
    </html>
    """,
        subtype="html",
    )

       

    with smtplib.SMTP(EMAIL_SERVER, PORT) as server:
        server.starttls()
        server.login(sender_email, password_email)
        server.sendmail(sender_email, receiver_email, msg.as_string())


if __name__ == "__main__":
    app.run(debug=True)
