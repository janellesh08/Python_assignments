from datetime import datetime
from datetime import date



class Pooltable:
    def __init__(self, tblnumber) -> None:
        self.tblnumber = tblnumber
        self.is_occupied = False
        self.start_time = None
        self.stop_time = None
        self.total_time = None


    #def save_to_file(self):
       # with open("pool_tabels.txt", "a")as file:
        #    for table in pool_tables_arr: 
         #       file.write(f"\nTable number: {self.tblnumber} --- Start time: {self.start_time} --- Total time: {self.total_time.total_seconds()/60} \n")

    #def save_to_file(self):
     #   day = str(date.today)
      #  ext = ".txt"
       # file_name = day + ext
        #total_time = self.start_time + self.stop_time
        #with open(file_name, "a") as file:
         #   file.write(f"\nTable number: {self.tblnumber} --- Start time: {self.start_time} --- Total time: {self.total_time.total_seconds()/60} \n")
             

    def checking_out(self):
        self.is_occupied = True
        self.start_time = datetime.now()
        

    def checking_in(self):
        self.is_occupied = False
        self.stop_time = datetime.now()
        self.total_time = self.stop_time - self.start_time 
        self.total_time_in_min = self.total_time.total_seconds() / 60 
        #self.save_to_file()
        

        



    

    