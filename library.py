import hash_table as ht

class DigitalLibrary:
    # DO NOT CHANGE FUNCTIONS IN THIS BASE CLASS
    def __init__(self):
        pass
    
    def distinct_words(self, book_title):
        pass
    
    def count_distinct_words(self, book_title):
        pass
    
    def search_keyword(self, keyword):
        pass
    
    def print_books(self):
        pass
class MuskLibrary:
    def __init__(self, book_titles, texts):
        t = []
        for r in range(len(texts)):
            f = []
            for  w in texts[r]:
                f.append(w)
            t.append(f)
        
        b = []
        for k in range(len(book_titles)):
            b.append(book_titles[k])
        self.lis =[]
        for i in  range(len(b)):
            a = self.mergesort(t[i])
            self.lis.append([b[i],a])
        self.mergesort1(self.lis)
        for i in range(len(self.lis)):
            u= []
            u.append(self.lis[i][1][0])
            for j in range(1,len(self.lis[i][1])):
                if self.lis[i][1][j] != u[-1]:
                    u.append(self.lis[i][1][j])
            self.lis[i].append(u)

    def distinct_words(self, book_title):
        index = self.binary_search_book(self.lis, book_title)
        if index is not None:
            return self.lis[index][2]
        return   

    def count_distinct_words(self, book_title):
        index = self.binary_search_book(self.lis, book_title)
        if index is not None:
            return len(self.lis[index][2])
        return 0  # Return 0 if book title is not found

    def search_keyword(self, keyword):
        result = []
        for book in self.lis:
            if self.binary_search_word(book[1], keyword) is not None:
                result.append(book[0])
        return result


    def merge(self, s1, s2, s):
        i = j = 0
        while i + j < len(s):
            if j == len(s2) or (i < len(s1) and s1[i] < s2[j]):
                s[i + j] = s1[i]
                i += 1
            else:
                s[i + j] = s2[j]
                j += 1
        return s

    def mergesort(self, s):
        n = len(s)
        if n <= 1:
            return s
        mid = n // 2
        s1 = s[:mid]
        s2 = s[mid:]
        s1 = self.mergesort(s1)
        s2 = self.mergesort(s2)
        return self.merge(s1, s2, s)
    def merge1(self, s1, s2, s):
        i = j = 0
        while i + j < len(s):
            if j == len(s2) or (i < len(s1) and s1[i][0] < s2[j][0]):
                s[i + j] = s1[i]
                i += 1
            else:
                s[i + j] = s2[j]
                j += 1
        return s

    def mergesort1(self, s):
        n = len(s)
        if n <= 1:
            return s
        mid = n // 2
        s1 = s[:mid]
        s2 = s[mid:]
        s1 = self.mergesort1(s1)
        s2 = self.mergesort1(s2)
        return self.merge1(s1, s2, s)

    def binary_search_book(self, a, b):
        low, high = 0, len(a) - 1
        while low <= high:
            mid = (low + high) // 2
            if a[mid][0] == b:
                return mid
            elif a[mid][0] < b:
                low = mid + 1
            else:
                high = mid - 1
        return None

    def binary_search_word(self, a, b):
        low, high = 0, len(a) - 1
        while low <= high:
            mid = (low + high) // 2
            if a[mid] == b:
                return mid
            elif a[mid] < b:
                low = mid + 1
            else:
                high = mid - 1
        return None

    def print_books(self):
        for book in self.lis:
            words_str = " | ".join(book[2])
            print(f"{book[0]}: {words_str}")



