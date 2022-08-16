import json
import os
import shutil
import re
from typing import Any, Dict

import pykakasi


AUTHOR_KEY = 'Author'
NAME_KEY = 'Name'
FRONT_FLIP_KEY = 'FrontFlip'
BACK_KEY = 'Back'
BACK_FLIP_KEY = 'BackFlip'
CLIMB_KEY = 'Climb'
BOUND_KEY = 'Bound'
SHADER_KEY = 'Shader'
COMIT_HASH_KEY = 'comitHash'

FRONT_IMG = 'front.png'
FRONT_FLIP_IMG = 'front_flip.png'
BACK_IMG = 'back.png'
BACK_FLIP_IMG = 'back_flip.png'
CLIMB_IMG = 'climb.png'
INFO_JSON = 'info.json'

class ExHDataConverter:

    def __init__(
        self,
        author : str,
        hat_name : str,
        bound : bool,
        adaptive : bool,
        img_dir : str,
        front_img_name : str,
        front_flip_img_name : str = "",
        back_img_name : str = "",
        back_flip_img_name : str = "",
        climb_img_name : str = ""):

        self.__author : str = self.__clean(author)
        self.__hat_name : str = self.__clean(hat_name)

        self.__bound : bool = bound
        self.__adaptive : bool = adaptive

        self.__img_dir : str = img_dir

        self.__front_img_name : str = front_img_name
        self.__front_flip_img_name : str = front_flip_img_name
        self.__back_img_name : str = back_img_name
        self.__back_flip_img_name : str = back_flip_img_name
        self.__climb_img_name : str = climb_img_name

    def get_author_name(self) -> str:
        return self.__author

    def get_hat_name(self) -> str:
        return self.__hat_name

    def create_info(self) -> Dict[str, Any]:

        info = {}
        info[AUTHOR_KEY] = self.__author
        info[NAME_KEY] = self.__hat_name
        info[FRONT_FLIP_KEY] = False if self.__front_flip_img_name == "" else True
        info[BACK_KEY] = False if self.__back_img_name == "" else True
        info[BACK_FLIP_KEY] = False if self.__back_flip_img_name == "" else True
        info[CLIMB_KEY] = False if self.__climb_img_name == "" else True

        info[SHADER_KEY] = self.__adaptive
        info[BOUND_KEY] = self.__bound
        info[COMIT_HASH_KEY] = ""

        return info

    def convert(self, path : str) -> None:

        copy_folder = os.path.join(path, self.__hat_name)

        if os.path.exists(copy_folder):
            shutil.rmtree(copy_folder)

        os.makedirs(copy_folder, exist_ok=True)

        shutil.copyfile(
            os.path.join(self.__img_dir, self.__front_img_name),
            os.path.join(copy_folder, FRONT_IMG))

        if self.__front_flip_img_name != "":
            shutil.copyfile(
                os.path.join(self.__img_dir, self.__front_flip_img_name),
                os.path.join(copy_folder, FRONT_FLIP_IMG))

        if self.__back_img_name != "":
            shutil.copyfile(
                os.path.join(self.__img_dir, self.__back_img_name),
                os.path.join(copy_folder, BACK_IMG))

        if self.__back_flip_img_name != "":
            shutil.copyfile(
                os.path.join(self.__img_dir, self.__back_flip_img_name),
                os.path.join(copy_folder, BACK_FLIP_IMG))

        if self.__climb_img_name != "":
            shutil.copyfile(
                os.path.join(self.__img_dir, self.__climb_img_name),
                os.path.join(copy_folder, CLIMB_IMG))

        with open(os.path.join(copy_folder, INFO_JSON), mode="w") as file:
            json.dump(self.create_info(), file, indent=2, ensure_ascii=False)

    def __clean(self, not_clean_str : str) -> str:

        if not_clean_str.isascii():
            return self.regex_clean(not_clean_str)

        kks = pykakasi.kakasi()
        result = kks.convert(not_clean_str)

        cleaned_str = ""

        for item in result:
            cleaned_str += item['hepburn']

        return self.regex_clean(cleaned_str)

    def regex_clean(self, not_cleen_str : str) -> str:

        cleaned_str = re.sub('<.*?>', '', not_cleen_str)
        cleaned_str = re.sub('^-\\s*', '', cleaned_str)
        cleaned_str = re.sub('<.*?>', '', cleaned_str)
        cleaned_str = re.sub(':', '', cleaned_str)

        return cleaned_str
