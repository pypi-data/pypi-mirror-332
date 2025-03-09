# Driver library for LCD display. Provided by Ryanteck LTD.
# The procedures below can all be called in your own code!
# You can just stick to the print string one though ;-)

# This is the driver library for the LCD display
# It contains some functions that you can call in your own program
# Just remember that in order to use it you have to import it
# You can do that with the line: import lcddriver
# Make sure that lcddriver is in the same directory though!
# Credit for this code goes to "natbett" of the Raspberry Pi Forum 18/02/13

import smbus
from time import *

# LCD Address
ADDRESS = 0x27

# commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

En = 0b00000100 # Enable bit
Rw = 0b00000010 # Read/Write bit
Rs = 0b00000001 # Register select bit

class I2C_Device:
    def __init__(self, addr, port=1):
        self.addr = addr
        self.bus = smbus.SMBus(port)

    # Write a single command
    def write_cmd(self, cmd):
        self.bus.write_byte(self.addr, cmd)
        sleep(0.0001)

    # Write a command and argument
    def write_cmd_arg(self, cmd, data):
        self.bus.write_byte_data(self.addr, cmd, data)
        sleep(0.0001)

    # Write a block of data
    def write_block_data(self, cmd, data):
        self.bus.write_block_data(self.addr, cmd, data)
        sleep(0.0001)

    # Read a single byte
    def read(self):
        return self.bus.read_byte(self.addr)

    # Read
    def read_data(self, cmd):
        return self.bus.read_byte_data(self.addr, cmd)

    # Read a block of data
    def read_block_data(self, cmd):
        return self.bus.read_block_data(self.addr, cmd)


class LCD:
    def __init__(self, port=1):
        self.device = I2C_Device(ADDRESS, port)

        self.write(0x03)
        self.write(0x03)
        self.write(0x03)
        self.write(0x02)

        self.write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
        self.write(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
        self.write(LCD_CLEARDISPLAY)
        self.write(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
        sleep(0.2)

        self.define_chars()
        sleep(0.2)

    def set_backlight(self, value):
        if value:
            self.device.write_cmd(LCD_BACKLIGHT)
        else:
            self.device.write_cmd(LCD_NOBACKLIGHT)

    # clocks EN to latch command
    def strobe(self, data):
        self.device.write_cmd(data | En | LCD_BACKLIGHT)
        sleep(.0005)
        self.device.write_cmd(((data & ~En) | LCD_BACKLIGHT))
        sleep(.0001)

    def write_four_bits(self, data):
        self.device.write_cmd(data | LCD_BACKLIGHT)
        self.strobe(data)

    # write a command to lcd
    def write(self, cmd, mode=0):
        self.write_four_bits(mode | (cmd & 0xF0))
        self.write_four_bits(mode | ((cmd << 4) & 0xF0))

    # put string function
    def display_string(self, string, line):
        if line == 1:
            self.write(0x80)
        if line == 2:
            self.write(0xC0)
        if line == 3:
            self.write(0x94)
        if line == 4:
            self.write(0xD4)

        for char in string:
            self.write(ord(char), Rs)

    # clear lcd and set to home
    def clear(self):
        self.write(LCD_CLEARDISPLAY)
        self.write(LCD_RETURNHOME)

    # define characters for positions
    def define_chars(self):
        characters = [
            [0x00, 0x1f, 0x00, 0x1f, 0x00, 0x1f, 0x00, 0x1f],  # stripes
            [0x00, 0x04, 0x15, 0x04, 0x1f, 0x04, 0x0e, 0x04],  # abs
            [0x00, 0x00, 0x15, 0x1f, 0x1f, 0x1f, 0x00, 0x00],  # queen
            [0x00, 0x00, 0x0e, 0x1f, 0x15, 0x1f, 0x1f, 0x0a],  # skulls
            [0x00, 0x15, 0x0a, 0x15, 0x0a, 0x15, 0x0a, 0x00],  # checks
        ]

        for i, character in enumerate(characters):
            self.write(0x40 + (0x08 * i))
            for line in character:
                self.write(line, Rs)
