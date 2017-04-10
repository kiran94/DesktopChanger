# Service for reading and writing to IO.
class fileIOService:
    
    #Reads from a file and returns file object.  
    def read(self, filename):
         fileObject = open(filename, 'r')
         data = fileObject.read()
         fileObject.close()

         return data

    #Returns a file object for writing. 
    def write(self, filename, data):
        fileObject = open(filename, 'w+')
        fileObject.write(data)
        fileObject.close()