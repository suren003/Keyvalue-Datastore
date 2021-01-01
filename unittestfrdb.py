import unittest 
from keyvaluedb import keyvalue  

class TestStringMethods(unittest.TestCase): 
      
    def setUp(self): 
        pass
      
    def test_db_creation_1(self): 
        a=keyvalue()
        self.assertEqual( a.create("aber",'{"ab":123}'), "Data added to the Datastore Successfully")
    
    def test_db_creation_2(self): 
        a=keyvalue()
        self.assertEqual( a.create("aber",'{"ab":123}'), "Error : Key already exist")

    def test_db_creation_3(self): 
        a=keyvalue()
        self.assertEqual( a.create(12,'{"ab":123}'), "Error : Key contains unrecognised characters")
    
    def test_db_creation_4(self): 
        a=keyvalue()
        self.assertEqual( a.create("ajsk",23), "Value is not a JSON Object")
    
    def test_db_creation_5(self): 
        a=keyvalue()
        self.assertEqual( a.create("ajsk",'{"ab":123}',200), "Data added to the Datastore Successfully")
    
    def test_db_creation_6(self): 
        a=keyvalue()
        self.assertEqual( a.create("ajskajskajskajskajskajskajskajskajskajskajskajsk",'{"ab":123}'), "Error : Length of Key is more than 32 Characters")

    def test_db_deletion_1(self):
        a=keyvalue()
        self.assertEqual(a.delete("aber"),"Key deleted Successfully")
    
    def test_db_deletion_2(self):
        a=keyvalue()
        self.assertEqual(a.delete("wac"),"Error : Key doesn't exist")
    
    def test_db_read_1(self):
        a=keyvalue()
        self.assertEqual(a.read("ajsk"),'{"ab":123}')
    
    def test_db_read_2(self):
        a=keyvalue()
        self.assertEqual(a.read("wac"),"Error : Key doesn't exist")

    def test_db_modify_1(self):
        a=keyvalue()
        a.create("ajskk",'{"ab":123123}')
        self.assertEqual(a.modify("ajskk",'{"ab":123123}'),"Data modified succesfully")
    
    def test_db_modify_2(self):
        a=keyvalue()
        self.assertEqual(a.modify("wac",'{"ab":123123}'),"Error : Key doesn't exist")
        
    


    
    

    

    
      
  
    
  
if __name__ == '__main__': 
    unittest.main() 