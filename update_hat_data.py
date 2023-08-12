import os
import json

from pylightxl import readxl

WORKING_DIR = os.path.dirname(os.path.realpath(__file__))

HAT_DATA_JSON = 'hatData.json'
HAT_TRANS_DATA_JSON = 'hatTranData.json'
HAT_IN_FILE = os.path.join(WORKING_DIR, 'HatTransData.xlsx')
HAT_OUT_FILE = os.path.join(WORKING_DIR, 'hat', HAT_TRANS_DATA_JSON)
HAT_FOLDER = os.path.join(WORKING_DIR, 'hat')
HAT_DATA_FILE = os.path.join(WORKING_DIR, 'hat', HAT_DATA_JSON)

HAT_DATA_DATA_KEY = 'data'
HAT_DATA_UPDATE_COMIT_KEY = 'updateComitHash'

def string_to_json(filename, outputFile) -> None:
  
  wb = readxl(filename)

  xlsx_data = {}

  for name in wb.ws_names:

    sheat = wb.ws(name)

    row, col = sheat.size

    # 行を回す
    for i in range(2, row + 1):

      data = {}

      # i行目の1列目はキー
      key = sheat.index(i, 1)
      if key == "":
        continue

      # i行目j列がデータ、jは2以上であり2が0(英語)である
      for j in range(2, col + 1):
          cell_data = sheat.index(i, j)

          if type(cell_data) != str or cell_data == "":
            continue

          # I hate excel why did I do this to myself
          data[str(j - 2)] = cell_data.replace("\r", "").replace("_x000D_", "").replace("\\n", "\n")

      if data != {}:
        xlsx_data[key] = data

  with open(outputFile, "w") as f:
    json.dump(xlsx_data, f, indent=4)

def update_hat_data():

  hats = os.listdir(HAT_FOLDER)

  hats.remove(HAT_DATA_JSON)
  hats.remove(HAT_TRANS_DATA_JSON)

  with open(os.path.join(HAT_DATA_FILE), mode='w') as hat_json:
    json.dump(
      {HAT_DATA_DATA_KEY:hats, HAT_DATA_UPDATE_COMIT_KEY:""},
      hat_json, indent=2, ensure_ascii=False)

def main():
  string_to_json(HAT_IN_FILE, HAT_OUT_FILE)
  update_hat_data()

if __name__ == "__main__":
  main()