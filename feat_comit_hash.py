import sys

import os
import json
from pathlib import Path
from typing import List

HAT_DIR = os.path.join(
  os.path.dirname(os.path.realpath(__file__)), 'hat')
HAT_INFO_UPDATE_COMIT_KEY = 'comitHash'
HAT_INFO_NAME = 'info.json'

def get_hat_dir_name(change_files : List[str]) -> List[str]:

  hat_dir = []

  for path in change_files:

    check_path = Path(path)
    parent = check_path.parent

    is_hat_dir = parent.is_dir()
    hat_name = parent.parts[-1]
    if is_hat_dir and not (hat_name in hat_dir):
      hat_dir.append(hat_name)

  return hat_dir

def feat_comit_hash(comit_hash: str, hat_name: List[str]):

  for hat in hat_name:
    info_path = os.path.join(HAT_DIR, hat, HAT_INFO_NAME)
    if os.path.exists(info_path):
      with open(os.path.join(info_path), mode='r') as info:
        hat_info = json.load(info)

      hat_info[HAT_INFO_UPDATE_COMIT_KEY] = comit_hash
      with open(os.path.join(info_path), mode='w') as hat_json:
        json.dump(
          hat_info,
          hat_json, indent=2, ensure_ascii=False)

def main(comit_hash: str, change_files: List[str]) -> None:
  feat_comit_hash(
    comit_hash,
    get_hat_dir_name(change_files))


if __name__ == "__main__":
  comit_hash = sys.argv[1]
  change_files = sys.argv[2:]
  print(f"comit_hash: {comit_hash}")
  print(f"change_files : {change_files}")
  main(comit_hash, change_files)