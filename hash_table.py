from prime_generator import get_next_size

class HashTable:
    def __init__(self, collision_type, params):
        '''
        Possible collision_type:
            "Chain"     : Use hashing with chaining
            "Linear"    : Use hashing with linear probing
            "Double"    : Use double hashing
        '''
        self.collision_type = collision_type
        if  self.collision_type == "Double":
            self.z2 = params[1]
            self.c2 = params[2]
        self.z = params[0]
        self.table_size = params[-1]
        self.table = [None]*self.table_size
        self.num_elements = 0
        self.distinct = 0

    def insert(self, x):
        if x is not None:
            if self.collision_type == 'Chain':
                self.insert_chain(x)
            elif  self.collision_type == 'Linear':
                self.insert_linear(x)
            elif  self.collision_type == 'Double':
                self.insert_double(x)

    def find(self, key):
        if self.collision_type ==  'Chain':
            return  self.find_chain(key)
        elif  self.collision_type == 'Linear':
            return self.find_linear(key)
        elif   self.collision_type == 'Double':
            return self.find_double(key)

    def char_to_num(self,key):
        # print(key)
        if 'a'<= key<='z':
            return ord(key)-ord('a')
        elif 'A'<= key<='Z':
            return ord(key)-ord('A') + 26
        return -1
    def hash_value(self,x,key):
        # print(x)
        p = 0
        for i in range(len(key)):
            p += ((x**i)*(self.char_to_num(key[i])))
        return p

    # def get_slot(self, key):
    #     x = self.z
    #     h = self.hash_value(x,key)
    #     slot = h%self.table_size
    #     return slot
    
    def get_load(self):
        return (self.num_elements)/(self.table_size)
    
    def __str__(self):
        g = []
        for i in self.table:
            if i is None:
                g.append("<EMPTY>")
            elif isinstance(i,list):
                g.append(" ; ".join(map(str,i)))
            else:
                g.append(str(i))
        return ' | '.join(g)
    # TO BE USED IN PART 2 (DYNAMIC HASH TABLE)
    def rehash(self):
        return self.rehash1()
# IMPLEMENT ALL FUNCTIONS FOR CLASSES BELOW
# IF YOU HAVE IMPLEMENTED A FUNCTION IN HashTable ITSELF, 
# YOU WOULD NOT NEED TO WRITE IT TWICE
    
class HashSet(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type,params)
    
    # def insert(self, key):
    #     pass
    def insert_chain(self,x):
        j = self.get_slot(x)
        # print(j,x)
        if self.table[j] is None:
            self.table[j] = []
            self.table[j].append(x)
            self.num_elements += 1
            self.distinct += 1
        else:
            if  x not in self.table[j]:
                self.table[j].append(x)
                self.distinct += 1
                self.num_elements += 1
                   
    def insert_linear(self,x):
        j = self.get_slot(x)
        if self.table[j] is None:
            self.table[j] = x
            self.num_elements += 1
            self.distinct += 1
        else:
            if self.table[j] == x:
                return
            i = (j+1)%self.table_size
            while self.table[i] is not None:
                if self.table[i] == x:
                    return
                elif i == j:
                    raise  Exception("Table is full")
                else:
                    i =  (i+1)%self.table_size
            if self.table[i] is  None:
                self.table[i] = x
                self.num_elements += 1
                self.distinct += 1
            else:
                return 

    def insert_double(self,x):
        j = self.get_slot(x)
        if self.table[j] is None:
            self.table[j] = x
            self.num_elements += 1
            self.distinct += 1
        else:
            t = self.z2
            p = self.hash_value(t,x)
            h2 = self.c2-(p%self.c2)
            h1 = j
            i = 1
            if  self.table[h1] == x:
                return
            while self.table[(h1+i*h2)%self.table_size] is not  None:
                if  self.table[(h1+i*h2)%self.table_size] == x:
                    return
                elif  (h1+i*h2)%self.table_size == j:
                    raise Exception("Table is full")
                else:
                    i += 1
            if self.table[(h1+i*h2)%self.table_size] is None:
                self.table[(h1+i*h2)%self.table_size] = x
                self.num_elements += 1
                self.distinct += 1


    def find_chain(self,key):
        j  = self.get_slot(key)
        if self.table[j] is None:
            return False
        else:
            if key in self.table[j]:
                return True
            return  False

    def  find_linear(self,key):
        i = self.get_slot(key)
        j = i
        while  self.table[j] is not None:
            if self.table[j] == key:
                return True
            else:
                j = (j + 1) % self.table_size
        return False
    
    def find_double(self,key):
        j = self.get_slot(key)
        if self.table[j] is None:
            return False
        else:
            if  self.table[j] ==  key:
                return True
            else:
                t = self.z2
                p = self.hash_value(t,key)
                h2 = self.c2-(p%self.c2)
                h1 = j
                i = 1
                while self.table[(h1+i*h2)%self.table_size] is not  None:
                    if   self.table[(h1+i*h2)%self.table_size] == key:
                        return True
                    elif self.table[(h1+i*h2)%self.table_size] == self.table[j]:
                        return False
                    i += 1
            return False
                    
    def get_slot(self, key):
        x = self.z
        h = self.hash_value(x,key)
        slot = h%self.table_size
        return slot

