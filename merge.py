from PyPDF2 import PdfMerger

# Cria o objeto para fazer a junção
merger = PdfMerger()

# Loop de 1 até 80, adicionando os PDFs na ordem correta
for i in range(1, 81):
    merger.append(f"pdfs/{i}.pdf")

# Escreve o arquivo final unificado
merger.write("resultado.pdf")
merger.close()

print("Todos os PDFs foram unidos com sucesso em 'resultado.pdf'.")
