from pages.Dynamicloadingpages import DynamicLoadingPage


def test_dynamic_loading(page):
    dynamic=DynamicLoadingPage(page)
    dynamic.open()
    dynamic.load()
    assert dynamic.get_finish_text() == "Hello World!"

