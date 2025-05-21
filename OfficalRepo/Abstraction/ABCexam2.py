# ✅ 2. Document Reader – Abstracting File Opening

from abc import ABC, abstractmethod


class DocumentReader(ABC):
    @abstractmethod
    def open_document(self):
        pass

class PDFReader(DocumentReader):
    def open_document(self):
        print("Opening PDF Document")

class WordReader(DocumentReader):
    def open_document(self):
        print("Opening Word Document")

#usage
pdf = PDFReader()
pdf.open_document()
# output: Opening PDF Document

word = WordReader()
word.open_document()
# output: Opening Word Document

# 🧠 What it teaches:
# Different file types have different logic.

# User doesn’t worry about the internal logic.