import time
import csv
import os
import pandas as pd

class TimeExecution(object):
    
    time = [[0], [0], [0], [0], [0], [0], [0]]
    
    def timeCreateUser(self, t1, t2):
        self.time[0].append(t2-t1)
    
    def timeFindByGraduation(self, t1, t2):
        self.time[1].append(t2-t1)

    def timeFindByAbilities (self, t1, t2):
        self.time[2].append(t2-t1)
    
    def timeModifyAbilitie(self, t1, t2):
        self.time[3].append(t2-t1)
    
    def timeFindByExperience(self, t1, t2):
        self.time[4].append(t2-t1)

    def timeListAllUsers(self, t1, t2):
        self.time[5].append(t2-t1)

    def timeFindByEmail(self, t1, t2):
        self.time[6].append(t2-t1)

    def exportData(self, file):
        # with open(file+".csv", 'w', newline="") as csvfile:
        #     spamwriter = csv.writer(csvfile, delimiter=';', quoting=csv.QUOTE_MINIMAL)
        #     spamwriter.writerow(['CreateUser', 'FindByGraduation', 'FindByAbilities', 'ModifyAbilitie', 'FindByExperience', 'ListAllUsers', 'FindByEmail'])
            
        #     for coluna in self.time:
        #         spamwriter.writerow(coluna)

        columns = ['CreateUser', 'FindByGraduation', 'FindByAbilities', 'ModifyAbilitie', 'FindByExperience', 'ListAllUsers', 'FindByEmail']

        
        # while(len(self.time[0]) != 21):
        #     self.time[0].append(0)

        data = {'CreateUser': self.time[0],
                'FindByGraduation': self.time[1],
                'FindByAbilities': self.time[2],
                'ModifyAbilitie': self.time[3],
                'FindByExperience': self.time[4],
                'ListAllUsers': self.time[5],
                'FindByEmail': self.time[6]
                }
        
        df = pd.DataFrame(data)

        df.to_csv("src/data/" + file + '.csv')

        print("Foi criado o arquivo " + file + ".csv")
