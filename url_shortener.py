#importing the librabry
import pyshorteners

#creating a class
us = pyshorteners.Shortener()

url = input("enter the url:")

#using tinyurl
print(us.tinyurl.short(url))