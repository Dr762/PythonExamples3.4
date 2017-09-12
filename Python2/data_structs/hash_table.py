class HashTable(object):
    def __init__(self):
        self.table = [None]*10000
        print self.table

    def store(self, string):
        """Input a string that's stored in
        the table."""
        val = self.calculate_hash_value(string)
        if val!=-1:
            if self.table[val]!=None:
                self.table[val].append(string)
            else:
                self.table[val] = [string]


    def lookup(self, string):
        """Return the hash value if the
        string is already in the table.
        Return -1 otherwise."""
        val = self.calculate_hash_value(string)
        if val!=-1:
            if self.table[val]!=None:
                if string in self.table[val]:
                    return val
        return -1

    def calculate_hash_value(self, string):
        """Helper function to calulate a
        hash value from a string."""
        val = ord(string[0])*100 + ord(string[1])
        return val

# Setup
hash_table = HashTable()

# Test calculate_hash_value
# Should be 8568
print hash_table.calculate_hash_value('UDACITY')

# Test lookup edge case
# Should be -1
print hash_table.lookup('UDACITY')

# Test store
hash_table.store('UDACITY')
# Should be 8568
print hash_table.lookup('UDACITY')

# Test store edge case
hash_table.store('UDACIOUS')
# Should be 8568
print hash_table.lookup('UDACIOUS')
