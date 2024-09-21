from datetime import datetime
import pytz

def formatted_date():
    tz = pytz.timezone('Asia/Kolkata')  # Adjust timezone as needed
    now = datetime.now(tz)
    return now.strftime("%d/%m/%Y %I:%M %p")