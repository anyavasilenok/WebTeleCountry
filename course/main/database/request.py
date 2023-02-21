from neo4j import GraphDatabase
from config import LOCALHOST, LOGIN, PASSWORD


class Request:

    def __init__(self):
        self.driver = GraphDatabase.driver(LOCALHOST, auth=(LOGIN, PASSWORD))

    def close(self):
        self.driver.close()


request = Request()

