import unittest
from models.models import Country
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class countryTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.db_string = "postgres://{0}:{1}@{2}:{3}/{4}".format(
            config.username, config.password, config.address, config.port, config.dbname)
        cls.db = create_engine(cls.db_string)
        cls.db.connect()
        Session = sessionmaker(bind=cls.db)
        cls._session = Session()

    def test_addCountry(self):
        testCountry = Country()
        testCountry.countryname = "test_CountryName"
        query = self._session.query(Country)
        currentCount = query.count()

        self._session.add(testCountry)
        self._session.commit()
        self.assertTrue(query.count() == (currentCount+1),
                        "Count is not increased")
        self.assertTrue(query.filter(Country.countryid == testCountry.countryid) and query.filter(
            Country.countryname == testCountry.countryid), "Country did not match expected value for adding")

        query.filter(
            Country.countryname == testCountry.countryname and Country.countryid == testCountry.countryid).delete()

        self._session.commit()

    def test_deleteCountry(self):
        raise NotImplementedError("error")

    def test_updateCountry(self):
        raise NotImplementedError("error")

    def test_listCountries(self):
        raise NotImplementedError("error")


if __name__ == '__main__':
    unittest.main()
