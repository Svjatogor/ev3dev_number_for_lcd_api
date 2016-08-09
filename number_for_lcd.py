#!/usr/bin/env python

# Hard coding these values is not a good idea because the values could
# change. But, since this is an example, we want to keep it short.

import os
import array

class NumberDrawer(object):
    """docstring for NumberDrawer"""
    SCREEN_WIDTH = 178 # pixels
    SCREEN_HEIGHT = 128 # pixels
    LINE_LENGTH = 24 # bytes
    SIZE = 3072 # bytes
    def __init__(self):
        self.buf = [0] * self.SIZE
        self.width = 6
        self.height = 12
        self.left_up_point = {'x' : 8, 'y' : 2}
    def draw_number(self, number):
        self.clear_lcd()
        if number == 0:
            self.draw_zero()
        elif number == 1:
            self.draw_one()
        elif number == 2:
            self.draw_two()
        elif number == 3:
            self.draw_three()
        elif number == 4:
            self.draw_four()
        elif number == 5:
            self.draw_five()
        elif number == 6:
            self.draw_six()
        elif number == 7:
            self.draw_seven()
        elif number == 8:
            self.draw_eight()
        elif number == 9:
            self.draw_nine()
        else:
            pass
    # draw zero
    def draw_zero(self):
        self.draw_horizontal_line('up')
        self.draw_horizontal_line('down')
        self.draw_vertical_line('left', 'up', 'big')
        self.draw_vertical_line('right', 'up', 'big')
        self.draw()
    # draw one
    def draw_one(self):
        self.draw_diagonal_line('up', 'small')
        self.draw_vertical_line('right', 'up', 'big')
        self.draw()
    # draw two
    def draw_two(self):
        self.draw_horizontal_line('up')
        self.draw_vertical_line('right', 'up', 'small')
        self.draw_vertical_line('left', 'up', 'small')
        self.draw_diagonal_line('mid', 'small')
        self.draw_horizontal_line('down')
        self.draw()
    # draw three
    def draw_three(self):
        self.draw_horizontal_line('up')
        self.draw_diagonal_line('up', 'small')
        self.draw_horizontal_line('mid')
        self.draw_vertical_line('right', 'down', 'small')
        self.draw_horizontal_line('down')
        self.draw()
    # draw four
    def draw_four(self):
        self.draw_vertical_line('left', 'up', 'small')
        self.draw_horizontal_line('mid')
        self.draw_vertical_line('right', 'up', 'big')
        self.draw()
    # draw five
    def draw_five(self):
        self.draw_horizontal_line('up')
        self.draw_horizontal_line('mid')
        self.draw_horizontal_line('down')
        self.draw_vertical_line('left', 'up', 'small')
        self.draw_vertical_line('right', 'down', 'small')
        self.draw()
    # draw six
    def draw_six(self):
        self.draw_diagonal_line('up', 'small')
        self.draw_horizontal_line('mid')
        self.draw_horizontal_line('down')
        self.draw_vertical_line('left', 'down', 'small')
        self.draw_vertical_line('right', 'down', 'small')
        self.draw()
    # draw seven
    def draw_seven(self):
        self.draw_horizontal_line('up')
        self.draw_diagonal_line('up', 'big')
        self.draw()
    # draw eight
    def draw_eight(self):
        self.draw_horizontal_line('up')
        self.draw_horizontal_line('mid')
        self.draw_horizontal_line('down')
        self.draw_vertical_line('left', 'up', 'big')
        self.draw_vertical_line('right', 'up', 'big')
        self.draw()
    # draw nine
    def draw_nine(self):
        self.draw_horizontal_line('up')
        self.draw_vertical_line('left', 'up', 'small')
        self.draw_vertical_line('right', 'up')
        self.draw_horizontal_line('mid')
        self.draw_horizontal_line('down')
        self.draw()
    # clear lcd
    def clear_lcd(self):
        self.buf = [0] * self.SIZE
        self.draw()
    # draw horizontal line in start_y row  height 8 pixels
    def draw_horizontal_line(self, position):
        row_to_draw = 0

        if position == 'up':
            row_to_draw = self.left_up_point['y']
        elif position == 'mid':
            row_to_draw = self.left_up_point['y'] + self.height / 2
        elif position == 'down':
            row_to_draw = self.left_up_point['y'] + self.height
        # convert to 16 bit format imafe
        row_to_draw *= 8
        for row in range(row_to_draw, row_to_draw + 8):
            for col in range(self.left_up_point['x'], self.left_up_point['x'] + self.width):
                self.buf[row * self.LINE_LENGTH + col] = 0xff
    # draw vertical line in start_x colunm width 8 pixels
    def draw_vertical_line(self, position_horizontal, position_vertical, type_line = 'big'):
        colunm_to_draw = 0
        row_to_draw = 0
        height = self.height
        # calc column to draw
        if position_horizontal == 'left':
            colunm_to_draw = self.left_up_point['x']
        elif position_horizontal == 'right':
            colunm_to_draw = self.left_up_point['x'] + self.width
        # update height
        if position_vertical == 'up':
            row_to_draw = self.left_up_point['y']
            if type_line == 'small':
                height /= 2;
        elif position_vertical == 'down':
            height /= 2
            row_to_draw = self.left_up_point['y'] + height
        # convert to 16 bit format imafe
        row_to_draw *= 8
        for row in range(row_to_draw, row_to_draw + height * 8):
            self.buf[row * self.LINE_LENGTH + colunm_to_draw] = 0xff
    # draw diagonal line start in row start_y
    def draw_diagonal_line(self, position_vertical, type_line  = 'small'):
        row_start = 0

        height = self.height * 8

        if type_line == 'small':
            height /= 2

        if position_vertical == 'up':
            row_start = self.left_up_point['y'] * 8
        elif position_vertical == 'mid':
            row_start = self.left_up_point['y'] * 8 + height

        column_start = self.left_up_point['x'] + self.width

        column = column_start
        row_steps = row_start
        add_to_big = 0;
        while row_steps < row_start + height:
            row_for_line = row_steps
            while row_for_line < row_steps + 8 and row_for_line < row_start + height:
                self.buf[row_for_line * self.LINE_LENGTH + column] = 0xff
                row_for_line += 1
            if type_line == 'small' or (type_line == 'big' and add_to_big < height / 2):
                column -= 1
            row_steps += 8
            add_to_big += 8
    # write in lcd file
    def draw(self):
        f = os.open('/dev/fb0', os.O_RDWR)
        s = array.array('B', self.buf).tostring()
        os.write(f, s)
        os.close(f)
