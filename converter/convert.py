import os
from pathlib import Path
from typing import Any, List

import pandas as pd

from toh_analyzer import get_exh_dataconverter

HAT_DATA = 'hatData.json'
HAT_TRANS_DATA = 'HatTransData.xlsx'
HAT_FOLDER = 'hat'

WORKING_FOLDER = 'repo'

TRANS_COLUM = (
    'Unnamed: 0',
    'English',
    'Latam',
    'Brazilian',
    'Portuguese',
    'Korean',
    'Russian',
    'Dutch',
    'Filipino',
    'French',
    'German',
    'Italian',
    'Japanese',
    'Spanish',
    'SChinese',
    'TChinese',
    'Irish',
)

def main() -> None:

    cur_folder_path = Path(__file__).resolve().parent

    tran_excel = os.path.join(str(cur_folder_path.parent), HAT_TRANS_DATA)

    trans_data = pd.read_excel(tran_excel)

    repos = os.listdir(
        os.path.join(str(cur_folder_path), WORKING_FOLDER)
    )

    export_path = os.path.join(cur_folder_path.parent, HAT_FOLDER)

    for repo in repos:

        print(f'Repository:{repo}  Convert Start!!!!')

        data_converter = get_exh_dataconverter(
            os.path.join(str(cur_folder_path), WORKING_FOLDER, repo))
        for (converter, name, author) in data_converter:

            print(f'Converting....     SkinCreater:{author}  SkinName:{name}')

            trans_data = pd.concat([trans_data, pd.DataFrame([dict(zip(TRANS_COLUM, create_data(converter.get_hat_name(), name)))])], ignore_index=True)

            if (trans_data[TRANS_COLUM[0]] == converter.get_hat_name()).sum() == 0:
                trans_data = pd.concat(
                    [
                        trans_data,
                        pd.DataFrame([dict(zip(TRANS_COLUM, create_data(converter.get_hat_name(), name)))])
                    ],
                    ignore_index=True)
                trans_data.append(
                    dict(zip(TRANS_COLUM, create_data(converter.get_hat_name(), name))), ignore_index=True)
            if (trans_data[TRANS_COLUM[0]] == converter.get_author_name()).sum() == 0:

                trans_data = pd.concat(
                    [
                        trans_data,
                        pd.DataFrame([dict(zip(TRANS_COLUM, create_data(converter.get_author_name(), author)))])
                    ],
                    ignore_index=True)
            converter.convert(export_path)

    trans_data = trans_data.rename(columns={TRANS_COLUM[0]:''})
    with pd.ExcelWriter(tran_excel, engine="openpyxl", mode="w") as writer:
        trans_data.to_excel(writer, sheet_name="Hat", index=False)


def create_data(key : str, value :str) -> List[str]:

    data = [""] * len(TRANS_COLUM)
    data[0] = key
    data[12] = value

    return data

if __name__ == '__main__':
    main()