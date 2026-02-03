from rlm.rlm_repl import RLM_REPL
from pypdf import PdfReader
import os

def load_pdf_text(pdf_path: str) -> str:
    print(f"Loading PDF: {pdf_path}")
    reader = PdfReader(pdf_path)
    text = []
    for i, page in enumerate(reader.pages):
        page_text = page.extract_text()
        if page_text:
            text.append(page_text)
    return "\n".join(text)


def main():
    print("Using RLM (REPL) with a real PDF as context.")

    # === NOME DO SEU PDF NA RAIZ ===
    PDF_FILE = "SEU PDF"  # <-- troque para o nome real

    if not os.path.exists(PDF_FILE):
        raise FileNotFoundError(f"PDF not found: {PDF_FILE}")

    context = load_pdf_text(PDF_FILE)

    print(f"PDF loaded. Total characters: {len(context)}")

    rlm = RLM_REPL(
        model="gpt-5-mini",
        recursive_model="gpt-5-nano",
        enable_logging=True,
        max_iterations=25
    )
    query = """ SEU PROMPT    """
    result = rlm.completion(context=context, query=query)
    print(f"Result: {result}.")
    # Define o nome do arquivo
    file_name = "resultado.txt"

    try:
    
        # Salva o resultado no arquivo txt
        with open(file_name, "w", encoding="utf-8") as file:
            file.write(result)
        
        print(f"Sucesso! O resultado foi salvo em: {file_name}")

    except Exception as e:
        print(f"Erro ao processar ou salvar o arquivo: {e}")

if __name__ == "__main__":
    main()
