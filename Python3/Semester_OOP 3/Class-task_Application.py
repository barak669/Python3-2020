class Application:

    def __init__(self, app_name, app_price=7, app_size=300, rating=5):
        self.app_name=app_name
        self.app_price=app_price
        self.app_size=app_size
        self.rating=rating
    
    def print_info(self):
        print(f"app_name: {self.app_name}, app_prise {self.app_price}, app_size: {self.app_size}, rating: {self.rating}")

    @property
    def app_name(self):
        return self.__app_name
    
    @property
    def app_price(self):
        return self.__app_price
    
    @property
    def app_size(self):
        return self.__app_size
    
    @property
    def rating(self):
        return self.__rating

    @app_price.setter
    def app_price(self,appPrice):
        self.__app_price=app_price if(app_price>0) else 750
    
    @app_name.setter
    def app_name(self,app_name):
        self.__app_name=app_name

    @app_size.setter
    def app_size(self,app_size):
            self.__app_size=app_size if(app_price>=0) else 4
    
    @rating.setter
    def rating(self,rating):
        self.__rating=rating if(rating>=1 and rating<=5) else 1