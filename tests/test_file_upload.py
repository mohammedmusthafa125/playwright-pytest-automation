import os
from pages.FileUploadPage import FileUploadPage

def test_file_upload(page):
    upload = FileUploadPage(page)
    upload.open()



    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(BASE_DIR, "testdata", "sample.txt")

    upload.upload_file(file_path)

    assert upload.get_uploaded_filename() == "sample.txt"
