class Mobile:

    def __init__(self,virsionNum, isAndroid, memorySize, appArray):
        self.virsionNum=virsionNum
        self.isAndroid=isAndroid
        self.memorySize=memorySize
        self.appArray=appArray


    @property
    def virsionNum(self):
        return self.__virsionNum
    
    @property
    def isAndroid(self):
        return self.__isAndroid
    
    @property
    def memorySize(self):
        return self.__memorySize
    
    @property
    def appArray(self):
        return self.__appArray

    @age.setter
    def virsionNum(self,virsionNum):
        self.__virsionNum=virsionNum

    @age.setter
    def isAndroid(self,isAndroid):
        self.__isAndroid=isAndroid
    
    @age.setter
    def memorySize(self,memorySize):
        self.__memorySize=memorySize
    
    @age.setter
    def appArray(self,appArray):
        self.__appArray=appArray