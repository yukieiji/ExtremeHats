import json
import os
from typing import List, Tuple

from exh_data_converter import ExHDataConverter

HAT_DATA = 'CustomHats.json'
HAT_FOLDER = 'hats'

HAT_DATA_KEY = 'hats'

HAT_NAME_KEY = 'name'
HAT_AUTHOR_KEY = 'author'
HAT_FRONT_IMG_KEY = 'resource'
HAT_FRONT_FLIP_IMG_KEY = 'flipresource'
HAT_BACK_IMG_KEY = 'backresource'
HAT_BACK_FLIP_IMG_KEY = 'backflipresource'
HAT_CLIMB_IMG_KEY = 'climbresource'

HAT_ADAPTIVE_KEY = 'adaptive'
HAT_BOUNCE_KEY = 'bounce'

def get_exh_dataconverter(repo : str) -> List[Tuple[ExHDataConverter, str, str]]:

    result = []
    hat_dir = os.path.join(repo, HAT_FOLDER)

    with open(os.path.join(repo, HAT_DATA), mode='r') as hat_file:

        hat_json = json.load(hat_file)

        for hat in hat_json[HAT_DATA_KEY]:

            result.append(
                (
                    ExHDataConverter(
                        hat[HAT_AUTHOR_KEY],
                        hat[HAT_NAME_KEY],
                        HAT_BOUNCE_KEY in hat,
                        HAT_ADAPTIVE_KEY in hat,
                        hat_dir,
                        hat[HAT_FRONT_IMG_KEY],
                        "" if (not HAT_FRONT_FLIP_IMG_KEY in hat) else hat[HAT_FRONT_FLIP_IMG_KEY],
                        "" if (not HAT_BACK_IMG_KEY in hat) else hat[HAT_BACK_IMG_KEY],
                        "" if (not HAT_BACK_FLIP_IMG_KEY in hat) else hat[HAT_BACK_FLIP_IMG_KEY],
                        "" if (not HAT_CLIMB_IMG_KEY in hat) else hat[HAT_CLIMB_IMG_KEY]),
                    hat[HAT_NAME_KEY],
                    hat[HAT_AUTHOR_KEY]
                )
            )

    return result
