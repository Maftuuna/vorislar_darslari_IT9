"""
 for loop sikl yaratishda ishlatiladi
"""

oquvchilar =[ "maftuna", "matluba","mashxura", "sharofat","mohinur","dilnura"]

# print(f" Assalomu alaykum hurmatli{ oquvchilar[0]},Ishlar qanday")
# print(f" Assalomu alaykum hurmatli{ oquvchilar[1]},Ishlar qanday")
# print(f" Assalomu alaykum hurmatli{ oquvchilar[2]},Ishlar qanday")
# print(f" Assalomu alaykum hurmatli{ oquvchilar[3]},Ishlar qanday")
# print(f" Assalomu alaykum hurmatli{ oquvchilar[4]},Ishlar qanday")
# print(f" Assalomu alaykum hurmatli{ oquvchilar[5]},Ishlar qanday")


# for ism in oquvchilar :
#   print(f"Assalomu alaykum{ism.title()}")
#   print(f"Xayr hurmatli{ism.upper()}")
  
# raqamlar = list ((1,2,-8, 56))
# for son in raqamlar :
#    print(f"{son} ning kvadrati : {son**2} ga teng")
   
# sonlar =list(range(30,91))
# for son in sonlar:
# print(f"{son}/9 ning qiymati : {son/9} ga teng")

sonlar2 = []

sonlar = list (range(27,54,7))
for son in sonlar:
  sonlar2.append(son**4) 
print(f"4-darajaga oshan royhat{sonlar2}")