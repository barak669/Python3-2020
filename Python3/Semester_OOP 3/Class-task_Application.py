class Application:

    def __init__(self,appName, appPrice, appSize, rating):
        self.appName=appName
        self.appPrice=appPrice
        self.appSize=appSize
        self.rating=rating


    @property
    def appName(self):
        return self.__appName
    
    @property
    def appPrice(self):
        return self.__appPrice
    
    @property
    def appSize(self):
        return self.__appSize
    
    @property
    def rating(self):
        return self.__rating

    @age.setter
    def appPrice(self,appPrice):
        if(appPrice>0):
            self.__appPrice=appPrice
    
    @age.setter
    def appName(self,appName):
        self.__appName=appName

    @age.setter
    def appSize(self,appSize):
        self.__appSize=appSize
    
    @age.setter
    def rating(self,rating):
        if(rating>=1 and rating<=5):
            self.__rating=rating