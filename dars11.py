#11-uyga vazifa
#1-masala
a = int(input("son kirit "))
sonni_kvadrati = lambda a : a**2
print(sonni_kvadrati(a))

#%% 2-masala

yigindi = lambda a,b: a+b
print(yigindi(3, 6))

#%% 3-masala
a = int(input("son kirit "))
juftmi_toqmi = lambda a: a%2 == 0
print("toq bulsa False, juft bulsa True qiymat qaytaradi",juftmi_toqmi(a))

#%% 4-masala
a = int(input("son kirit "))
b = int(input("son kirit "))
yuza = lambda a,b : a*b
print("tugri turtburchakni yuzi ",yuza(a, b))

#%% 5-masala
r = int(input("son kirit "))
pi = 3.1415
uzunlik = lambda r: 2*pi*r
print(uzunlik(r))

#%% 6-masala
r = int(input("son kirit "))
pi = 3.1415
yuza = lambda r : 2*pi*r**2
print("yuzasi ", yuza(r))

#%% 7-masala
my_list = [1, 5, 4, 6, 8, 11, 3, 12]

new_list = list(map(lambda x: x ** 3 , my_list))

print(new_list)

#%% 8-masala
a=[11,22,-5,-6,4,-3,0]
musbat=filter(lambda x: x>0 ,a)
print(list(musbat))


#%% 9-masala
a=[11,22,-5,-6,4,-3,0]
musbat=filter(lambda x: x<0 ,a)
print(list(musbat))

#%% 10-masala
a=[12,33,44,24,100,14,49,51]
yuza=filter(lambda x: x>30 ,a)
print(list(yuza))























