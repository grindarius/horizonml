import random
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

random.seed(331502)
np.random.seed(331502)

class Pixel:
    pixel_top_left: int = 0
    pixel_top_right: int = 0
    pixel_bottom_left: int = 0
    pixel_bottom_right: int = 0
    '''
    Shape of the pixel, could be only 'vertical', 'horizontal', 'diagonal', 'blank', 'solid' and 'unknown'
    '''
    shape: str = ''

    @staticmethod
    def _determine_shape(
        pixel_top_left: int,
        pixel_top_right: int,
        pixel_bottom_left: int,
        pixel_bottom_right: int
    ) -> str:
        if pixel_top_left == 1 and pixel_top_right == 1 and pixel_bottom_left == 0 and pixel_bottom_right == 0:
            return 'horizontal'
        elif pixel_top_left == 0 and pixel_top_right == 0 and pixel_bottom_left == 1 and pixel_bottom_right == 1:
            return 'horizontal'
        elif pixel_top_left == 1 and pixel_top_right == 0 and pixel_bottom_left == 1 and pixel_bottom_right == 0:
            return 'vertical'
        elif pixel_top_left == 0 and pixel_top_right == 1 and pixel_bottom_left == 0 and pixel_bottom_right == 1:
            return 'vertical'
        elif pixel_top_left == 1 and pixel_top_right == 0 and pixel_bottom_left == 0 and pixel_bottom_right == 1:
            return 'diagonal'
        elif pixel_top_left == 0 and pixel_top_right == 1 and pixel_bottom_left == 1 and pixel_bottom_right == 0:
            return 'diagonal'
        elif pixel_top_left == 0 and pixel_top_right == 0 and pixel_bottom_left == 0 and pixel_bottom_right == 0:
            return 'blank'
        elif pixel_top_left == 1 and pixel_top_right == 1 and pixel_bottom_left == 1 and pixel_bottom_right == 1:
            return 'solid'
        else:
            return 'unknown'
    
    def to_dictionary(self):
        return {
            'pixel_top_left': self.pixel_top_left,
            'pixel_top_right': self.pixel_top_right,
            'pixel_bottom_left': self.pixel_bottom_left,
            'pixel_bottom_right': self.pixel_bottom_right,
            'shape': self.shape
        }

    @staticmethod
    def get_random_shape():
        pixel = Pixel(*[random.randint(0, 1) for _ in range(4)])
        return pixel.to_dictionary()

    def __init__(self, pixel_top_left: int, pixel_top_right: int, pixel_bottom_left: int, pixel_bottom_right: int) -> None:
        self.pixel_top_left = pixel_top_left
        self.pixel_top_right = pixel_top_right
        self.pixel_bottom_left = pixel_bottom_left
        self.pixel_bottom_right = pixel_bottom_right
        self.shape = Pixel._determine_shape(
            pixel_top_left,
            pixel_top_right,
            pixel_bottom_left,
            pixel_bottom_right
        )

if __name__ == '__main__':
    # * initializing data
    df = pd.DataFrame(
        data=np.random.randint(2, size=(60000, 4)),
        columns=['pixel_top_left', 'pixel_top_right', 'pixel_bottom_left', 'pixel_bottom_right']
    )

    df['shape'] = df.apply(
        lambda row: Pixel._determine_shape(
            row['pixel_top_left'], row['pixel_top_right'], row['pixel_bottom_left'], row['pixel_bottom_right']
        ),
        axis=1
    )

    print(df.describe())
    print(df.head(10))
    print(df['shape'].value_counts())

    train_data, test_data = train_test_split(df, test_size=0.2, random_state=331502)

    print(f'train size = {train_data.shape}')
    print(f'test size = {test_data.shape}')