class HashMap(HashTable):
    def __init__(self, collision_type, params):
        super().__init__(collision_type, params)
 
    def insert_chain(self,x):
        j = self.get_slot(x[0])
        if self.table[j] is None:
                self.table[j] = [x]
                self.num_elements += 1
                self.distinct += 1
        elif self.table[j] is not None:
            if x not in self.table[j]:
                self.table[j].append(x)
                self.num_elements += 1
                self.distinct += 1
            elif x in  self.table[j]:
                return 


    def insert_linear(self,x):
        j = self.get_slot(x[0])
        if self.table[j] is None:
            self.table[j] = x
            self.num_elements += 1
            self.distinct += 1
        else:
            if self.table[j] == x:
                return
            i = (j+1)%self.table_size
            while self.table[i] is not None:
                if self.table[i] == x:
                    return
                elif i == j:
                    raise  Exception("Table is full")
                else:
                    i =  (i+1)%self.table_size
            self.table[i] = x
            self.num_elements += 1
            self.distinct += 1
              
    def insert_double(self,x):
        j = self.get_slot(x[0])
        if self.table[j] is None:
            self.table[j] = x
            self.num_elements += 1
            self.distinct += 1
        else:
            t = self.z2
            p = self.hash_value(t,x[0])
            h2 = self.c2-(p%self.c2)
            h1 = j
            i = 1
            if  self.table[h1] == x:
                return
            while self.table[(h1+i*h2)%self.table_size] is not  None:
                if  self.table[(h1+i*h2)%self.table_size] == x:
                    return
                elif  self.table[(h1+i*h2)%self.table_size] == self.table[j]:
                    raise Exception("Table is full")
                else:
                    i += 1
            self.table[(h1+i*h2)%self.table_size] = x
            self.num_elements += 1
            self.distinct += 1

    def find_chain(self,key):
        j  = self.get_slot(key)
        if self.table[j] is None:
            return 
        else:
            for i in range(len(self.table[j])):
                if self.table[j][i][0] == key:
                    return self.table[j][i][1]
            return

    def  find_linear(self,key):
        j = self.get_slot(key)
        while  self.table[j] is not None:
            if self.table[j][0] == key:
                return self.table[j][1]
            else:
                j = (j + 1) % self.table_size
        return 

    def find_double(self,key):
        j = self.get_slot(key)
        if self.table[j] is None:
            return 
        else:
            if  self.table[j][0] ==  key:
                return self.table[j][1]
            else:
                t = self.z2
                p = self.hash_value(t,key)
                h2 = self.c2-(p%self.c2)
                h1 = j
                i = 1
                while self.table[(h1+i*h2)%self.table_size] is not  None:
                    if   self.table[(h1+i*h2)%self.table_size][0] == key:
                        return self.table[(h1+i*h2)%self.table_size][1]
                    elif self.table[(h1+i*h2)%self.table_size] == self.table[j]:
                        return 
                    else:
                        i += 1
            return 

    def get_slot(self, key):
        x = self.z
        h = self.hash_value(x,key)
        slot = h%self.table_size
        return slot
