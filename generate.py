#!/usr/bin/env python

import argparse
from PIL import Image

from maze_generator import generate_maze

parser = argparse.ArgumentParser(description='Generate random maze')
parser.add_argument('--width', type=int, help='width of maze', default=25)
parser.add_argument('--height', type=int, help='height of maze', default=25)
parser.add_argument('--boxsize', type=int, default=40)
parser.add_argument('--linewidth', type=int, default=4)
parser.add_argument('--output', type=str, help='output filepath')

def main():
    args = parser.parse_args()

    screen = generate_maze(
        width=args.width,
        height=args.height,
        box_size=args.boxsize,
        line_width=args.linewidth,
    ) * 255
    image = Image.fromarray(screen)

    if args.output:
        image.convert('RGB').save(args.output)
    else:
        image.show()

if __name__ == '__main__':
    main()
