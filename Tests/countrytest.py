import unittest
from models.models import Country
import config
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# General Principles at play:
# for each action we want to do with this entity we should be writing a test case
# Generally follow CRUD (Create, Read, Update, and Delete) other functionality will arise as our program gets more complicated, at the very least stub in your test case when you add functionality
# session.commit writes the actual changes to the database so that we can later use them otherwise they are stored in session memory

class countryTest(unittest.TestCase):

    # setup and teardown methods do stuff like initailize the database connection and set up the session variable
    @classmethod
    def setUpClass(cls):
        cls.db_string = "postgres://{0}:{1}@{2}:{3}/{4}".format(
            config.username, config.password, config.address, config.port, config.dbname)
        cls.db = create_engine(cls.db_string)
        cls.db.connect()
        Session = sessionmaker(bind=cls.db)
        cls._session = Session()

    @classmethod
    def tearDownClass(cls)
    cls._session.close()
    cls.db.close()
    ##write an item to the database, check that it was added and remove it aftewards
    def test_addCountry(self):
        # Initialize items to be used in testing
        testCountry = Country(countryname="test_CountryName")
        query = self._session.query(Country)
        currentCount = query.count()
        # add Item to database
        self._session.add(testCountry)
        self._session.commit()
        # Verify that the expected result occurs, because we are adding I expect an additional item with the properties above
        self.assertTrue(query.count() == (currentCount+1),
                        "Count is not increased")
        self.assertTrue(query.filter(Country.countryid == testCountry.countryid) and query.filter(
            Country.countryname == testCountry.countryid), "Country did not match expected value for adding")

        # clean up the database by removing test item we only need to pass the id as it is the primary key
        query.filter(Country.countryid == testCountry.countryid).delete()
        self._session.commit()
    
    ##write an item to the database, delete it, verify that it is not in the database
    def test_deleteCountry(self):
        raise NotImplementedError("error")
    
    ## write an item to the database, retrieve it, modify it, write it back to the database, ensure that hte new version is in the database
    def test_updateCountry(self):
        raise NotImplementedError("error")
    
    ## write a set of items to the database, retrieve them, verify that the contents are expected and the count is expected
    def test_listCountries(self):
        raise NotImplementedError("error")


if __name__ == '__main__':
    unittest.main()
