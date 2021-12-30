import unittest

from automon.integrations.elasticsearch.client import ElasticsearchClient


class Elasticsearch(unittest.TestCase):

    def test_endpoints(self):
        hosts = 'https://logging.es.eastus2.azure.elastic-cloud.com:9243'
        cloud_id = ''
        user = 'elastic'
        password = 'pMdre9vGI0p1OzjitSEvHcLF'

        c = ElasticsearchClient(hosts=hosts, cloud_id=cloud_id, user=user, password=password)

        if c.connected():
            self.assertTrue(c)
            self.assertTrue(c.get_indices())
            self.assertTrue(c.info())
            self.assertTrue(c.ping())


if __name__ == '__main__':
    unittest.main()
