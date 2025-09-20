import unittest
from RandomizedSet0380 import RandomizedSet

class RandomizedSetTest(unittest.TestCase):
    def test_randomizedSet(self):
        result = []
        randomized_set = None
        result.append(str(randomized_set))
        randomized_set = RandomizedSet()
        result.append(str(randomized_set.insert(1)))
        result.append(str(randomized_set.remove(2)))
        result.append(str(randomized_set.insert(2)))
        random_val = randomized_set.getRandom()
        result.append(str(random_val))
        result.append(str(randomized_set.remove(1)))
        result.append(str(randomized_set.insert(2)))
        result.append(str(randomized_set.getRandom()))
        
        expected1 = ["None", "True", "False", "True", "1", "True", "False", "2"]
        expected2 = ["None", "True", "False", "True", "2", "True", "False", "2"]
        
        if random_val == 1:
            self.assertEqual(result, expected1)
        else:
            self.assertEqual(result, expected2)
