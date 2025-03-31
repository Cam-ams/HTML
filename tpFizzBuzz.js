function FizzBuzz(){
    let r = '';
    for(i=1; i<101 ; i++){
        const divisiblePar3 = i%3 ==0;
        const divisiblePar5 = i % 5 ==0;
        if (divisiblePar3 && divisiblePar5) {
            r=console.log('FizzBuzz');

        } else if  (divisiblePar3){
            r= console.log('Fizz');

        } else if (divisiblePar5){
            r=console.log('Buzz');
            }
        if (i %3 !=0 && i%5 != 0 ) {
            r = console.log(i)

        }
    }
    return (r);
} 

console.log(FizzBuzz());
 