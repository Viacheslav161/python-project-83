from bs4 import BeautifulSoup


def get_data(response):
    parsed_content = BeautifulSoup(response.text, "lxml")
    result = {}

    result['h1'] = parsed_content.h1.string if parsed_content.h1 else ""
    result['title'] = parsed_content.title.string if parsed_content.title else ""
    meta_description = parsed_content.find('meta', {'name': 'description'})
    result['description'] = (
        meta_description.get('content') if meta_description else ""
    )

    return result
