function Fibonacci(nbrMax, actuel = 0, suivant=1, compteur=0){
    if (compteur > nbrMax){
        return;
    }
    console.log(actuel);
    fibonnacci(nbrMax, suivant,actuel+suivant, compteur+1);
}
fibonnacci(10, 3, 5, 3);