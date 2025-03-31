function factorial (nbr){
    let resultat= 1;
    for (i=1; i<nbr+1; i++ ){
        resultat = resultat *i;
    }
    return resultat;
}
console.log(factorial(62));