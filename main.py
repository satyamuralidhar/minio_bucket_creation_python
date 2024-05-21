'''
Reference for minio docs
'''
from minio import Minio 
import os
from minio.commonconfig import Tags

#create a client
client = Minio(endpoint="localhost:9000",
    access_key=os.environ.get('MINIO_ACCESS_KEY'),
    secret_key=os.environ.get('MINIO_SECRET_KEY'),
    secure=False)

# create a buckets
no_of_buckets=4
empty_buckets = list()

'''
Buckets Creation
'''
def bucket_creation() -> None:
    try:
        for i in range(1,no_of_buckets+1):
            client.make_bucket("demobucket0"+str(i))
    except:
        print("Buckets are already exists")

'''
Appending list of buckets into an empty list
'''
for bkts in client.list_buckets():
        empty_buckets.append(bkts)

class Bucket:
    def __init__(self,name):
        self.name = name
    
bucket_names = []

for bucket in empty_buckets:
    bucket_names.append(bucket.name)

print(bucket_names)

'''
create tags
'''

if len(bucket_names) == no_of_buckets:
    tags = Tags.new_bucket_tags()
    tags['Envrionment'] = 'Dev'
    tags['User'] = 'Satya'
    for i in bucket_names:
        client.set_bucket_tags(i,tags)

if __name__ == "__main__":
    bucket_creation()


