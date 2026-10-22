#include <stdio.h>

#define MAX_TITULOS 3
#define TAM_TEXTO 121


int buscarTitulo(
    int codigos[],
    int qtdTitulos,
    int codigoBuscado
) {
    int posBusca = -1;

    for (int i = 0; i < qtdTitulos; i++) {
        if (codigos[i] == codigoBuscado) {
            posBusca = i;
        }
    }

    return posBusca;
}


void mostrarDescricao(
    int posicao,
    char descricao1[],
    char descricao2[],
    char descricao3[]
) {
    if (posicao == 0) {
        printf("%s\n", descricao1);
    } else if (posicao == 1) {
        printf("%s\n", descricao2);
    } else {
        printf("%s\n", descricao3);
    }
}


int cadastrarTitulo(
    int codigos[],
    int estoques[],
    char descricao1[],
    char descricao2[],
    char descricao3[],
    int qtdTitulos
) {
    int novoCodigo;
    int repetido;
    int estoque;
    int c;
    int tam;
    int descricaoValida;
    char descricaoTemp[TAM_TEXTO];

    printf("\nCadastro do titulo %d de %d\n", qtdTitulos + 1, MAX_TITULOS);


    do {
        printf("Codigo do livro: ");
        scanf("%d", &novoCodigo);

        repetido = 0;
        if (buscarTitulo(codigos, qtdTitulos, novoCodigo) != -1) {
            repetido = 1;
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


    while ((c = getchar()) != '\n' && c != EOF) {
    }


    do {
        descricaoValida = 1;
        printf("Descricao (Titulo; Autor; Ano; Categoria): ");

        if (fgets(descricaoTemp, TAM_TEXTO, stdin) == NULL) {
            descricaoTemp[0] = '\0';
        }


        tam = 0;
        while (descricaoTemp[tam] != '\0') {
            tam++;
        }

        if (tam > 0 && descricaoTemp[tam - 1] == '\n') {

            descricaoTemp[tam - 1] = '\0';
        } else if (tam == TAM_TEXTO - 1) {

            c = getchar();
            if (c != '\n' && c != EOF) {
                descricaoValida = 0;
                printf("Descricao muito longa (maximo %d caracteres).\n", TAM_TEXTO - 1);
                while ((c = getchar()) != '\n' && c != EOF) {
                }
            }
        }

        if (descricaoValida && descricaoTemp[0] == '\0') {
            descricaoValida = 0;
            printf("Descricao nao pode ficar vazia.\n");
        }
    } while (!descricaoValida);


    codigos[qtdTitulos] = novoCodigo;
    estoques[qtdTitulos] = estoque;


    for (int j = 0; j <= tam; j++) {
        if (qtdTitulos == 0) {
            descricao1[j] = descricaoTemp[j];
        } else if (qtdTitulos == 1) {
            descricao2[j] = descricaoTemp[j];
        } else {
            descricao3[j] = descricaoTemp[j];
        }
    }

    return qtdTitulos + 1;
}


void listarTitulos(
    int codigos[],
    int estoques[],
    char descricao1[],
    char descricao2[],
    char descricao3[],
    int qtdTitulos
) {
    printf("\n=== Acervo ===\n");
    for (int i = 0; i < qtdTitulos; i++) {
        printf("Codigo: %d | Estoque: %d | ", codigos[i], estoques[i]);
        mostrarDescricao(i, descricao1, descricao2, descricao3);
    }
}


int calcularQtdExemplares(
    int estoques[],
    int qtdTitulos
) {
    int qtdExemplares = 0;

    for (int i = 0; i < qtdTitulos; i++) {
        qtdExemplares += estoques[i];
    }

    return qtdExemplares;
}


int disponibilidadeTitulo(
    int qtdEstoque
) {
    if (qtdEstoque > 0) {
        return 1;
    }
    return 0;
}

int main(void) {
    int codigos[MAX_TITULOS] = {0};
    int estoques[MAX_TITULOS] = {0};
    int qtdTitulos = 0;

    char descricao1[TAM_TEXTO];
    char descricao2[TAM_TEXTO];
    char descricao3[TAM_TEXTO];
    descricao1[0] = '\0';
    descricao2[0] = '\0';
    descricao3[0] = '\0';


    while (qtdTitulos < MAX_TITULOS) {
        qtdTitulos = cadastrarTitulo(
            codigos,
            estoques,
            descricao1,
            descricao2,
            descricao3,
            qtdTitulos
        );
    }


    listarTitulos(
        codigos,
        estoques,
        descricao1,
        descricao2,
        descricao3,
        qtdTitulos
    );


    int codigoBuscado;
    printf("\nDigite o codigo do livro que deseja buscar: ");
    scanf("%d", &codigoBuscado);


    int posBusca;
    posBusca = buscarTitulo(
        codigos,
        qtdTitulos,
        codigoBuscado
    );

    if (posBusca == -1) {
        printf("O titulo %d nao existe no acervo.\n", codigoBuscado);
    } else {
        printf("Titulo %d encontrado.\n", codigoBuscado);
        printf("Descricao: ");
        mostrarDescricao(posBusca, descricao1, descricao2, descricao3);


        int disponivel;
        disponivel = disponibilidadeTitulo(estoques[posBusca]);

        if (disponivel == 1) {
            printf("Situacao: disponivel (%d exemplar(es) em estoque).\n",
                   estoques[posBusca]);
        } else {
            printf("Situacao: temporariamente indisponivel.\n");
        }
    }


    int qtdExemplares;
    qtdExemplares = calcularQtdExemplares(
        estoques,
        qtdTitulos
    );
    printf("\nTotal de titulos: %d\n", qtdTitulos);
    printf("Total de exemplares: %d\n", qtdExemplares);

    return 0;
}
