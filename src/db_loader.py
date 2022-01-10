import csv
from datetime import datetime
from src import db
from src.models import Events


def load_data_from_file():
    rows = []
    with open("data.csv", 'r') as file:
        csvreader = csv.DictReader(file, delimiter=';')
        for row in csvreader:
            row['timestamp'] = datetime.fromtimestamp(float(row['timestamp']))
            row['stars'] = int(row['stars'])
            events = Events(**row)
            db.session.add(events)
            rows.append(row)
    db.session.commit()
    db.session.close()
    return len(rows)


if __name__ == '__main__':
    print(f'{load_data_from_file()} records added')
