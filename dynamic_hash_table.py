from hash_table import HashSet, HashMap
from prime_generator import get_next_size

class DynamicHashSet(HashSet):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash1(self):
        # IMPLEMENT THIS FUNCTION
        old_table = self.table
        a = get_next_size()
        self.table = [None] * a
        self.table_size = a
        self.num_elements = 0
        self.distinct = 0
        for  bucket in old_table:
            if bucket  is not None:
                if isinstance(bucket,list):
                    for i in  bucket:
                        self.insert(i)
                else:
                    self.insert(bucket)
        
    def insert(self, x):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(x)

        if self.get_load() >= 0.5:
            self.rehash1()
            
class DynamicHashMap(HashMap):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
        
    def rehash1(self):
        old_table = self.table
        a = get_next_size()
        self.table = [None] *a
        self.table_size = a
        self.num_elements = 0
        self.distinct = 0
        for  bucket in old_table:
            if bucket  is not None:
                if isinstance(bucket,list):
                    for i in  bucket:
                        self.insert(i)
                else:
                    self.insert(bucket)

    
    def insert(self, key):
        # YOU DO NOT NEED TO MODIFY THIS
        super().insert(key)
        
        if self.get_load() >= 0.5:
            self.rehash1()
