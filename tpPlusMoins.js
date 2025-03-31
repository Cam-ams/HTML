function nombreplusMoins(){
    const nombreAleatoire = (math.floor()*100);
    while (true) {
        const nombreUtilisateurSTR = prompt("Rentrez votre nbr");
        const nombreUtilisateur = Number(nombreUtilisateurSTR);
        alert ('nombre invalide !');
        continue;
        if (nombreUtilisateur > nombreAleatoire){
            alert("moins");
            continue;
        } else if (nombreUtilisateur < nombreAleatoire){
            alert('plus');
            continue;
        }
        else {
            alert("Gagné")
            break;
        }
    }
}
nombreplusMoins;