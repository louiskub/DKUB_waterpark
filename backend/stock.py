from service import Cabana, Locker, Ticket, Towel
from datetime import date, timedelta

from service import Cabana, Locker, Ticket, Towel
from datetime import date, timedelta

class Stock:
    def __init__(self):
        self.__cabana_list = create_cabana()
        self.__locker_list = create_locker()
        self.__ticket_list = create_ticket()
        self.__towel = Towel()

    @property
    def cabana_list(self):
        return self.__cabana_list
    
    @property
    def locker_list(self):
        return self.__locker_list
    
    @property
    def ticket_list(self):
        return self.__ticket_list
    
    @property
    def towel(self):
        return self.__towel

class DailyStock(Stock):
    def __init__(self, date):
        Stock.__init__(self)
        self.__date = date
    
    @property
    def date(self):
        return self.__date
    
    def update_item(self, item, amount):
        if isinstance(item, Cabana):
            item.update_status('A')
        elif not isinstance(item, Ticket):
            item.update_status('A', amount)

    def is_available(self, item, amount):
        if isinstance(item, Cabana):
            return not item.is_reserve # If reserved = Not available
        elif not isinstance(item, Ticket):
            return item.remaining_amount >= amount
        return True
    
    def get_cabana_in_zone(self, cabana_zone):
        print("ok")
        for zone in range (len(self.cabana_list)):
            if cabana_zone == self.cabana_list[zone][0].zone:
                return self.cabana_list[zone]
        return None

def create_locker():
    return [Locker('M', 80), Locker('L', 20)]

def create_cabana():
    wave_pool_zone = []
    wave_pool_zone.append(Cabana('W01', 'S', 'Wave Pool')) # Wave Pool Zone
    wave_pool_zone.append(Cabana('W02', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W03', 'M', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W04', 'M', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W05', 'M', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W06', 'M', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W07', 'M', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W08', 'M', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W09', 'M', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W10', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W11', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W12', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W13', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W14', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W15', 'L', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W16', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W17', 'M', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W18', 'M', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W19', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W20', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W21', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('W22', 'M', 'Wave Pool'))
    wave_pool_zone.append(Cabana('P05', 'S', 'Wave Pool'))
    wave_pool_zone.append(Cabana('P06', 'S', 'Wave Pool'))

    activity_relax_zone = []
    activity_relax_zone.append(Cabana('P01', 'S', 'Activity and Relax')) # Activity and Relax Zone
    activity_relax_zone.append(Cabana('P02', 'S', 'Activity and Relax'))
    activity_relax_zone.append(Cabana('P03', 'M', 'Activity and Relax'))
    activity_relax_zone.append(Cabana('P04', 'M', 'Activity and Relax'))

    hill_zone = []
    hill_zone.append(Cabana('H01', 'S', 'Hill')) # Hill Zone
    hill_zone.append(Cabana('H02', 'S', 'Hill'))
    hill_zone.append(Cabana('H03', 'S', 'Hill'))
    hill_zone.append(Cabana('H04', 'M', 'Hill'))
    hill_zone.append(Cabana('H05', 'M', 'Hill'))
    hill_zone.append(Cabana('H06', 'M', 'Hill'))
    hill_zone.append(Cabana('H07', 'S', 'Hill'))
    hill_zone.append(Cabana('H08', 'M', 'Hill'))
    hill_zone.append(Cabana('H09', 'M', 'Hill'))
    hill_zone.append(Cabana('H10', 'S', 'Hill'))
    hill_zone.append(Cabana('H11', 'M', 'Hill'))

    family_zone = []
    family_zone.append(Cabana('K01', 'M', 'Family')) # Family Zone
    family_zone.append(Cabana('K02', 'S', 'Family'))
    family_zone.append(Cabana('K03', 'L', 'Family'))
    family_zone.append(Cabana('K04', 'S', 'Family'))
    family_zone.append(Cabana('K05', 'S', 'Family'))
    family_zone.append(Cabana('K06', 'M', 'Family'))
    family_zone.append(Cabana('K07', 'M', 'Family'))
    family_zone.append(Cabana('K08', 'M', 'Family'))
    family_zone.append(Cabana('K09', 'M', 'Family'))
    family_zone.append(Cabana('K10', 'S', 'Family'))
    family_zone.append(Cabana('K11', 'L', 'Family'))
    family_zone.append(Cabana('K12', 'S', 'Family'))
    family_zone.append(Cabana('K13', 'S', 'Family'))
    family_zone.append(Cabana('K14', 'M', 'Family'))
    family_zone.append(Cabana('K15', 'M', 'Family'))
    family_zone.append(Cabana('K16', 'S', 'Family'))
    family_zone.append(Cabana('K17', 'M', 'Family'))
    
    cabana_list = [wave_pool_zone, activity_relax_zone, hill_zone, family_zone]
    return cabana_list

def create_ticket():
    ticket_list = []
    
    # Solo Ticket
    ticket_list.append(Ticket('Full Day', 1, 699))
    ticket_list.append(Ticket('Senior with Slides', 1, 599)) # >= 60 y.o. and want to play slides
    ticket_list.append(Ticket('Child', 1, 0))
    ticket_list.append(Ticket('Senior / Pregnant / Disabled', 1, 0)) # including pregnant and disabled 

    # Group Ticket
    ticket_list.append(Ticket('Group package for 4 people', 4, 2599))
    ticket_list.append(Ticket('Group package for 6 people', 6, 3779))
    ticket_list.append(Ticket('Group package for 8 people', 8, 4879))
    ticket_list.append(Ticket('Group package for 10 people', 10, 5999))
    return ticket_list

    
    # def get_cabana_in_zone(self, cabana_zone):
    #     for zone in range (len(self.cabana_list)):
    #         for cabana in self.cabana_list[zone]:
    #             if cabana_zone == cabana.zone:
    #                 return self.cabana_list[zone]
    #             zone += 1        
    #     return None
