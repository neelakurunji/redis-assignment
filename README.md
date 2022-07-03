# redis-assignment

# Problem Statement
1. Implement a queue and insert 200 people listed to receive Covid-19 vaccine into Redis OSS server
2. ReplicaOf will forward the queue to Enterprise DB. From the Redis Enterprise DB resource, split those
people into 6 vaccine receiving spots. Please share how many received their shots in each position.
3. For validation: preserve the output of steps 1 & 2.

# My Take
I could only do till the loading of data and replicating it in the Enterprise DB.

# Run the App
python3 redis_app.py redis_dataset.csv
