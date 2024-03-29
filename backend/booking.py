class Booking:
    __ID = 100000

    def __init__(self, member_id, order, booking_date):
        self.__id = Booking.__ID
        self.__member_id = member_id
        self.__order = order
        self.__booking_date = booking_date
        self.__status = False
        Booking.__ID += 1
    
    @property
    def id(self):
        return self.__id
    
    @property
    def order(self):
        return self.__order
    
    @property
    def member_id(self):
        return self.__member_id
    
    @property
    def booking_date(self):
        return self.__booking_date
    
    @booking_date.setter
    def booking_date(self, date):
        self.__booking_date = date
    @order.setter
    def order(self, order):
        self.__order = order

    def update_status(self):
        self.__status = True
        return "Done"

    def to_dict(self):
        return {
            "booking_id": self.__id,
            "member_id": self.__member_id,
            "order": self.__order.to_dict(),
            "booking_date": self.__booking_date,
            "status": self.__status
        }