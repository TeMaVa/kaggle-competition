# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
import csv

# TÄLÄÄ HETKELLÄ KOKO TIETÄÄKSEMME 1931, sillä VAR_218 ja VAR_240 puuttuvat

# Initialize the helper variable for csv
variable_count = 1933
indices_string = [str(x) for x in range(1,variable_count)]
indices_string.remove('218')
indices_string.remove('240')
variable_count = variable_count - 2

for i in range(len(indices_string)):
    indices_string[i] = indices_string[i].rjust(4,'0')
    globals()['VAR_%s' % indices_string[i]] = []
    

indices_string.insert(0,'ID')



with open('train.csv') as csvfile:
     reader = csv.DictReader(csvfile)
     i = 1
     for row in reader:
         for column_i in range(1,variable_count):
             globals()['VAR_%s' % indices_string[column_i]].append(str(row['VAR_%s'% indices_string[column_i]]))
         print("Finished row " + str(i))
         i = i + 1
