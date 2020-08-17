class Mobile:

    def __init__(self,virsion_num, isAndroid, memory_size):
        self.virsion_num=virsion_num
        self.isAndroid=isAndroid
        self.memory_size=memory_size
        self.used_memory=0
        self.app_array=[]

    def print_info(self):
        print(f" virsion_num: {self.virsion_num}, isAndroid {self.isAndroid}, memory_size: {self.memory_size}, app_array: {self.app_array}")

    def add_app(self,app):
        if(app.app_size + used_memory > memory_size):
            print("sorry")
        else:
            self.used_memory+=app.app_size
            self.app_array.append(app)

    def is_memory_full(self):
        return self.used_memory<self.


    @property
    def virsion_num(self):
        return self.__virsion_num
    
    @property
    def isAndroid(self):
        return self.__isAndroid
    
    @property
    def memory_size(self):
        return self.__memory_size
    
    @property
    def app_array(self):
        return self.__app_array

    @virsion_num.setter
    def virsion_num(self,virsion_num):
        self.__virsion_num=virsion_num if(virsion_num>1) else 1

    @isAndroid.setter
    def isAndroid(self,isAndroid):
        self.__isAndroid=isAndroid
    
    @memory_size.setter
    def memory_size(self,memory_size):
        self.__memory_size=memory_size if(memory_size>0) else 4
    
    @age.setter
    def appArray(self,appArray):
        self.__appArray=appArray

    def printMobileInfo :
        print(f"virsionNum is: {self.virsionNum}, isAndroid: {self.isAndroid}, memory size is:{self.memorySize},app is: {self.appArray}")