from datetime import datetime, date
import string                                                   # NEEDS DEBUGGING

now = datetime.now()

today = date.today()

class Componants(object):
    
    def __init__(self, fp):
        with open (fp, 'r') as f:
            self.lines = f.readlines()
            f.close()

        self.line0 = self.lines[0].split()
        self.line1 = self.lines[1].split()
        self.line2 = self.lines[2].split()

        # Line 0

        self.satellite_name = self.line0

        # Line 1

        self.catalogNum = self.line1[1][0:4]
        self.classification = str(self.line1[1][5]) # spacecraft self.classification 
        if self.classification == 'U':
            self.classification = "unclassified"
        if self.classification == 'C':
            self.classification == "classified"
        if self.classification == 'S':
            self.classification == "secret"
        self.int_desig = int(self.line1[2][0:2]) # (last two digits of launch year)
        if self.int_desig > int((str(today.year).lstrip('2').lstrip('0'))):
            self.launch_year = int(1900 + self.int_desig)
        else:
            self.launch_year = int(2000 + self.int_desig)

        self.launch_num = int((self.line1[2][2:5])) # luanch number of year
        if self.launch_num > 100:
            self.launch_num = self.launch_num.lstrip('0')
        if len(self.line1[2]) < 6:       # no launch part
            self.launch_part = "None"
        else: 
            self.launch_part = self.line1[2][5:] #might be more than one unit
            if len(self.launch_part) == 1:
                self.launch_part_num = (string.ascii_uppercase.index(self.launch_part) + 1) #gives the index of the launch piece in terms of its position in the alphabet
        

        # EPOCH
        self.epoch = self.line1[3]
        self.year_idx = int(self.epoch[0:2])

        if self.year_idx > int((str(today.year).lstrip('2').lstrip('0'))):
            self.year = int(1900 + self.year_idx)
        else:
            self.year = int(2000 + self.year_idx)
        epochSplit = str(self.epoch[2:]).split('.')

        self.day = int(epochSplit[0])

        self.month = int(round((self.day)/30))

        time0 = epochSplit[1]

        power = int(len(str(time0)))
        t = (float(time0)*10**-power)*24

        self.time_hour = str(t)[0:2]

        self.time_minute = round((float(t)-float(self.time_hour))*60)

        self.time = (f"{self.time_hour}:{self.time_minute}")

        self.date_UK = (self.time, self.day, self.month, self.year)

#----------------------------------------------------------------------------------------

        self.ballistic_coeff = self.line1[3][15:24] # first derivative of mean motion
        self.ballistic_coeff_second_deriv = self.line1[4]
        self.radiation_press_coef = self.line1[5]
        self.ephemeris_type = self.line1[6]
        self.element_set_num = self.line1[7][0:-1]
        self.checkSum = self.line1[7][-1] # Not sure what this is

        # Line 2

        self.inclination = self.line2[2]
        self.right_ascension = self.line2[3]
        self.eccentricity = self.line2[4]
        self.arg_of_perigee = self.line2[5]
        self.mean_anomaly = self.line2[6]
        self.mean_motion = self.line2[7][0:-6] # revs per day
        self.rev_num = self.line2[7][-6:]# at epoch
        #checkSum2 = checkSum