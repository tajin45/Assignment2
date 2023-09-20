sec= int(input("Enter seconds: "))
hour = sec// 3600
minute = (sec % 3600)//60
second = sec%60
print (sec,"is equal", hour, "hours", minute,"minutes", second,"seconds")