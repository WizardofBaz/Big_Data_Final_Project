import csv
from Connection import get_redis_connection

# Connect to Redis
r = get_redis_connection()

r.flushall()

Happy = 'What_Made_You_Happy.csv'

# Function to import data into Redis
def import_data(Happy):
    with open(Happy, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            key = row['hmid']
            value = row['cleaned_hm']
            r.set(key, value)

if __name__ == "__main__":
    import_data(Happy)
    print("Data imported successfully.")
