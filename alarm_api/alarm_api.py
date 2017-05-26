from pymongo import MongoClient

class alarm_api:

    db = ""

    def __init__(self, host, port):

        self.host = host
        self.port = port


    def MongoConnect(self):
        client = MongoClient(self.host, self.port)
        self.db = client.Arduino_Alarm

    def setCollection(self, collection_name):
        self.collection_name = collection_name

    def getCollection(self):
        return self.collection_name

    def makeTestQuery():
        collection = self.collection_name

    def test_print(self):
        print(self.db)



def main():
    api = alarm_api('localhost', 27017)
    api.MongoConnect()
    api.setCollection('alarm_data')
    api.test_print()
    #name = api.getCollection()
    #print(name)


if __name__ == '__main__':
    main()
