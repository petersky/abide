#import boto3

# TODO: Rewrite. Not thread-safe.
#dynamodb = boto3.resource('dynamodb')


class DDB(object):
    def __init__(self, table_name):
        self.name = table_name
        self.loaded = False
        self.table = None

    def load(self):
        #self.table = dynamodb.Table(self.name)
        self.table.load()
        self.loaded = True
