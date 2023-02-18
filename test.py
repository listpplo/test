from nsetools import Nse 
import datetime
import os
import time 

# Definf the nse object 
nse = Nse()
#getting the corret date and time


time_stamp = datetime.datetime.now()

# creating and reading the file

#name1 = "file date -- "
#name = name1 + str(time_stamp)
lst_file = open("list.txt","r")
data_file = open("data.txt", "a+")

data_file.write("************************************************************************\n")
data_file.write("Time : "+str(datetime.datetime.now())+"\n")
data_file.write("________________________________________________________________________\n")
#print(nse.get_quote("INFY"))
symbols = lst_file.readlines()
print(symbols)
print(time.time())
for symbol in symbols:
  sym = symbol.split("\n")
  #print(sym)
  data = nse.get_quote(sym[0])
  data_file.write(symbol)
  data_file.write("Quantity selled : "+ str(data["totalSellQuantity"])+"\n")
  data_file.write("Total Quantity Buyed : " +str(data["totalBuyQuantity"])+"\n")
  data_file.write("Closing Price : "+str(data["closePrice"])+"\n")
  data_file.write("Day Low : "+str(data["dayLow"])+"\n")
  data_file.write("Day High : "+str(data["dayHigh"])+"\n")
  data_file.write("\n")
  data_file.write("\n")

data_file.write("************************************************************************")
#os.system("cat data.txt")
data_file.close()
