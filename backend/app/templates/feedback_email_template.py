from typing import Dict

def get_feedback_email_template(feedback_link: str) -> str:
    return f"""
    <html>
    <body>
        <p>Dear Tester,</p>
        <p>Thank you for playing our game! We would love to hear your feedback.</p>
        <p>Please click the link below to provide your feedback:</p>
        <a href="{feedback_link}">Submit Feedback</a>
        <p>Thank you for your time!</p>
        <p>The Development Team</p>
    </body>
    </html>
    """
