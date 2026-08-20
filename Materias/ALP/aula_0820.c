#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <stdbool.h>

/*int main()
{
    int inicio = 100;

    while(inicio <= 500){
        if(inicio % 11 == 5){
            printf("%d\n", inicio);
            inicio++;
        }else inicio++;
    }
    return 0;
}
*/


/*
int main()
{
    int a = 80000, b=200000;
    int cont =0;
    while(a <= b){
        cont++;
        a = a +  (a * 0.03);
        b = b+(b * 0.015);
    }
    printf("precisou de %d anos para o pais a chegar ou ultrapassar o pais b",cont);
}*/

/*int main()
{
    int n = 0;
    int aux;
    printf("quantos numeros vc irá digitar: ")
    while(n<=0){
        scanf("%d", &n)
        if(n<=o){
            printf("Digite um numero maior que 0: ");
        }
    }

    while()
}*/

int main(){
    int  n, aux,atual, anterior;
    bool crescente = true;

    printf("entre com um numero:  ");
    scanf("%d", &n);
    while(n<=0){
        printf("Valor invalido. Entre com outro valor: ");
        scanf("%d",&n);
    }
    int cont =1;
    while(cont<=n){
        printf("Entre com um numero da sequencia: ");
        scanf("%d", &atual);
        cont++;
        if(atual<anterior){
            crescente = false;
        }
        anterior = atual;

    }
}
