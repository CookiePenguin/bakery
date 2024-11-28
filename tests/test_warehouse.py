import os
import unittest
import sqlite3

from src.db import Warehouse


class TestWarehouse(unittest.TestCase):

    def setUp(self):
        self.warehouse = Warehouse()


    def test_get_stuff(self):
        test_stuff = [('Круассаны', 15), ('Розаны', 10), ('Ватрушки', 21)]
        for i in test_stuff:
            self.warehouse.cursor.execute("INSERT INTO Stuff (name, amount) VALUES (?, ?)", (i[0], i[1]))
        self.warehouse.connection.commit()
        result = self.warehouse.get_staff()
        self.assertEqual(test_stuff, result)

    def test_write_stuff(self):
        test_stuff = [('Круассаны', 15), ('Розаны', 10), ('Ватрушки', 21)]
        for i in test_stuff:
            self.warehouse.write_stuff({i[0]: i[1]})

        stuff = self.warehouse.cursor.execute('SELECT * FROM Stuff').fetchall()

        self.assertEqual(stuff, test_stuff)


    def test_order_ingredients(self):
        pass

    def test_get_ingredients(self):
        pass

    def tearDown(self):
        self.warehouse.connection.close()
        os.remove('warehouse.db')


if __name__ == '__main__':
    unittest.main()