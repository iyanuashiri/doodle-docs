import os, sys, csv
from docs.models import Doc


def create_docs():
    with open(os.path.join(sys.path[0], 'MOCK_DATA.csv'), 'r') as csvfile:
        data = csv.DictReader(csvfile)
        for row in data:
            Doc.objects.create(title=row['title'], body=row['body'])
    return 'Complete'


if __name__ == '__main__':
    create_docs()
