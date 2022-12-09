import pandas as pd
from logger import logged_func
from pathlib import Path
import os


class File:
    @logged_func
    def __init__(self, file_path=''):
        if file_path:
            self.file_name = file_path.replace('\\', '/').split('/')[-1]
            self.file_path = Path(file_path.replace('\\', '/').replace(f'/{self.file_name}', ''))
        # self.filepath = file_path if file_path else Path(__file__) / 'input.xlsx'
        else:
            self.file_name = 'input.xls'
            self.file_path = Path(os.getcwd()).parent
        self.full_path = self.file_path / self.file_name

    @logged_func
    def read(self):
        df = pd.read_excel(self.full_path).T
        # df_c = df.applymap(lambda x: )
        nums = df[
            df.isin(
                [
                    'Регистрационный номер \nдекларации на товары \nили регистрационный номер '
                    '\nпартии товара, подлежащего \nпрослеживаемости',
                    'Количество \nтовара, \nподлежащего \nпрослеживаемости, \nв количественной \nединице \nизмерения '
                    '\nтовара, \nиспользуемой \nв целях \nосуществления \nпрослеживаемости'
                ]
                # [
                #     'Регистрационный номер',
                #     'Количество \nтовара, \nподлежащего \nпрослеживаемости'
                # ]
            ).any(axis=1)].dropna(how='any', axis=1).iloc[0]
        return nums.str.extract(r'(\d{8}.\d{6}.[0-9a-zA-Zа-яА-Я]\d{6,7}.{0,})', expand=False).dropna().to_list()
        # return nums.str.extract(r'(\d{8}.\d{6}.[0-9a-zA-Zа-яА-Я]\d{6,7}.\d{1,})', expand=False).dropna().to_list()

    @logged_func
    def save(self, data):
        pd.DataFrame(data).T.to_excel(self.file_path / 'output.xlsx')
        print(str(self.file_path / 'output.xlsx'))
        return True

