# coding: utf-8
from sqlalchemy import (CheckConstraint, Column, ForeignKey, Integer, String,
                        Table, Text, text)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()
metadata = Base.metadata


class Country(Base):
    __tablename__ = 'country'    
    countryid = Column(Integer, primary_key=True, server_default=text("nextval('country_countryid_seq'::regclass)"))
    countryname = Column(String(60))
    
class Repeater(Base):
    __tablename__ = 'repeater'

    repeaterid = Column(Integer, primary_key=True)    
    stateid = Column(ForeignKey('state.stateid'))

    state = relationship('State')


class State(Base):
    __tablename__ = 'state'
    stateid = Column(String(10), primary_key=True)
    statename = Column(String(60))
    countryid = Column(ForeignKey('country.countryid'), nullable=False, server_default=text("nextval('state_countryid_seq'::regclass)"))

    country = relationship('Country')


class SpatialRefSy(Base):
    __tablename__ = 'spatial_ref_sys'
    __table_args__ = (
        CheckConstraint('(srid > 0) AND (srid <= 998999)'),
    )
    srid = Column(Integer, primary_key=True)
    auth_name = Column(String(256))
    auth_srid = Column(Integer)
    srtext = Column(String(2048))
    proj4text = Column(String(2048))

t_geography_columns = Table(
    'geography_columns', metadata,
    Column('f_table_catalog', String),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geography_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', Text)
)


t_geometry_columns = Table(
    'geometry_columns', metadata,
    Column('f_table_catalog', String(256)),
    Column('f_table_schema', String),
    Column('f_table_name', String),
    Column('f_geometry_column', String),
    Column('coord_dimension', Integer),
    Column('srid', Integer),
    Column('type', String(30))
)
