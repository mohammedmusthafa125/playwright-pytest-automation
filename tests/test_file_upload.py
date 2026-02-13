import os
from pages.FileUploadPage import FileUploadPage

def test_file_upload(page):
    upload = FileUploadPage(page)
    upload.open()

    file_path = os.path.abspath("testdata/sample.txt")
    upload.upload_file(file_path)

    assert upload.get_uploaded_filename() == "sample.txt"
