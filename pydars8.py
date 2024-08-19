#if else elif
#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
    #print('Sizga kirish bepul.')
#elif yosh<=12:
    #print('Sizga kirish 5000 so\'m')
#else:
    #print('Sizga kirish 10000 so\'m')
#asosan bunday qilish shart emas!



#yosh = int(input('Yoshingiz nechida? '))
#if yosh<=4:
    #narh = 0
#elif yosh<=12:
    #narh = 5000
#else:
    #narh = 10000

#print(f"Sizga kirish {narh} so'm")

#kun = input("Bugun kun nima?>>>")
#if kun.lower() == 'shanba' or kun.lower() == 'yakshanba':
    #print("bugun dam olish kuni!")
#else:
    #print("bugun ish kuni!")  

#kun = input("Bugun nima kun?")
#harorat = float(input("Havo harorati qanday?"))
#if kun.lower()=='yakshanba' and harorat>=30:
    #print("Cho'milgani ketdik!")
#elif kun.lower()=='yakshanba' and harorat<30:
    #print("Uyda dam olamiz!")   

#Boolean(bool)

#narh = 15000
#choy = True
#salat = False

#if choy and salat:
    #narh = narh + 10000
#elif choy or salat:
    #narh = narh + 5000

#print(f"jami {narh} so'm")

#bir nechta qiymatlarni tekshirish
#narh = 15000 # mijoz 15 so'mga ovqat oldi
#choy = True
#salat = False
#non = True
#kompot = True
#assorti = False
#Quyidagi har bir shart alohida tekshiriladi va bir-biriga bog'liq emas
#if choy:   # agar choy olsa
   # print("Mijoz choy oldi.")
   # narh = narh + 3000
#if salat:  # agar salat olsa
 #   print("Mijoz salat oldi.")
  #  narh = narh + 5000
#if non:    # agar non olsa
 #   print("Mijoz non oldi.")
  #  narh = narh + 2000
#if kompot: # agar kompot olsa
 #   print("Mijoz kompot oldi.")
  #  narh = narh + 5000
#if assorti: # agar assorti olsa
 #   print("Mijoz assorti oldi.")
  #  narh = narh + 15000
    
#print(f"Jami {narh} so'm")

#menu = ["osh" , "qozonkabob" ,"shashlik" , "somsa"]
#a = "somsa" in menu
#print(a)

#menu = ['osh','qazonkabob','shashlik','norin','somsa']
#ovqat = input('Nima ovqat yeysiz?>>>')
#if ovqat.lower() in menu:
    #print('Buyurtma qabul qilindi.')
#else:
    #print('Afsuski bizda bunday ovqat yo\'q')

#menu = ["osh" , "qozonkabob" , "somsa" , "shashlik" , "no'xot sho'rva"]
#buyurtmalar = ["osh" , "qozonkabob" , "manti"]
#for taom in buyurtmalar:
    #print(f"Menuda {taom} bor")
   # else:
        #print(f"Kechirasiz , menuda {taom} yo'q")


menu = ['osh','qazonkabob','shashlik','norin','somsa']
buyurtmalar = []

if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else: # agar ro'yxat bo'sh bo'lsa
    print("Savatchangiz bo'sh!")        
        
        
        #agar listda qiymat yo'q bo'lsa
   