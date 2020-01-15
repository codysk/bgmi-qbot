import unittest
from utils import group_set, discuss_set
import random
import os


class TestSavableSet(unittest.TestCase):

    def test_all(self):
        group_set.clear()
        discuss_set.clear()
        group_set.save()
        discuss_set.save()
        i = 10
        while i > 0:
            i -= 1
            tmp_id = str(random.randrange(1000, 99999))
            discuss_set.add(tmp_id)
            group_set.add(tmp_id)

        self.assertEqual(10, len(discuss_set))
        self.assertEqual(10, len(group_set))

        discuss_set.add('d_target')
        group_set.add('g_target')

        self.assertIn('d_target', discuss_set)
        self.assertIn('g_target', group_set)

        discuss_set.remove('d_target')
        self.assertNotIn('d_target', discuss_set)
        group_set.remove('g_target')
        self.assertNotIn('g_target', group_set)

        group_set.clear()
        discuss_set.clear()
        self.assertEqual(0, len(discuss_set))
        self.assertEqual(0, len(group_set))

        group_set.save()
        discuss_set.save()
        with open(os.environ.get('DATA_PATH', './data') + '/discuss_set.json') as file:
            content = file.read()
            self.assertEqual("[]", content)
        with open(os.environ.get('DATA_PATH', './data') + '/group_set.json') as file:
            content = file.read()
            self.assertEqual("[]", content)

        with open(os.environ.get('DATA_PATH', './data') + '/discuss_set.json', 'w') as file:
            file.write('["123","asd"]')
        discuss_set.load()
        self.assertIn("asd", discuss_set)
        with open(os.environ.get('DATA_PATH', './data') + '/group_set.json', 'w') as file:
            file.write('["321","qwe"]')
        group_set.load()
        self.assertIn("321", group_set)

        pass


if __name__ == '__main__':
    unittest.main()
