from lxml import html
from models.models import RequestModel, CSSSelectorModel, CSSSelectorResultModel


class HTMLParser:
    css_service = None
    xpath_service = None

    def __init__(self, text):
        self.dom = html.fromstring(text)

    def get_css_elements(self, css_model: CSSSelectorModel):
        elements = self.dom.cssselect(css_model.selector)
        if css_model.text:
            results = [el.text_content() for el in elements]
            return CSSSelectorResultModel(**css_model.dict(), results=results)
        if css_model.attr:
            # maybe it's better not silent?
            results = [el.get(css_model.attr) for el in elements if el.get(css_model.attr)]
            return CSSSelectorResultModel(**css_model.dict(), results=results)

    def get_css_results(self, model: RequestModel):
        results = []
        for css_model in model.css_selectors:
            results.append(self.get_css_elements(css_model=css_model))
        return results
