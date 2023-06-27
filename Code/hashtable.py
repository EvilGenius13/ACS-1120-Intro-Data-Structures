#!python

from linkedlist import LinkedList


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = []
        for i in range(init_size):
            self.buckets.append(LinkedList())

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = []
        for key, val in self.items():
            items.append('{!r}: {!r}'.format(key, val))
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        Running time: O(n) This method has to loop through all the buckets and all the items in each bucket to get all the keys."""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        Running time: O(n) This method has to loop through all the buckets and all the items in each bucket to get all the values."""
        all_values = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_values.append(value)
        return all_values

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        Running time: O(n) This method has to loop through all the buckets and all the items in each bucket to get all the items."""
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        Running time: O(n) This method has to loop through all the buckets and count the items in each bucket to get the length."""
        count = 0
        for bucket in self.buckets:
            count += bucket.length()
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        Running time: O(n) This method has to find the bucket where the key belongs and then check if the key-value entry exists in the bucket.
        This is dependent on the length of the bucket."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        return bucket.find(lambda item: item[0] == key) is not None
        # for item_key, item_value in bucket.items():
        #     if item_key == key:
        #         return True
        # return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        Running time: O(1) This method has to find the bucket where the key belongs and then retrieve the value associated with the key and bucket."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        item = bucket.find(lambda item: item[0] == key)
        if item is not None:
            return item[1]
        else:
            raise KeyError('Key not found: {}'.format(key))

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        Running time: O(1) This method has to find the bucket where the key belongs and then insert or update the key-value entry in the bucket."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        item = bucket.find(lambda item: item[0] == key)
        if item is not None:
            bucket.delete(item)
        bucket.append((key, value))

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        Running time: O(1) This method has to find the bucket where the key belongs and then delete the key-value entry in the bucket."""
        index = self._bucket_index(key)
        bucket = self.buckets[index]
        item = bucket.find(lambda item: item[0] == key)
        if item is not None:
            bucket.delete(item)
        else:
            raise KeyError('Key not found: {}'.format(key))

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    test_hash_table()
