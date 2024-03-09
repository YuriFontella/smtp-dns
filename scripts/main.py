import csv
import datetime
import os

from scripts.deliver import deliver
from src.models.main import Files

async def emails(data):
    now = datetime.datetime.now()
    format = "%Y-%m-%d_%H-%M-%S"

    name = f'{now.strftime(format)}.csv'
    file_path = os.path.join('files', name)

    with open(file_path, 'w') as file:
        writer = csv.DictWriter(file, fieldnames=['email', 'status', 'message'])
        writer.writeheader()

        for email in data:
            status, message = await deliver(email)
            writer.writerow(dict(email=email, status=status, message=message))


    full_path = os.path.join(os.getcwd(), file_path)
    if os.path.exists(full_path):
        await Files.create(name=name)
