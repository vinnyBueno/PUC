#include <stdio.h>

#define MAX_LIVROS 3
#define MAX_USUARIOS 3
#define TAM_TEXTO 121


typedef struct {
    int codigo;
    char descricao[TAM_TEXTO];
    int estoque;
} Livro;

typedef struct {
    int codigo;
    char dados[TAM_TEXTO];
    int codigoLivroEmprestado;
} Usuario;


void limparTeclado(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF) {
    }
}


void lerTexto(char texto[], char mensagem[]) {
    int valido;
    int tam;
    int c;

    do {
        valido = 1;
        printf("%s", mensagem);

        if (fgets(texto, TAM_TEXTO, stdin) == NULL) {
            texto[0] = '\0';
        }


        tam = 0;
        while (texto[tam] != '\0') {
            tam++;
        }

        if (tam > 0 && texto[tam - 1] == '\n') {

            texto[tam - 1] = '\0';
        } else if (tam == TAM_TEXTO - 1) {

            c = getchar();
            if (c != '\n' && c != EOF) {
                valido = 0;
                printf("Texto muito longo (maximo %d caracteres).\n", TAM_TEXTO - 1);
                limparTeclado();
            }
        }

        if (valido && texto[0] == '\0') {
            valido = 0;
            printf("O texto nao pode ficar vazio.\n");
        }
    } while (!valido);
}


int buscarLivro(Livro livros[], int qtdLivros, int codigoBuscado) {
    int posBusca = -1;

    for (int i = 0; i < qtdLivros; i++) {
        if (livros[i].codigo == codigoBuscado) {
            posBusca = i;
        }
    }

    return posBusca;
}


int cadastrarLivro(Livro livros[], int qtdLivros) {
    int novoCodigo;
    int repetido;
    int estoque;

    printf("\nCadastro do livro %d de %d\n", qtdLivros + 1, MAX_LIVROS);


    do {
        printf("Codigo do livro: ");
        scanf("%d", &novoCodigo);

        repetido = 0;
        if (buscarLivro(livros, qtdLivros, novoCodigo) != -1) {
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

    limparTeclado();


    livros[qtdLivros].codigo = novoCodigo;
    livros[qtdLivros].estoque = estoque;
    lerTexto(livros[qtdLivros].descricao,
             "Descricao (Titulo; Autor; Ano; Categoria): ");

    return qtdLivros + 1;
}


void listarLivros(Livro livros[], int qtdLivros) {
    printf("\n=== Acervo ===\n");
    for (int i = 0; i < qtdLivros; i++) {
        printf("Codigo: %d | Estoque: %d | %s\n",
               livros[i].codigo, livros[i].estoque, livros[i].descricao);
    }
}


int calcularQtdExemplares(Livro livros[], int qtdLivros) {
    int qtdExemplares = 0;

    for (int i = 0; i < qtdLivros; i++) {
        qtdExemplares += livros[i].estoque;
    }

    return qtdExemplares;
}


int disponibilidadeLivro(int qtdEstoque) {
    if (qtdEstoque > 0) {
        return 1;
    }
    return 0;
}


int buscarUsuario(Usuario usuarios[], int qtdUsuarios, int codigoBuscado) {
    int posBusca = -1;

    for (int i = 0; i < qtdUsuarios; i++) {
        if (usuarios[i].codigo == codigoBuscado) {
            posBusca = i;
        }
    }

    return posBusca;
}


int cadastrarUsuario(Usuario usuarios[], int qtdUsuarios) {
    int novoCodigo;
    int repetido;

    printf("\nCadastro do usuario %d de %d\n", qtdUsuarios + 1, MAX_USUARIOS);


    do {
        printf("Codigo do usuario: ");
        scanf("%d", &novoCodigo);

        repetido = 0;
        if (buscarUsuario(usuarios, qtdUsuarios, novoCodigo) != -1) {
            repetido = 1;
        }

        if (novoCodigo < 0) {
            printf("Codigo invalido: nao pode ser negativo.\n");
        } else if (repetido) {
            printf("Codigo invalido: ja cadastrado.\n");
        }
    } while (novoCodigo < 0 || repetido);

    limparTeclado();

    usuarios[qtdUsuarios].codigo = novoCodigo;
    lerTexto(usuarios[qtdUsuarios].dados, "Dados do usuario (Nome; Curso): ");
    usuarios[qtdUsuarios].codigoLivroEmprestado = -1;

    return qtdUsuarios + 1;
}


void listarUsuarios(Usuario usuarios[], int qtdUsuarios) {
    printf("\n=== Usuarios ===\n");
    for (int i = 0; i < qtdUsuarios; i++) {
        printf("Codigo: %d | %s | Livro emprestado: ",
               usuarios[i].codigo, usuarios[i].dados);

        if (usuarios[i].codigoLivroEmprestado == -1) {
            printf("nenhum (-1)\n");
        } else {
            printf("%d\n", usuarios[i].codigoLivroEmprestado);
        }
    }
}

int main() {
    Livro livros[MAX_LIVROS];
    Usuario usuarios[MAX_USUARIOS];
    int qtdLivros = 0;
    int qtdUsuarios = 0;


    while (qtdLivros < MAX_LIVROS) {
        qtdLivros = cadastrarLivro(livros, qtdLivros);
    }


    listarLivros(livros, qtdLivros);


    int codigoBuscado;
    printf("\nDigite o codigo do livro que deseja buscar: ");
    scanf("%d", &codigoBuscado);

    int posBusca;
    posBusca = buscarLivro(livros, qtdLivros, codigoBuscado);

    if (posBusca == -1) {
        printf("O livro %d nao existe no acervo.\n", codigoBuscado);
    } else {
        printf("Livro encontrado:\n");
        printf("Codigo: %d\n", livros[posBusca].codigo);
        printf("Descricao: %s\n", livros[posBusca].descricao);
        printf("Estoque: %d\n", livros[posBusca].estoque);


        if (disponibilidadeLivro(livros[posBusca].estoque) == 1) {
            printf("Situacao: disponivel.\n");
        } else {
            printf("Situacao: temporariamente indisponivel.\n");
        }
    }


    int qtdExemplares;
    qtdExemplares = calcularQtdExemplares(livros, qtdLivros);
    printf("\nTotal de livros: %d\n", qtdLivros);
    printf("Total de exemplares: %d\n", qtdExemplares);


    while (qtdUsuarios < MAX_USUARIOS) {
        qtdUsuarios = cadastrarUsuario(usuarios, qtdUsuarios);
    }


    listarUsuarios(usuarios, qtdUsuarios);

    return 0;
}
