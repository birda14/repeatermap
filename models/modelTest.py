from models import Country
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker



db_string = "postgres://{0}:{1}@{2}:{3}/{4}".format(
    username, password, address, port, dbname)


def main():
    
    c = Country()
    c.countryname = "testName"

    print("{0} {1}".format(c.countryname, c.countryid))
    _session = Session()
    _session.add(c)
    _session.commit()
    result = _session.query(Country)
    c2 = result.first()
    print(c2.countryname)
if __name__ == "__main__":
    main()
