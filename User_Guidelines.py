from keyvaluedb import keyvalue
#importing keyvalue class from keyvaluedb.py file

a=keyvalue()
#creating a object of the class type "keyvalue" without arguments
#So the path and filename are set to default ones
#We can do create, read, modify and delete operations to a key value data store 
#using this object

a=keyvalue(path)
#creating a object with passing one argument
#This argument is considered as path
#filename is not set here. Hence a default file name is used

a=keyvalue(path,filename)
#creating a object with passing two arguments
#Here first argument is the file path and second argument is the filename
#Since the datastore we create is of type JSON use a filename ending with ".json"


a.create(key,value,time-to-live)
#We created a New entry in our keyvalue database
#Here the first argument is the "key" that is of type string capped at 32 characters
#Key should not contain any characters other than a-z and A-Z
#Second argument is a "JSON object" limited at a maximum size of 16Kb 
#Use single quotes outside of the JSON object since JSON contains double quotes which leads to error.
#Third argument is the time-to-live property. This is optional.
#If this is set then that entry could be accessed only for the mentioned seconds from the time of creation
#If this is not set or set to zero then the lifetime of the entry is infinite.

a.read(key)
#This reads the JSON object that is associated with this key in the datastore and returns it.

a.modify(key,value)
#This function is used to modify the value of the entry in the datastore using the key associated with it.

a.delete(key)
#This function deletes an data entry from the datastore that matches with the key passed to this function.
