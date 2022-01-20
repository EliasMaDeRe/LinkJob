#include <bits/stdc++.h>
using namespace std;
void Espejo(int numero){
int t = 0;

    while (numero > 0){
        cout << numero % 10;
        numero /= 10;
        
    }

}

int main(){

int numero;

cin >> numero;

Espejo(numero);

        
 return 0;}
