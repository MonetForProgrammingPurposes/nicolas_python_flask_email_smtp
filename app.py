from flask import Flask, request, jsonify
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Configure SMTP server settings
EMAIL_HOST = "smtp.gmail.com"  
EMAIL_PORT = 587 
EMAIL_HOST_USER = "monettenicolas069@gmail.com"  
EMAIL_HOST_PASSWORD = "dnxy ssap uurh ojtr"  

@app.route('/send-email', methods=['POST'])
def send_email():
    # Get data from request body
    data = request.json
    recipient_email = data.get('email')
    message_body = data.get('message')

    # Check if the required fields are provided
    if not recipient_email or not message_body:
        return jsonify({"error": "Email and message are required!"}), 400

    try:
        # Create email message
        msg = MIMEMultipart()
        msg['From'] = EMAIL_HOST_USER
        msg['To'] = recipient_email
        msg['Subject'] = "Automated Email from Flask App"  # Subject of the email

        # Attach the message body
        msg.attach(MIMEText(message_body, 'plain'))

        # Send the email using SMTP
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            server.sendmail(EMAIL_HOST_USER, recipient_email, msg.as_string())

        return jsonify({"message": "Email sent successfully!"}), 200

    except Exception as e:
        # Handle errors
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