class JGBLibrary(DigitalLibrary):
    # IMPLEMENT ALL FUNCTIONS HERE
    def __init__(self, name, params):
        '''
        name    : "Jobs", "Gates" or "Bezos"
        params  : Parameters needed for the Hash Table:
            z is the parameter for polynomial accumulation hash
            Use (mod table_size) for compression function
            
            Jobs    -> (z, initial_table_size)
            Gates   -> (z, initial_table_size)
            Bezos   -> (z1, z2, c2, initial_table_size)
                z1 for first hash function
                z2 for second hash function (step size)
                Compression function for second hash: mod c2
        '''
        self.name = name
        self.params = params
        if self.name  == "Jobs":
            self.books = ht.HashMap('Chain',params)
        elif self.name == "Gates":
            self.books = ht.HashMap('Linear',params)
        else:
            self.books = ht.HashMap('Double',params)
    
    def add_book(self, book_title, text):
        if self.name  == "Jobs":
            x = ht.HashSet('Chain',self.params)
        elif self.name  == "Gates":
            x = ht.HashSet('Linear',self.params)
        else:
            x = ht.HashSet('Double',self.params)
        for i in text:
            x.insert(i)
        self.books.insert((book_title,x))
        

    def distinct_words(self, book_title):
        r = self.books.find(book_title)
        l = []
        if r is not None:
            for i in r.table:
                if i is not None:
                    # print(i)
                    if isinstance(i,list):
                        l.extend(i)
                    else:
                        l.append(i)
        return l
    
    def count_distinct_words(self, book_title):
        a = self.books.find(book_title)
        if a:
            return a.distinct
    
    def search_keyword(self, keyword):
        l =[]
        for  i in self.books.table:
            if i is not None:
                if isinstance(i,list):
                    for j in i:
                        if j[1].find(keyword) is True:
                            l.append(j[0])
                else:
                    if i[1].find(keyword) is True:
                        l.append(i[0])
        return l
    
    def print_books(self):
        for  i in self.books.table:
            if i is not None:
                if isinstance(i,list):
                    for  j in i:
                        a = j[1].__str__()
                        print(j[0]+': '+a)
                else:
                    a = i[1].__str__()
                    print(i[0]+': '+a)
        

# class JGBLibrary(DigitalLibrary):
#     def __init__(self, name, params):
#         self.name = name
#         self.params = params
#         if self.name == "Jobs":
#             self.books = ht.HashMap('Chain', params)
#         elif self.name == "Gates":
#             self.books = ht.HashMap('Linear', params)
#         else:
#             self.books = ht.HashMap('Double', params)

#     def add_book(self, book_title, text):
#         if self.name == "Jobs":
#             word_set = ht.HashSet('Chain', self.params)
#         elif self.name == "Gates":
#             word_set = ht.HashSet('Linear', self.params)
#         else:
#             word_set = ht.HashSet('Double', self.params)
        
#         # Insert each word into the HashSet
#         for word in text:
#             word_set.insert(word)
        
#         # Insert book with title as key and word_set as value
#         self.books.insert((book_title, word_set))

#     def distinct_words(self, book_title):
#         word_set = self.books.find(book_title)
#         if word_set is None:
#             return []  # Book not found
        
#         distinct_words_list = []
#         for item in word_set.table:
#             if item is not None:  # Check for non-empty slots
#                 if isinstance(item, list):
#                     distinct_words_list.extend(item)
#                 else:
#                     distinct_words_list.append(item)
#         return distinct_words_list

#     def count_distinct_words(self, book_title):
#         word_set = self.books.find(book_title)
#         if word_set is None:
#             return  # Book not found
#         return word_set.num_elements  # Ensure HashSet tracks the count

#     def search_keyword(self, keyword):
#         result = []
#         for entry in self.books.table:
#             if entry is not None:
#                 if isinstance(entry, list):  # Handle chaining
#                     for book_entry in entry:
#                         if book_entry[1].find(keyword) is not False:
#                             result.append(book_entry[0])
#                 elif entry[1].find(keyword) is not False:  # Single entry
#                     result.append(entry[0])
#         return result

#     def print_books(self):
#         for entry in self.books.table:
#             if entry is not None:
#                 if isinstance(entry, list):  # Handle chaining
#                     for book_entry in entry:
#                         print(f"{book_entry[0]}: {book_entry[1]}")
#                 else:
#                     print(f"{entry[0]}: {entry[1]}")
# library = JGBLibrary("Jobs", (31, 11))  # Assuming parameters for polynomial hash

# # Adding a sample book with duplicate words
# library.add_book("Sample", ["apple", "banana", "apple", "cherry"])

# # Check if words are distinct in the HashSet associated with the book title
# distinct_words = library.distinct_words("Sample")
# print("Distinct words in 'Sample':", distinct_words)
