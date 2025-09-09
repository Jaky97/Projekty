def factorial(n):  #vložení n do funkce
    if n == 0:  #pokud je n 0 vrátí 1
        return 1  
    return n * factorial(n - 1)  #hodnota (n - 1)  * hodnota n}





int factorial(int n) {                #vložení n do funkce
    if (n == 0) return 1; // základní případ #pokud je n 0 vrátí 1
    return n * factorial(n - 1); // rekurzivní krok #hodnota (n - 1)  * hodnota n
}