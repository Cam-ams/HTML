import time
import msvcrt

class Cookie :
    
    def __init__(self): 
        # nombre de cookies
        self.nbrCookies = 0
        
        # nombres de pouvoirs
        self.nbrGrandMere = 0
        self.nbrMine=0
        self.nbrFerme = 0
        self.nbrUsine =0
        self.nbrBanque=0
        self.nbrTemple =0
        self.nbrTourDeMage =0




    def hausseCookie (self):  ## la fonction cookies permet d'augmenter le nbr de cookie de 1
        self.nbrCookies += 1


    def temps (self):   #permet d'augmenter le nbr de cookie par sec 
        while True:
            time.sleep(1)   # chaque seconde on appel la methode hausseCookie
            self.hausseCookie()
            print(self.nbrCookies)


    def clickCookie (self):   #  chaque touche entrée il y a un +1 sur nbr cookies
        self.nbrCookies +=1
        print("Plus un cookie")
    
    def achatGrandMere(self):  # g pour ajouter une grand mere
            if self.nbrCookies >= 21:
                self.nbrCookies = self.nbrCookies-21
                print("grand mere manon")

    
    def achatFerme(self): # f pour ajouter une ferme
        if self.nbrCookies >= 31:
            self.nbrCookies = self.nbrCookies - 31
            print("j'ai une ferme ")
    

    def achatMine(self): # M pour ajouter une mine
        if self.nbrCookies >= 41:
            self.nbrCookies = self.nbrCookies - 41
            print("j'ai une mine ")
                 




    def additionCookies (self):
         while True :
              self.hausseCookie()
              c = msvcrt.getch()
              if  msvcrt.kbhit() :
                 if c == b'i':
                    self.clickCookie()

                 if c == b'g':
                    self.achatGrandMere()
                 
                 if c== b'f':
                    self.achatFerme()


                 if c== b'm':
                    self.achatMine()


                 #else : self.hausseCookie()
            
              print(self.nbrCookies) 

               
              time.sleep(0.1)



    
    
    



    ##def grandMere (self):  
    ##    self.nbrCookies 

       

g=Cookie()


print(g.additionCookies()) 



    



    






 



    
    

    