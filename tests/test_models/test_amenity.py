#!/usr/bin/python3
"""
Unit Test for Amenity Class
"""
import unittest
from datetime import datetime
import models
import json
from models.engine.db_storage import __session
from os import environ
from models.engine.db_storage import DBStorage

Amenity = models.amenity.Amenity
BaseModel = models.base_model.BaseModel


class TestAmenityDocs(unittest.TestCase):
    """Class for testing BaseModel docs"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('..... Testing Documentation .....')
        print('........   Amenity  Class   ........')
        print('.................................\n\n')

    def test_doc_file(self):
        """... documentation for the file"""
        expected = '\nAmenity Class from Models Module\n'
        actual = models.amenity.__doc__
        self.assertEqual(expected, actual)

    def test_doc_class(self):
        """... documentation for the class"""
        expected = 'Amenity class handles all application amenities'
        actual = Amenity.__doc__
        self.assertEqual(expected, actual)

    def test_doc_init(self):
        """... documentation for init function"""
        expected = 'instantiates a new amenity'
        actual = Amenity.__init__.__doc__
        self.assertEqual(expected, actual)


class TestAmenityInstances(unittest.TestCase):
    """testing for class instances"""

    @classmethod
    def setUpClass(cls):
        print('\n\n.................................')
        print('....... Testing Functions .......')
        print('.........  Amenity  Class  .........')
        print('.................................\n\n')

    def setUp(self):
        """initializes new amenity for testing"""
        self.amenity = Amenity()
        if (environ(HBNB_TYPE_STORAGE) == "db"):
            DBStorage.__init__()

    @unittest.skipIf(environ(HBNB_TYPE_STORAGE) == "file",
                     "only need to tearDown if database used")
    def tearDown(self):
        """tearDown to close __session and __engine when using database"""
        DBStorage.__session.close()
        DBStorage.__engine.close()

    def test_instantiation(self):
        """... checks if Amenity is properly instantiated"""
        self.assertIsInstance(self.amenity, Amenity)

    def test_to_string(self):
        """... checks if BaseModel is properly casted to string"""
        my_str = str(self.amenity)
        my_list = ['Amenity', 'id', 'created_at']
        actual = 0
        for sub_str in my_list:
            if sub_str in my_str:
                actual += 1
        self.assertTrue(3 == actual)

    def test_instantiation_no_updated(self):
        """... should not have updated attribute"""
        my_str = str(self.amenity)
        actual = 0
        if 'updated_at' in my_str:
            actual += 1
        self.assertTrue(0 == actual)

    def test_updated_at(self):
        """... save function should add updated_at attribute"""
        self.amenity.save()
        actual = type(self.amenity.updated_at)
        expected = type(datetime.now())
        self.assertEqual(expected, actual)

    @unittest.skipIf(environ(HBNB_TYPE_STORAGE) == "db",
                     "this test used filestorage, not a database")
    def test_to_json(self):
        """... to_json should return serializable dict object"""
        self.amenity_json = self.amenity.to_json()
        actual = 1
        try:
            serialized = json.dumps(self.amenity_json)
        except:
            actual = 0
        self.assertTrue(1 == actual)

    @unittest.skipIf(environ(HBNB_TYPE_STORAGE) == "db",
                     "this test used filestorage, not a database")
    def test_json_class(self):
        """... to_json should include class key with value Amenity"""
        self.amenity_json = self.amenity.to_json()
        actual = None
        if self.amenity_json['__class__']:
            actual = self.amenity_json['__class__']
        expected = 'Amenity'
        self.assertEqual(expected, actual)

    def test_wifi_attribute(self):
        """... add wifi attribute"""
        self.amenity.name = "greatWifi"
        if hasattr(self.amenity, 'name'):
            actual = self.amenity.name
        else:
            actual = ''
        expected = "greatWifi"
        self.assertEqual(expected, actual)

    @unittest.skipIf(environ(HBNB_TYPE_STORAGE) == 'file',
                     "this test uses a database for storage")
    def test_amenity_id(self):
        expected = self.amenity.id
        DBStorage.new(self.amenity)
        DBStorage.save()
        actual = DBStorage.__session.query(Amenity).filter(
            Amenity.id == expected).one()
        self.assertTrue(expected == actual)

    @unittest.skipIf(environ(HBNB_TYPE_STORAGE) == 'file',
                     "this test uses a database for stroage")
    def test_amenity_attr_name(self):
        expected = "wifi"
        amenity_id = self.amenity.id
        DBStorage.new(self.amenity)
        DBStorage.save()
        amenity_obj = DBStorage.__session.query(Amenity).filter(
            Amenity.id == amenity_id).one()
        amenity_obj.name = "wifi"
        DBStorage.save(amenity_obj)
        actual = DBStorage.__session.query(Amenity.name).filter(
            Amenity.id =- amenity_id).one()
        self.assertTrue(expected == actual)

if __name__ == '__main__':
    unittest.main
