# 📄 PDF Merger

> Uma aplicação Python simples e eficiente para juntar múltiplos documentos PDF em um único arquivo

![Python](https://img.shields.io/badge/python-v3.6+-blue.svg)
![PyPDF2](https://img.shields.io/badge/PyPDF2-3.0.1-green.svg)
![License](https://img.shields.io/badge/license-MIT-blue.svg)

## 🎯 Propósito

O **PDF Merger** é uma ferramenta desenvolvida para resolver o problema comum de ter múltiplos documentos PDF que precisam ser combinados em um único arquivo. Ideal para:

- Unir capítulos de livros ou documentos
- Combinar faturas e comprovantes
- Consolidar relatórios e apresentações
- Organizar documentos acadêmicos ou profissionais

## ✨ Funcionalidades

- ✅ Junta até 80 arquivos PDF automaticamente
- ✅ Ordem sequencial garantida (1.pdf, 2.pdf, ..., 80.pdf)
- ✅ Interface simples via linha de comando
- ✅ Arquivo de saída otimizado
- ✅ Tratamento automático de arquivos

## 🚀 Pré-requisitos

- Python 3.6 ou superior
- PyPDF2 library

## 📦 Instalação

1. Clone o repositório ou faça o download dos arquivos
2. Instale a dependência necessária:

```bash
pip install PyPDF2
```

## 🔧 Como Usar

### 1. Preparar os Arquivos

Coloque todos os arquivos PDF que deseja juntar na pasta `pdfs/` com nomes sequenciais:

```
pdfs/
├── 1.pdf
├── 2.pdf
├── 3.pdf
├── ...
└── 80.pdf
```

### 2. Executar o Script

```bash
python merge.py
```

### 3. Resultado

O arquivo unificado será gerado como `resultado.pdf` na pasta raiz do projeto.

## 📁 Estrutura do Projeto

```
pdf-merger/
├── merge.py              # Script principal
├── pdfs/                 # Pasta com os PDFs a serem unidos
│   ├── 1.pdf
│   ├── 2.pdf
│   └── ...
├── resultado.pdf         # Arquivo final gerado
└── README.md            # Este arquivo
```

## 💡 Exemplo de Uso

```python
# O script automaticamente:
# 1. Localiza todos os PDFs numerados de 1 a 80
# 2. Junta-os em ordem sequencial
# 3. Salva o resultado em 'resultado.pdf'
# 4. Exibe mensagem de confirmação
```

**Saída esperada:**
```
Todos os PDFs foram unidos com sucesso em 'resultado.pdf'.
```

## ⚙️ Personalização

Para modificar o comportamento do script:

- **Alterar quantidade de arquivos**: Modifique o `range(1, 81)` na linha 7
- **Mudar pasta de origem**: Altere `pdfs/` na linha 8
- **Personalizar nome do arquivo final**: Modifique `resultado.pdf` na linha 11

## 🐛 Solução de Problemas

### Erro "FileNotFoundError"
- Verifique se a pasta `pdfs/` existe
- Certifique-se de que os arquivos estão nomeados corretamente (1.pdf, 2.pdf, etc.)

### Erro "ModuleNotFoundError: No module named 'PyPDF2'"
- Execute: `pip install PyPDF2`

### PDFs não são unidos na ordem correta
- Verifique se os nomes dos arquivos seguem a sequência numérica (1.pdf, 2.pdf, ...)

## 🤝 Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para:

- Reportar bugs
- Sugerir melhorias
- Enviar pull requests

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 👨‍💻 Autor

Desenvolvido com ❤️ para facilitar o gerenciamento de documentos PDF.

---

⭐ Se este projeto foi útil para você, considere dar uma estrela no repositório! 