import unittest
from dsainone.hash_table import HashTable

class TestHashTable(unittest.TestCase):
    """Unit tests for the optimized HashTable implementation."""

    def setUp(self):
        """Initialize a new hash table before each test."""
        self.hash_table = HashTable(capacity=50)  # Smaller capacity for testing

    def test_insert_and_search(self):
        """Test insertion and retrieval of values."""
        self.hash_table.insert("key1", 100)
        self.hash_table.insert("key2", 200)
        self.assertEqual(self.hash_table.search("key1"), 100)
        self.assertEqual(self.hash_table.search("key2"), 200)

    def test_search_non_existent_key(self):
        """Test searching for a key that does not exist."""
        self.assertIsNone(self.hash_table.search("missing_key"))

    def test_insert_and_overwrite(self):
        """Ensure that inserting a duplicate key updates the value."""
        self.hash_table.insert("key1", 100)
        self.hash_table.insert("key1", 500)  # Overwrite
        self.assertEqual(self.hash_table.search("key1"), 500)

    def test_delete_key(self):
        """Test deletion of a key-value pair."""
        self.hash_table.insert("key1", 100)
        self.hash_table.delete("key1")
        self.assertIsNone(self.hash_table.search("key1"))

    def test_collision_handling(self):
        """Check if hash table handles collisions correctly (open addressing)."""
        for i in range(50):  # Fill up all slots
            self.hash_table.insert(f"key{i}", i)

        for i in range(50):
            self.assertEqual(self.hash_table.search(f"key{i}"), i)

    def test_large_insertions(self):
        """Test performance with a large number of entries."""
        for i in range(1000):
            self.hash_table.insert(f"key{i}", i)

        for i in range(1000):
            self.assertEqual(self.hash_table.search(f"key{i}"), i)

if __name__ == "__main__":
    unittest.main()
