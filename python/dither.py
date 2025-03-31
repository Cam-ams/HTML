import sys
import matplotlib.pyplot as plt # type: ignore

# On charge l'image à réduire et on la convertit en liste de pixels²
img = plt.imread(r"C:\Users\Cam\Desktop\SDV\Dev\python\test.jpg").tolist() ##ERREUR A REFAIRE

# Couleurs que l'algorithme pourra utiliser pour "approximer" la valeur d'un pixel
COLORS = [
    [0, 0, 0],            # Noir
    [255, 255, 255],      # Blanc
    [255, 0, 0],          # Rouge
    [0, 255, 0],          # Vert
    [0, 0, 255],          # Bleu
]

# Convertit une valeur numérique à virgule en un nombre entier compris entre 0 et 255
# Les valeurs RGB que nous utilisons doivent être comprises entre ces deux valeurs
def to_byte(n):
    return max(0, min(255, int(round(n, 0))))

# Fonction calculant la distance entre chaque couleurs d'un pixel A et un pixel B
def pixel_error(pixel_a, pixel_b):
    r_error = pixel_b[0] - pixel_a[0]
    g_error = pixel_b[1] - pixel_a[1]
    b_error = pixel_b[2] - pixel_a[2]
    return [r_error, g_error, b_error]

# Fonction qui choisit dans la liste des couleurs COLORS, la couleur qui est la plus
# proche de celle du pixel passé en paramètre
# Pour cela, on calcule l'erreur totale entre ce pixel et chaque couleur de la palette,
# et on prends la plus petite
def find_closest_color(pixel):
    errors = [(n, pixel_error(pixel, try_pixel)) for (n, try_pixel) in enumerate(COLORS)]
    best = sorted(errors, key=lambda p: sum([err**2 for err in p[1]]))
    return COLORS[best[0][0]]

# Affiche le résultat
def show(grid):
    plt.gca().invert_yaxis()
    plt.imshow(grid)
    plt.show()
    sys.exit(0)


###### Début du TP ######

class Dither():
    def __init__(self,img,a=0,b=0,c=0,d=0,e=0):
        self.a=a
        self.b=b
        self.c=c
        self.d=d
        self.e=e
        self.img=img

        
    def dith(self):
        liste_p=[]
        for i in range(len(img)):
            for j in range(len(img[i])): ## prbl i un nbr n'a pas de longueur
                pixel=find_closest_color(img[i][j])
                error=pixel_error(pixel,img[i][j])

                img[i][j]=pixel
                print(pixel)
    
    def forward_error(self,error, p_x, p_y, k):

##te= Dither(img)
##te.dith()

