import os
import re
from PyPDF2 import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    try:
        reader = PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    except Exception as e:
        print(f"Error reading {pdf_path}: {e}")
        return ""


def find_pdfs_recursively(root_directory):
    """Find all PDF files in a directory and its subdirectories."""
    pdf_files = []
    for dirpath, _, filenames in os.walk(root_directory):
        for file in filenames:
            if file.endswith(".pdf"):
                pdf_files.append(os.path.join(dirpath, file))
    return pdf_files


def find_similar_pdfs(directory, similarity_threshold=0.9):
    """Find and list similar PDFs in the given directory and subdirectories."""
    pdf_files = find_pdfs_recursively(directory)
    texts = []
    file_names = []

    # Extract text from each PDF
    for pdf_file in pdf_files:
        print(f"Extracting text from {pdf_file}...")
        text = extract_text_from_pdf(pdf_file)
        if text.strip():
            texts.append(text)
            file_names.append(pdf_file)

    # Use TF-IDF Vectorizer to compare text
    if len(texts) < 2:
        print("Not enough PDF files with extractable text.")
        return []

    vectorizer = TfidfVectorizer().fit_transform(texts)
    cosine_matrix = cosine_similarity(vectorizer)

    # Find pairs with high similarity
    similar_pairs = []
    for i in range(len(file_names)):
        for j in range(i + 1, len(file_names)):
            if cosine_matrix[i, j] >= similarity_threshold:
                similar_pairs.append((file_names[i], file_names[j], cosine_matrix[i, j]))

    return similar_pairs


def filter_paths(input_lines, target_folder):
    """
    Filters the paths to keep only the first path starting with the target folder.
    """
    filtered_paths = []
    for line in input_lines:
        match = re.match(rf"({re.escape(target_folder)}.*?\.pdf) and .*", line.strip())
        if match:
            filtered_paths.append(match.group(1))
    return filtered_paths


def delete_files(file_paths):
    """Deletes all files in the provided list of file paths."""
    for file_path in file_paths:
        if os.path.exists(file_path):
            try:
                os.remove(file_path)
                print(f"Deleted: {file_path}")
            except Exception as e:
                print(f"Error deleting {file_path}: {e}")
        else:
            print(f"File not found: {file_path}")


if __name__ == "__main__":
    # Input parameters
    parent_folder = input("Enter the parent folder path containing PDFs: ").strip()
    target_folder = input("Enter the target folder path where duplicates will be deleted: ").strip()
    similarity_threshold = float(input("Enter the similarity threshold (e.g., 0.9 for 90%): ").strip())

    # Step 1: Find similar PDFs
    print("Finding similar PDFs across all subfolders...")
    similar_pdfs = find_similar_pdfs(parent_folder, similarity_threshold=similarity_threshold)

    if not similar_pdfs:
        print("No similar PDFs found.")
        exit()

    # Step 2: Filter paths for the target folder
    similar_lines = [
        f"{pdf1} and {pdf2} are {score * 100:.2f}% similar."
        for pdf1, pdf2, score in similar_pdfs
    ]
    filtered_paths = filter_paths(similar_lines, target_folder)

    if not filtered_paths:
        print(f"No duplicate PDFs found in the target folder: {target_folder}")
        exit()

    # Step 3: Delete filtered paths
    print("Deleting duplicate PDFs in the target folder...")
    delete_files(filtered_paths)

    print("Process completed.")
