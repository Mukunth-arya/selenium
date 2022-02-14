datakey = ['kumar,somu', 'divya', 'aryan', 'dhamu', 'somu']
value1  = ["kumar", "somu"]



def keyvalue(data, value):
    for i in datakey:
        print(i)
        for j  in range (len(value)):
              if i == value[j]:
                 print (j)
                 print (len(value1))
keyvalue(datakey, value1)