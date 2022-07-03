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

# The Output
<img width="1430" alt="Screenshot 2022-07-03 at 4 37 41 PM" src="https://user-images.githubusercontent.com/89900575/177037288-a10eeb18-62a4-4a3a-a1ea-3b4f2a570c1c.png">

<img width="1440" alt="Screenshot 2022-07-03 at 4 38 14 PM" src="https://user-images.githubusercontent.com/89900575/177037300-7bc5e3e2-1b92-4600-8f42-de2802f6cdc0.png">
