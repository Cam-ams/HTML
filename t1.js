
function multiplierParDeux(nombre0) {
    return nombre0 *2 ;
}

function multiplierParTrois(nombre1) {
    return nombre1 *3 ;
}

console.log(multiplierParDeux(6));
console.log(multiplierParTrois(8));

function ajouterExclamation(texte){
   texte = texte  + '!';
    return texte;
}

console.log (ajouterExclamation('b'));

function concatener (texte1,texte2){
    return texte1 +' ' +texte2 ;
}
console.log (concatener('y','o'));

function messageComplet(prenom){
      return ajouterExclamation(concatener('Bonjour',prenom));
}
console.log(messageComplet('Camélia'));

function doubleEtTriple (nombre){
    return multiplierParDeux(multiplierParTrois(nombre));
}

console.log (doubleEtTriple(2));

function phrasePersonalisee(prenom1, nombre3){
    return messageComplet(prenom1) +' Votre nombre multiplé par trois est  '+ multiplierParTrois(nombre3);
}

console.log (phrasePersonalisee('alice',5));

console.log (multiplierParTrois(multiplierParDeux(3)));
console.log (ajouterExclamation(concatener('Hello', 'World')));

//tp assimiler 