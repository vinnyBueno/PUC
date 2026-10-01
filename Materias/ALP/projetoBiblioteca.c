#include <stdio.h>
#include <stdlib.h>
#include <string.h>

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
    int codigoLivroEmprestado;   /* -1 = nenhum livro emprestado */
} Usuario;

/* ---------- Prototipos ---------- */
int cadastrarLivro(Livro livros[], int qtdLivros);
void listarLivros(Livro livros[], int qtdLivros);
int buscarLivro(Livro livros[], int qtdLivros, int codigoBuscado);
int calcularQtdExemplares(Livro livros[], int qtdLivros);
int disponibilidadeLivro(int qtdEstoque);

int cadastrarUsuario(Usuario usuarios[], int qtdUsuarios);
void listarUsuarios(Usuario usuarios[], int qtdUsuarios);
int buscarUsuario(Usuario usuarios[], int qtdUsuarios, int codigoBuscado);

static void limparBuffer(void);
static int lerInteiro(const char *msg);
static void lerTexto(const char *msg, char destino[]);

/* ---------- main ---------- */
int main(void) {
    Livro livros[MAX_LIVROS];
    Usuario usuarios[MAX_USUARIOS];
    int qtdLivros = 0;
    int qtdUsuarios = 0;
    int codigoBuscado, posBusca;

    printf("=== Cadastro de livros ===\n");
    while (qtdLivros < MAX_LIVROS) {
        qtdLivros = cadastrarLivro(livros, qtdLivros);
    }

    printf("\n=== Acervo ===\n");
    listarLivros(livros, qtdLivros);

    codigoBuscado = lerInteiro("\nCodigo do livro a buscar: ");
    posBusca = buscarLivro(livros, qtdLivros, codigoBuscado);
    if (posBusca == -1) {
        printf("Livro nao encontrado.\n");
    } else {
        printf("Codigo: %d\n", livros[posBusca].codigo);
        printf("Descricao: %s\n", livros[posBusca].descricao);
        printf("Estoque: %d\n", livros[posBusca].estoque);
        if (disponibilidadeLivro(livros[posBusca].estoque) == 1) {
            printf("Livro disponivel.\n");
        } else {
            printf("Livro temporariamente indisponivel.\n");
        }
    }

    printf("\nTotal de exemplares: %d\n", calcularQtdExemplares(livros, qtdLivros));

    printf("\n=== Cadastro de usuarios ===\n");
    while (qtdUsuarios < MAX_USUARIOS) {
        qtdUsuarios = cadastrarUsuario(usuarios, qtdUsuarios);
    }

    printf("\n=== Usuarios ===\n");
    listarUsuarios(usuarios, qtdUsuarios);

    return 0;
}

/* ---------- Livros ---------- */
int cadastrarLivro(Livro livros[], int qtdLivros) {
    int codigo, estoque;

    if (qtdLivros >= MAX_LIVROS) {
        printf("Limite de livros atingido.\n");
        return qtdLivros;
    }

    for (;;) {
        codigo = lerInteiro("Codigo do livro: ");
        if (codigo < 0) {
            printf("Codigo nao pode ser negativo.\n");
            continue;
        }
        if (buscarLivro(livros, qtdLivros, codigo) != -1) {
            printf("Codigo ja cadastrado.\n");
            continue;
        }
        break;
    }

    estoque = lerInteiro("Estoque: ");
    while (estoque < 0) {
        printf("Estoque nao pode ser negativo.\n");
        estoque = lerInteiro("Estoque: ");
    }

    livros[qtdLivros].codigo = codigo;
    livros[qtdLivros].estoque = estoque;
    lerTexto("Descricao (Titulo; Autor; Ano; Categoria): ", livros[qtdLivros].descricao);

    return qtdLivros + 1;
}

void listarLivros(Livro livros[], int qtdLivros) {
    int i;
    for (i = 0; i < qtdLivros; i++) {
        printf("Codigo: %d | Estoque: %d | %s\n",
               livros[i].codigo, livros[i].estoque, livros[i].descricao);
    }
}

int buscarLivro(Livro livros[], int qtdLivros, int codigoBuscado) {
    int i;
    for (i = 0; i < qtdLivros; i++) {
        if (livros[i].codigo == codigoBuscado) {
            return i;
        }
    }
    return -1;
}

int calcularQtdExemplares(Livro livros[], int qtdLivros) {
    int qtdExemplares = 0;
    int i;
    for (i = 0; i < qtdLivros; i++) {
        qtdExemplares += livros[i].estoque;
    }
    return qtdExemplares;
}

int disponibilidadeLivro(int qtdEstoque) {
    return qtdEstoque > 0 ? 1 : 0;
}

/* ---------- Usuarios ---------- */
int cadastrarUsuario(Usuario usuarios[], int qtdUsuarios) {
    int codigo;

    if (qtdUsuarios >= MAX_USUARIOS) {
        printf("Limite de usuarios atingido.\n");
        return qtdUsuarios;
    }

    for (;;) {
        codigo = lerInteiro("Codigo do usuario: ");
        if (codigo < 0) {
            printf("Codigo nao pode ser negativo.\n");
            continue;
        }
        if (buscarUsuario(usuarios, qtdUsuarios, codigo) != -1) {
            printf("Codigo ja cadastrado.\n");
            continue;
        }
        break;
    }

    usuarios[qtdUsuarios].codigo = codigo;
    lerTexto("Dados do usuario (nome; contato): ", usuarios[qtdUsuarios].dados);
    usuarios[qtdUsuarios].codigoLivroEmprestado = -1;

    return qtdUsuarios + 1;
}

void listarUsuarios(Usuario usuarios[], int qtdUsuarios) {
    int i;
    for (i = 0; i < qtdUsuarios; i++) {
        printf("Codigo: %d | %s | Livro emprestado: %d\n",
               usuarios[i].codigo,
               usuarios[i].dados,
               usuarios[i].codigoLivroEmprestado);
    }
}

int buscarUsuario(Usuario usuarios[], int qtdUsuarios, int codigoBuscado) {
    int i;
    for (i = 0; i < qtdUsuarios; i++) {
        if (usuarios[i].codigo == codigoBuscado) {
            return i;
        }
    }
    return -1;
}

/* ---------- Auxiliares ---------- */
static void limparBuffer(void) {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

static int lerInteiro(const char *msg) {
    int valor;
    for (;;) {
        printf("%s", msg);
        if (scanf("%d", &valor) == 1) {
            limparBuffer();
            return valor;
        }
        if (feof(stdin)) exit(1);
        limparBuffer();
        printf("Entrada invalida. Digite um numero.\n");
    }
}

/* Le uma linha (com espacos) de ate TAM_TEXTO-1 caracteres, sem aceitar vazia. */
static void lerTexto(const char *msg, char destino[]) {
    size_t len;
    do {
        printf("%s", msg);
        if (fgets(destino, TAM_TEXTO, stdin) == NULL) exit(1);
        len = strlen(destino);
        if (len > 0 && destino[len - 1] == '\n') {
            destino[len - 1] = '\0';
        } else {
            limparBuffer();
        }
        if (destino[0] == '\0') {
            printf("O texto nao pode ficar vazio.\n");
        }
    } while (destino[0] == '\0');
}
