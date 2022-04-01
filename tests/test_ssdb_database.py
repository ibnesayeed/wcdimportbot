from unittest import TestCase

from src.models.ssdb_database import SsdbDatabase


class TestSsdbDatabase(TestCase):
    @staticmethod
    def test_set():
        r = SsdbDatabase()
        r.connect()
        r.set(key="test", value="test")
        result = r.get("test").decode("UTF-8")
        print(result)
        assert result == "test"
        # self.fail()