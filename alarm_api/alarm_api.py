from pymongo import MongoClient


class alarm_api:
    database = ""
    collection_name = ""

    def __init__(self, host, port):
        self.host = host
        self.port = port

    def MongoConnect(self):
        client = MongoClient(self.host, self.port)
        self.database = client.Arduino_Alarm

    def setCollection(self, collection_name):
        self.collection_name = collection_name

    def getCollection(self):
        return self.collection_name

    def makeTestQuery(self):
        collection = self.collection_name
        db = self.database
        # test query
        data = db.collection.find()



def main():
    api = alarm_api('localhost', 27017)
    api.MongoConnect()
    api.setCollection('alarm_data')
    api.makeTestQuery()


if __name__ == '__main__':
    main()
