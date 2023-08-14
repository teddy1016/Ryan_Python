# Create a class that can be called to fix the formatting of the csv in this dir (sample.csv) and return it as a df. 
# BONUS: Return the data grouped in the best manner you see fit.

import pandas as pd
import re
import locale

class CsvToDf():
    #Initializer which loading csv data using inputed filename
    def __init__(self, filename):
        self.filename = filename
        self.basic_data = pd.read_csv (filename)
        self.outputData = self.basic_data.copy()
        self.data_count = self.basic_data['Master'].count()
    #function which fix formatting issues
    def processCSV(self, field, fixMod):
        #This mode is for fixing currency issue
        if fixMod == 0: 
                
            for i in range(0, self.data_count):
                decimal_point_char = locale.localeconv()['decimal_point']
                clean = re.sub(r'[^0-9'+decimal_point_char+r']+', '', str(self.basic_data[field][i]))
                if clean != '':
                    value = float(clean)
                else:
                    value = 0.0
                self.outputData.loc[i, field] = '$' +str(value)
            
        #This mode is for unique ID issue
        #Just re-indexing the ID from 1 to end
        if fixMod == 1: 
        
            for i in range(0, self.data_count):
                self.outputData.loc[i, field] = i + 1



    #function which fix formatting issues
    def GroupData(self, field, groupMod, criteria):
        #This group mode is for equals (=)
        if groupMod == '=': 
            for i in range(0, self.data_count):
                #self.outputData.get
                if self.basic_data[field][i] != criteria:
                    self.outputData = self.outputData.drop(i)
                    print(self.basic_data[field][i])
                    #self.outputData.loc[i] = {}
        #group for greaters (>)
        if groupMod == '>': 
            for i in range(0, self.data_count):
                #self.outputData.get
                if self.basic_data[field][i] <= criteria:
                    self.outputData = self.outputData.drop(i)
                    print(self.basic_data[field][i])
                    #self.outputData.loc[i] = {}
        #group for greaters (<)
        if groupMod == '<': 
            for i in range(0, self.data_count):
                #self.outputData.get
                if self.basic_data[field][i] >= criteria:
                    self.outputData = self.outputData.drop(i)
                    print(self.basic_data[field][i])
                    #self.outputData.loc[i] = {}
        #group for greaters (<)
        if groupMod == '<=': 
            for i in range(0, self.data_count):
                #self.outputData.get
                if self.basic_data[field][i] > criteria:
                    self.outputData = self.outputData.drop(i)
                    print(self.basic_data[field][i])
                    #self.outputData.loc[i] = {}
        #group for greaters (<)
        if groupMod == '>=': 
            for i in range(0, self.data_count):
                #self.outputData.get
                if self.basic_data[field][i] < criteria:
                    self.outputData = self.outputData.drop(i)
                    print(self.basic_data[field][i])
                    #self.outputData.loc[i] = {}
        
    def Output(self):
        
        print(self.outputData) 




# Class testing codes

formatFixer = CsvToDf('sample.csv')

#Fix revenue field's currency issue and the others follows.
formatFixer.processCSV('Revenue', 0)
formatFixer.processCSV('Profit', 0)
formatFixer.processCSV('Cost', 0)
formatFixer.processCSV('Expense', 0)
formatFixer.processCSV('Income', 0)
formatFixer.processCSV('Price', 0)
formatFixer.processCSV('Salary', 0)
formatFixer.processCSV('Investment', 0)

#Fix ID field's unique-id issue.
formatFixer.processCSV('ID', 1)

#Group data using Master
formatFixer.GroupData('Master', '>', 164981123)

#Output fixed data
formatFixer.Output()

#Processing basic-data to correct the format.


#Grouping processed (format fixed) data using certain criteria.


