import datetime

# Get the current date and time
now = datetime.datetime.now()

# Format the time nicely
formatted_time = now.strftime("%Y-%m-%d %H:%M:%S")

print(f"Current date and time: {formatted_time}")
