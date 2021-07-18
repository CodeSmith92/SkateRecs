import pandas as pd
import argparse
import os

local_path = os.path.dirname(os.path.abspath(__file__))

# CLI arguments
parser = argparse.ArgumentParser(description='Command line arguments for skate size and model suggestions.')

parser.add_argument('--shoe_size', type=float, choices=[6, 6.5, 7, 7.5, 8, 8.5, 9, 9.5, 10, 10.5, 11, 11.5, 12],
                    help='US M shoe size. Only accepted inputs are sizes 6-12, in increments of 0.5.',
                    required=True)
parser.add_argument('--foot_width', type=float, help='Widest part of foot in centimeters (trace foot w/socks on).',
                    required=True)
parser.add_argument('--foot_length', type=float, help='Optional input. Foot length in centimeters.')

# TODO: parser.add_argument('--experience', type=str, choices=['beginner', 'intermediate', 'advanced'],
#  help='Optional input')

args = parser.parse_args()


def sizetoLength():
    shoe_size = args.shoe_size

    # Length is in units of cm
    if shoe_size == 12:
        foot_length = 29.1
    elif shoe_size == 11.5:
        foot_length = 28.7
    elif shoe_size == 11:
        foot_length = 28.3
    elif shoe_size == 10.5:
        foot_length = 27.9
    elif shoe_size == 10:
        foot_length = 27.45
    elif shoe_size == 9.5:
        foot_length = 27.0
    elif shoe_size == 9:
        foot_length = 26.6
    elif shoe_size == 8.5:
        foot_length = 26.2
    elif shoe_size == 8:
        foot_length = 25.75
    elif shoe_size == 7.5:
        foot_length = 25.3
    elif shoe_size == 7:
        foot_length = 25.0
    elif shoe_size == 6.5:
        foot_length = 24.7
    else:
        shoe_size == 6
        foot_length = 24.3

    print(f'Default foot length: {foot_length} cm')
    return foot_length


def getWidthRatio():
    foot_width = args.foot_width

    if args.foot_length:
        foot_length = args.foot_length
        print(f'foot length: {foot_length} cm')

        width_ratio = foot_length / foot_width

        return width_ratio

    else:
        foot_length = sizetoLength()
        width_ratio = foot_length / foot_width

        return width_ratio


def getSkateVolume():
    width_ratio = getWidthRatio()
    print(f'length-to-width ratio: {round(width_ratio, 2)}')

    if width_ratio >= 3.1:
        volume = 'low'
        boot_width = ['standard']
    elif width_ratio >= 3.0:
        volume = 'low-medium'
    elif width_ratio >= 2.9:
        volume = 'low-medium'
    elif width_ratio > 2.5:
        volume = 'medium-volume'
    else:
        volume = 'higher-volume'

    print(f'Suggested skate volume based on length-to-width ratio: {volume}')
    return volume


def main():
    width = args.foot_width
    if width <= 0 | width >= 20:
        raise argparse.ArgumentTypeError(f"{width} is an invalid (human) foot width")
    return width

    shoe_size = args.shoe_size
    skate_size = shoe_size - 1.5
    print(f'Suggested Bauer and CCM skate size: {skate_size}')

    vol = getSkateVolume()

    print('Skate fit/model suggestions:')
    if vol == 'lower-volume':
        data = [('CCM', 'JetSpeed', 'D', 'low-medium'), ('Bauer', 'Vapor', 'D', 'low')]

        df = pd.DataFrame(data, columns=['Manufacturer', 'Skate Model', 'Width', 'Skate Volume'])
        print(df)

    elif vol == 'medium-volume':
        data = [('CCM', 'Super Tacks', 'D', 'medium'), ('CCM', 'Tacks', 'D', 'medium'),
                ('CCM', 'JetSpeed', 'EE', 'medium'), ('Bauer', 'Supreme', 'D',
                                                      'medium')]

        df = pd.DataFrame(data, columns=['Manufacturer', 'Skate Model', 'Width', 'Skate Volume'])
        print(df)

    else:
        data = [('CCM', 'Super Tacks', 'EE', 'medium-high'), ('CCM', 'RBZ', 'D', 'high'), ('Bauer', 'Nexus', 'D',
                                                                                           'high')]

        df = pd.DataFrame(data, columns=['Manufacturer', 'Skate Model', 'Width', 'Skate Volume'])
        print(df)
        print('NOTE: CCM recommends sizing down 2 sizes from shoe size for the RBZ skate line.')
        print(f'RBZ skate size: {shoe_size - 2.0}')

    # Output
    out_path = os.path.join(local_path, 'skate_recs.csv')
    df.to_csv(out_path, index=False)


if __name__ == '__main__':
    main()
