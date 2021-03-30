import json
import re
from shapely.geometry import Point, LineString, Polygon


class GirdReader:
    """
    Read melbGrid2.json.
    """
    def __init__(self):
        self.grid_geo_dict = {}

    def read(self, path: str) -> dict:
        with open(path) as f:
            data = json.load(f)
        try:
            features = data['features']

            for feat in features:
                props = feat['properties']

                self.grid_geo_dict[props['id']] = [
                    props['xmin'],
                    props['xmax'],
                    props['ymin'],
                    props['ymax']
                ]
            return self.grid_geo_dict
        except json.decoder.JSONDecodeError as error:
            print(error)

        # if __name__ == "__main__":
        #     print('test begin')
        #     file_path = r'../files/melbGrid2.json'
        #     GReader = GirdReader()
        #     grid_dict = GReader.read(file_path)
        #     print(grid_dict)