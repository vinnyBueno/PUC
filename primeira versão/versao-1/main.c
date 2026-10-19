#include <stdio.h>

#define MAX_TITULOS 3

int main() {
    int codigos[MAX_TITULOS] = {0};
    int estoques[MAX_TITULOS] = {0};
    int qtdTitulos = 0;


    while (qtdTitulos < MAX_TITULOS) {
        int novoCodigo;
        int repetido;
        int estoque;

        printf("\n Cadastro do titulo %d de %d \n", qtdTitulos + 1, MAX_TITULOS);


        do {
            printf("Codigo do livro: ");
            scanf("%d", &novoCodigo);

            repetido = 0;
            for (int i = 0; i < qtdTitulos; i++) {
                if (codigos[i] == novoCodigo) {
                    repetido = 1;
                }
            }

            if (novoCodigo < 0) {
                printf("Codigo invalido: nao pode ser negativo.\n");
            } else if (repetido) {
                printf("Codigo invalido: ja cadastrado.\n");
            }
        } while (novoCodigo < 0 || repetido);


        do {
            printf("Estoque do livro %d: ", novoCodigo);
            scanf("%d", &estoque);

            if (estoque < 0) {
                printf("Estoque invalido: nao pode ser negativo.\n");
            }
        } while (estoque < 0);


        codigos[qtdTitulos] = novoCodigo;
        estoques[qtdTitulos] = estoque;
        qtdTitulos++;
    }


    int qtdExemplares = 0;

    printf("\n=== Acervo ===\n");
    for (int i = 0; i < qtdTitulos; i++) {
        printf("Codigo: %d | Estoque: %d\n", codigos[i], estoques[i]);
        qtdExemplares += estoques[i];
    }
    printf("Total de titulos: %d\n", qtdTitulos);
    printf("Total de exemplares: %d\n", qtdExemplares);


    int codigoBusca;
    int posBusca = -1;

    printf("\nDigite o codigo do livro que deseja buscar: ");
    scanf("%d", &codigoBusca);

    for (int i = 0; i < qtdTitulos; i++) {
        if (codigos[i] == codigoBusca) {
            posBusca = i;
        }
    }

    if (posBusca == -1) {
        printf("O titulo %d nao existe no acervo.\n", codigoBusca);
    } else {

        printf("Titulo %d encontrado.\n", codigoBusca);
        if (estoques[posBusca] == 0) {
            printf("Situacao: temporariamente indisponivel.\n");
        } else {
            printf("Situacao: disponivel (%d exemplar(es) em estoque).\n",
                   estoques[posBusca]);
        }
    }

    return 0;
}
