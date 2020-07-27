class Cinema:

    def __init__(self, name,num_of_chairs,open_hour,close_hour):
        self.name=nameself.num_of_chairs=num_of_chairs
        self.open_hour=open_hour
        self.close_hour=close_hour

    def amount_of_open_hours(self):
        return self.close_hour-self.open_hour

    def print_info(self):
        return f*name:{self.name}, open_hour: {self.}

    @property
    def num_of_chairs(self):
        return self.__num_of_chairs


    @num_of_chairs.setter
    def num_of_chairs(self, num):
        self.__num_of_chairs = num if num>0 else 0

    @property
    def open_hour(self):
        return self.__open_hur


    @open_huor.setter
    def open_huor(self, hour):
        self.__open_huor = hour if hour>6 and hour<12 else 6

    @property
    def close_hour(self):
        return self.__close_hour


    @close_hour.setter
    def close_hour(self, hour):
        self.__close_hour = hour if hour>18 and hour<23 else 6


