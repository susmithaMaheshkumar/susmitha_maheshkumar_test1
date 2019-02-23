


class lrucache:

    def __init__(self, size):
        self.size = size
        self.cache = {}
        self.usageCounter = {}
    
    #returns 1 if key exists
    def checkIfkeyExists(self,queryKey):
        if queryKey in self.cache:
            return True
        else: 
            return False

    def checkIfCacheIsFull(self):
        if(len(self.cache) == self.size):
            return True
        else:
            return False
        
    def getsize(self):
        return self.size

    def getValue(self,key):
        if key in self.cache:
            self.usageCounter[key] += 1
            return self.cache[key]
        else:
            return -1

    def getLeastUsedKey(self):
        minimum = min(self.usageCounter.values())
        for key,val in self.usageCounter:
            if val == minimum:
                return key
        return None


    def setValue(self,key, value):
        #chjeck if key exists
        retValue = self.checkIfkeyExists(key)
        if retValue is True:
            
           self.cache[key] = value
        else:
            #check if buffer is full
            if self.checkIfCacheIsFull():
                #find which one to replace
                #find least used entry
                lruKey = self.getLeastUsedKey()
                if lruKey is None:
                    pass
                else:
                    self.cache[lruKey] = value
            else:
                #insert            
               self.cache[key] = value
        #decide whther you want to delete an item
        self.cache[key] = value
        pass
    

    def clearAll(self):
        self.cache.clear()

    def deleteValue(self,key):
        self.cache.pop(key)
