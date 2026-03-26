import random
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
from django.conf import settings

def generate_otp():
    """Generate 6-digit OTP"""
    return str(random.randint(100000, 999999))

def send_otp(email, otp):

    subject = "DigiLibrary - Email Verification OTP"

    text_content = f"Your OTP is {otp}"

    html_content = f"""
    <html>
    <body style="font-family:Arial;background:#111827;padding:40px">

        <div style="max-width:500px;margin:auto;background:#1f2937;
        padding:30px;border-radius:12px;text-align:center;color:white">

            <h2 style="color:#3b82f6;">DigiLibrary Verification</h2>

            <p style="font-size:16px">
            Use the OTP below to verify your email
            </p>

            <div style="
            font-size:20px;
            letter-spacing:8px;
            background:#111827;
            padding:15px;
            border-radius:10px;
            margin:20px 0;
            color:#22d3ee;
            font-weight:bold;">
            {otp}
            </div>

            <p style="font-size:14px;color:#9ca3af">
            This OTP is valid for 5 minutes.
            </p>

            <p style="font-size:12px;color:#6b7280;margin-top:30px">
            If you didn't request this OTP, please ignore this email.
            </p>

        </div>

    </body>
    </html>
    """

    # SendGrid Mail Object
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL, 
        to_emails=email,
        subject=subject,
        html_content=html_content
    )

    try:
        # Aapki API Key yahan settings se uthayi jayegi
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return True
    except Exception as e:
        print(f"SendGrid Error: {e}")
        return False