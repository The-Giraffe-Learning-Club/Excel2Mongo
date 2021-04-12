import unittest
import os
import sys
sys.path[0:0] = [""]

import pymongo


class TestPyMongo(unittest.TestCase):

    def setUp(self):
        self.host = os.environ.get("DB_IP", "localhost")
        self.port = int(os.environ.get("DB_PORT", 27017))

    def test_connection_alias(self):
        c = pymongo.MongoClient(self.host, self.port)
        self.assertTrue(c)
        self.assertEqual(c.host, self.host)
        self.assertEqual(c.port, self.port)

if __name__ == "__main__":
    unittest.main()