import sys
import os
import threading 
from threading import*
import time
import json
from pathlib import Path

class keyvalue:
    def __init__(self, *args):
        if len(args) == 2:
            if not(os.path.exists(args[0])):
                print("Path doesn't Exist")
            else:
                self.path=args[0]
                if args[1][-5:]==".json":
                    self.filename=args[1]
                    print("Path and Filename set successfully")
                else:
                    print("The entired filename is not a json format file name")
                
            
        elif len(args) == 1:
            if not(os.path.exists(self.path)):
                print("Path doesn't Exist")
            else:
                print("Path set successfully")
                self.path=args[0]
                self.filename="db.json"
        else:
            self.home = str(Path.home())
            self.path=os.path.join(self.home,"keyfiledatabase")
            self.filename="db.json"
            print("Path and filename set to default")

    def save(self,a):
        with open(self.filename, "w") as outfile:  
            json.dump(a, outfile)
        
    def read(self,key):
        if os.path.exists(os.path.join(self.path,self.filename)):
            
            os.chdir(self.path)
            f = open(self.filename,"r")
            a = json.load(f)
            f.close()
            if key in a:
                if a[key][1]==0 or time.time()<=a[key][1]:
                    return a[key][0]
                else:
                    return "Timeout"
            else:
                return "Error : Key doesn't exist"
        else:
            return "Error : Keyvalue Data Store Empty"

    def create(self,key,value,timed=0):
        key=str(key)
        if os.path.exists(os.path.join(self.path,self.filename)):
            
            os.chdir(self.path)
            
            f=open(self.filename,)
            try:
                a=json.load(f)
                f.close()
            except:
                a={}
        else:
            if not(os.path.exists(self.path)):
                os.mkdir(self.path)
            
            os.chdir(self.path)
            
            a={}
        temp={}
        if key in a:
            return "Error : Key already exist"
        else:
            if key.isalpha():
                if timed==0:
                    lis=[value,timed]
                else:
                    lis=[value,time.time()+timed]
                temp={key:lis}
                if len(key)<=32:
                    if sys.getsizeof(a)+sys.getsizeof(temp)<(1024*1020*1024):
                        if sys.getsizeof(value)<=(16*1024*1024):
                            try:
                                json_object = json.loads(value)
                                check=True
                            except:
                                check=False
                            if check:
                                f=open(self.filename,"w")
                                a.update(temp)
                                self.save(a)
                                f.close()
                               
                                return "Data added to the Datastore Successfully"
                            else:
                                return "Value is not a JSON Object"
                        else:
                            return "Error : Size of JSON Object is more than 16Kb"
                    else:
                        return "Error : Size of Keyvalue Datastore exceeds 1GB"
                else:
                    return "Error : Length of Key is more than 32 Characters"
            else:
                return "Error : Key contains unrecognised characters"                       

    def delete(self,key):
        if os.path.exists(os.path.join(self.path,self.filename)):
          
            os.chdir(self.path)
            f = open(self.filename,)
            a = json.load(f)
            f.close()
            if key in a:
                if a[key][1]==0 or time.time()<=a[key][1]:
                    a.pop(key)
                    self.save(a)
                    return "Key deleted Successfully"
                else:
                    return "Timeout"
            else:
                return "Error : Key doesn't exist"
        else:
            return "Error : Keyvalue Data Store Empty"

        
            
    def modify(self,key,value):
        if os.path.exists(os.path.join(self.path,self.filename)):
         
            os.chdir(self.path)
            f = open(self.filename,"r")
            a = json.load(f)
            f.close()
            if key in a:
                if a[key][1]==0 or time.time()<=a[key][1]:
                    try:
                        json_object = json.loads(value)
                        check=True
                    except:
                        check=False
                    if check:    
                        a[key][0]=value
                        self.save(a)
                        return "Data modified succesfully"
                    else:
                        return "Value is not a JSON Object"
                else:
                    return "Timeout"
            else:
                return "Error : Key doesn't exist"
        else:
            return "Error : Keyvalue Data Store Empty"