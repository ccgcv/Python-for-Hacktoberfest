import PyPDF2
import sys

def merge_pdfs(_pdfs, outputFilename):
    mergeFile = PyPDF2.PdfFileMerger()

    for _pdf in _pdfs:
        mergeFile.append(PyPDF2.PdfFileReader(_pdf, 'rb'))

    mergeFile.write(outputFilename)

if __name__ == '__main__':
    _pdfs = sys.argv
    _pdfs.pop(0)
    outputFilename = _pdfs.pop(-1)

    if len(_pdfs) > 1:
        merge_pdfs(_pdfs, outputFilename)