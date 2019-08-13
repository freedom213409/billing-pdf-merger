from PyPDF2 import PdfFileReader, PdfFileWriter
from os import listdir
from os.path import isfile, isdir, join


# 指定要列出所有檔案的目錄
mypath = "G:/我的雲端硬碟/03 Nextlink Product Team/04 Routine/02 AWS Billing/AWS Invoices (Molly)/EDP+SPP Invoices_201906"

# 取得所有檔案與子目錄名稱
files = listdir(mypath)

# 以迴圈處理
inFileList = []

for f in files:
    # 產生檔案的絕對路徑
    fullpath = join(mypath, f)
    # 判斷 fullpath 是檔案還是目錄
    if isfile(fullpath):
      if f != "PDFMerger.py":
          inFileList.append(mypath +"/"+ f)

print(inFileList)

def mergePdf(inFileList, outFile):
    '''
    合并文档
    :param inFileList: 要合併文黨的 list
    :param outFile:    合併後的输出文件
    :return:
    '''
    pdfFileWriter = PdfFileWriter()
    for inFile in inFileList:
        # 依照順序循環打開inFileList中的所有文件
        pdfReader = PdfFileReader(open(inFile, 'rb'))
        pageObj = pdfReader.getPage(0)
        pdfFileWriter.addPage(pageObj)
        """
        # 獲取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        print(page_count)
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))
        """
        # 最後，統一寫到outFile的文件中
        pdfFileWriter.write(open(outFile, 'wb'))


mergePdf(inFileList, 'merged.pdf')
