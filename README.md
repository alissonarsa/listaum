# listaum
Estrutura de Dados II: Recursividade e Alocação

1:
# Nossa estrutura de arquivos simulada em memória
sistema_de_arquivos = {
    'nome': 'raiz',
    'tipo': 'pasta',
    'conteudo': [
        {
            'nome': 'documentos',
            'tipo': 'pasta',
            'conteudo': [
                {'nome': 'trabalho1.docx', 'tipo': 'arquivo'},
                {'nome': 'relatorio.pdf', 'tipo': 'arquivo'}
            ]
        },
        {
            'nome': 'imagens',
            'tipo': 'pasta',
            'conteudo': [
                {'nome': 'foto1.jpg', 'tipo': 'arquivo'},
                {'nome': 'foto2.png', 'tipo': 'arquivo'}
            ]
        },
        {'nome': 'arquivo_raiz.txt', 'tipo': 'arquivo'}
    ]
}


