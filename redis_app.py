import csv, redis, json
import sys

REDIS_HOST = '34.93.49.121'
REDIS_PORT = 5050

def read_csv_data(csv_file, ik, iv):
    with open(csv_file, encoding='utf-8') as csvf:
        csv_data = csv.reader(csvf)
        print("Reading from the datasource!")
        return [(r[ik], r[iv]) for r in csv_data]

def store_data(conn, data):
    for i in data:
        conn.setnx(i[0], i[1])
        print("Writing Data to Redis!")
    return data

def main():
    if len(sys.argv) < 2:
        sys.exit(
        "Usage: %s file.csv [key_column_index, value_column_index]"
        % __file__
        )
    columns = (0, 2) if len(sys.argv) < 4 else (int(x) for x in sys.argv[2:4])
    data = read_csv_data(sys.argv[1], *columns)
    conn = redis.Redis(host=REDIS_HOST, port=REDIS_PORT)
    print (json.dumps(store_data(conn, data)))

if '__main__' == __name__:
    main()