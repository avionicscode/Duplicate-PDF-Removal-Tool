# Project Name: Duplicate PDF Removal Tool

## Description
The **Duplicate PDF Removal Tool** is a comprehensive Python-based project designed to efficiently identify and remove duplicate PDF files within a folder and its subfolders. It leverages text extraction, TF-IDF vectorization, and cosine similarity to compare PDF content, enabling users to delete duplicates within a specified target folder while retaining the original files elsewhere.

## Key Features
1. **Recursive PDF Search**: Scans the parent directory and its subfolders to locate all PDF files.
2. **Duplicate Detection**: Uses advanced text comparison (TF-IDF and cosine similarity) to find similar PDFs.
3. **Targeted Deletion**: Filters duplicates to retain only those in the specified folder for deletion.
4. **All-in-One Workflow**: Combines duplicate detection, filtering, and deletion into a single script.

## How It Works
1. **Input Parameters**:
   - **Parent Folder**: The root directory containing all PDFs to scan.
   - **Target Folder**: The directory where duplicate PDFs will be deleted.
   - **Similarity Threshold**: A value (e.g., 0.9 for 90%) to determine how similar two PDFs need to be to be considered duplicates.

2. **Duplicate Detection**:
   - Extracts text from all PDFs in the parent folder.
   - Compares the content using TF-IDF and cosine similarity.
   - Logs all duplicate pairs with similarity scores.

3. **Filtering**:
   - Filters duplicates to include only those located in the target folder.

4. **Deletion**:
   - Deletes the duplicate PDFs in the target folder while leaving the originals untouched.

## Requirements
- Python 3.x
- Required Libraries:
  - `PyPDF2`
  - `scikit-learn`

Install the libraries using pip:
```bash
pip install PyPDF2 scikit-learn
```

## Usage Instructions
1. **Clone or Download the Project**:
   - Save the script as `delete_duplicates.py`.

2. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory containing the script.
   - Execute the script:
     ```bash
     python delete_duplicates.py
     ```

3. **Provide Input Parameters**:
   - Enter the parent folder path (e.g., `D:\LabDuplicatesPDFs`).
   - Enter the target folder path (e.g., `D:\LabDuplicatesPDFs\folder1`).
   - Enter the similarity threshold (e.g., `0.9` for 90%).

4. **Observe Output**:
   - The script will print the duplicate detection progress.
   - Deleted files will be logged in the terminal.

## Example Workflow
### Input:
- **Parent Folder**: `D:\LabDuplicatesPDFs`
- **Target Folder**: `D:\LabDuplicatesPDFs\folder1`
- **Threshold**: `0.9`

### Output:
1. Logs of duplicate PDFs detected:
   ```
   Similar PDFs found:
   D:\LabDuplicatesPDFs\folder1\file1.pdf and D:\LabDuplicatesPDFs\folder2\file2.pdf are 95.00% similar.
   ```
2. Deleted files:
   ```
   Deleted: D:\LabDuplicatesPDFs\folder1\file1.pdf
   ```

## Project Structure
```
project_folder/
    delete_duplicates.py  # Main script combining all functionalities
```

## Limitations
- Relies on text extraction; may not work for PDFs with non-text content (e.g., scanned images).
- Computationally intensive for large datasets.

## Future Improvements
- Add support for image-based text extraction using OCR.
- Implement a GUI for ease of use.
- Include detailed logging to a file for audit purposes.

