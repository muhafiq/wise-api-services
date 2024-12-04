import os
from email.message import EmailMessage
import ssl
import smtplib

EMAIL_SENDER = os.environ.get('EMAIL_SENDER')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')

def send_email(subject, data):
    body = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Reset Password</title>
        <style>
            body {{
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                margin: 0;
                padding: 20px;
            }}
            .container {{
                max-width: 600px;
                margin: 0 auto;
                background-color: #ffffff;
                padding: 30px;
                border-radius: 8px;
                box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            }}
            .header {{
                text-align: center;
                color: #333;
            }}
            .header h1 {{
                font-size: 24px;
            }}
            .content {{
                font-size: 16px;
                line-height: 1.5;
                color: #333;
            }}
            .button {{
                display: block;
                width: 200px;
                margin: 20px auto;
                padding: 10px;
                background-color: #007bff;
                color: white;
                text-align: center;
                text-decoration: none;
                border-radius: 5px;
                font-size: 16px;
            }}
            .footer {{
                font-size: 14px;
                text-align: center;
                color: #777;
            }}
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>Reset Your Password</h1>
            </div>
                <p>Hello {data['email']},</p>
                <p>We received a request to reset your password. To proceed, please use the following 6-digit token to reset your password:</p>
                <p><strong>{data['token']}</strong></p>
                <p>If you did not request this, please ignore this email. If you need further assistance, feel free to contact our support team.</p>
            <div class="footer">
                <p>Best regards, <br> Wise. Inc</p>
            </div>
        </div>
    </body>
    </html>
    """

    em = EmailMessage()
    em['From'] = EMAIL_SENDER
    em['To'] = data['email']
    em['Subject'] = subject
    em.set_content(body, subtype='html')

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login(EMAIL_SENDER, EMAIL_PASSWORD)
        smtp.sendmail(EMAIL_SENDER, data['email'], em.as_string())




