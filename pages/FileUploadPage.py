class FileUploadPage:
    def __init__(self, page):
        self.page = page
        self.file_input = page.locator("input[type='file']")
        self.upload_button = page.get_by_role("button", name="Upload")

    def open(self):
        self.page.goto("https://the-internet.herokuapp.com/upload")

    def upload_file(self, file_path):
        self.file_input.set_input_files(file_path)
        self.upload_button.click()

    def get_uploaded_filename(self):
        return self.page.locator("#uploaded-files").inner_text()
