from logger import logger
from file_work import File
from pager import SearchPage
from PySimpleGUI import popup_get_file


def main():
    filepath = popup_get_file('Пожалуйста, укажите расположение книги продаж')
    data = File(filepath).read()
    page = SearchPage()
    res = {}
    for c in set(data):
        try:
            res[c] = page.search(c)
        except Exception as ex:
            page.driver.get('https://www.nalog.gov.ru/rn77/service/traceability/#tab0')
            res[c] = page.search(c)
    # res = {c: page.search(c) for c in set(data)}
    File().save(res)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        main()
    except Exception as ex:
        logger.exception(ex)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
