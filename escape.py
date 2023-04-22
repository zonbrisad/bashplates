#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#----------------------------------------------------------------------------
#
# A bashplate like python script
#
# File:    bpp.py
# Author:  Peter Malmberg <peter.malmberg@gmail.com>
# Date:    2022-05-22
# License: MIT
# Python:  3
#
#----------------------------------------------------------------------------
# Pyplate
#   This file is generated from pyplate Python template generator.
#
# Pyplate is developed by:
#   Peter Malmberg <peter.malmberg@gmail.com>
#
# Available at:
#   https://github.com/zobrisad/pyplate.git
#
# ---------------------------------------------------------------------------
#
# https://en.wikipedia.org/wiki/ANSI_escape_code#3-bit_and_4-bit
# https://gist.github.com/fnky/458719343aabd01cfb17a3a4f7296797
# https://www.ditig.com/256-colors-cheat-sheet
# https://michurin.github.io/xterm256-color-picker/
#
#

from __future__ import annotations
from dataclasses import dataclass
import subprocess
import enum
import logging
import os
from enum import Enum, auto

    
class Esc:
    ETX = '\x03'               # End of text(ETX), CTRL-C
    ESCAPE = "\x1b"

    """ ANSI foreground colors codes """
    BLACK = "\x1b[0;30m"        # Black
    RED = "\x1b[0;31m"          # Red
    GREEN = '\x1b[0;32m'        # Green
    YELLOW = '\x1b[0;33m'       # Yellow
    BLUE = '\x1b[0;34m'         # Blue
    MAGENTA = '\x1b[0;35m'      # Magenta
    CYAN = '\x1b[0;36m'         # Cyan
    WHITE = '\x1b[0;37m'        # Gray
    DARKGRAY = '\x1b[1;30m'     # Dark Gray
    BR_RED = '\x1b[1;31m'       # Bright Red
    BR_GREEN = '\x1b[1;32m'     # Bright Green
    BR_YELLOW = '\x1b[1;33m'    # Bright Yellow
    BR_BLUE = '\x1b[1;34m'      # Bright Blue
    BR_MAGENTA = '\x1b[1;35m'   # Bright Magenta
    BR_CYAN = '\x1b[1;36m'      # Bright Cyan
    BR_WHITE = '\x1b[1;37m'     # White

    # ANSI background color codes
    #
    BG_BLACK = '\x1b[40m'       # Black
    BG_RED = '\x1b[41m'         # Red
    BG_GREEN = '\x1b[42m'       # Green
    BG_YELLOW = '\x1b[43m'      # Yellow
    BG_BLUE = '\x1b[44m'        # Blue
    BG_MAGENTA = '\x1b[45m'     # Magenta
    BG_CYAN = '\x1b[46m'        # Cyan
    BG_WHITE = '\x1b[47m'       # White

    # ANSI Text attributes
    NORMAL = "\x1b[0m"       # Reset attributes
    BOLD = "\x1b[1m"         # bold font
    LOWINTENSITY = "\x1b[2m" # Low intensity/faint/dim
    ITALIC = "\x1b[3m"       # Low intensity/faint/dim
    UNDERLINE = "\x1b[4m"    # Underline
    SLOWBLINK = "\x1b[5m"    # Slow blink
    FASTBLINK = "\x1b[6m"    # Fast blink
    REVERSE = "\x1b[7m"      # Reverse video
    CROSSED = "\x1b[9m"      # Crossed text
    FRACTUR = "\x1b[20m"     # Gothic
    FRAMED = "\x1b[51m"      # Framed 
    OVERLINED = "\x1b[53m"   # Overlined 
    SUPERSCRIPT = "\x1b[73m" # Superscript
    SUBSCRIPT = "\x1b[74m"   # Subscript
    
    END = "\x1b[0m"
    CLEAR = "\x1b[2J"
    RESET = "\x1b[m"
    
    WONR = "\x1b[1;47\x1b[1;31m"

    # ANSI cursor operations
    #
    RETURN = "\x1b[F"           # Move cursor to begining of line
    UP = "\x1b[A"               # Move cursor one line up
    DOWN = "\x1b[B"             # Move cursor one line down
    FORWARD = "\x1b[C"          # Move cursor forward
    BACK = "\x1b[D"             # Move cursor backward
    HIDE = "\x1b[?25l"          # Hide cursor
    END = "\x1b[m"              # Clear Attributes

    # ANSI movement codes 
    CUR_UP = '\x1b[A'         # cursor up
    CUR_DOWN = '\x1b[B'       # cursor down
    CUR_FORWARD = '\x1b[C'    # cursor forward
    CUR_BACK = '\x1b[D'       # cursor back
    CUR_RETURN = '\x1b[F'     # cursor return
    
    CUR_HIDE = '\x1b[?25l'      # hide cursor
    CUR_SHOW = '\x1b[?25h'      # show cursor

    KEY_HOME = '\x1b[1~'      # Home
    KEY_INSERT = '\x1b[2~'    # 
    KEY_DELETE = '\x1b[3~'    # 
    KEY_END = '\x1b[4~'       # 
    KEY_PGUP = '\x1b[5~'      # 
    KEY_PGDN = '\x1b[6~'      # 
    KEY_HOME = '\x1b[7~'      # 
    KEY_END = '\x1b[8~'       # 
    KEY_F0 = '\x1b[10~'       # F
    KEY_F1 = '\x1b[11~'       # F
    KEY_F2 = '\x1b[12~'       # F
    KEY_F3 = '\x1b[13~'       # F
    KEY_F4 = '\x1b[14~'       # F
    KEY_F5 = '\x1b[15~'       # F
    KEY_F6 = '\x1b[17~'       # F
    KEY_F7 = '\x1b[18~'       # F
    KEY_F8 = '\x1b[19~'       # F
    KEY_F9 = '\x1b[20~'       # F
    KEY_F10 = '\x1b[21~'      # F
    KEY_F11 = '\x1b[23~'      # F
    KEY_F12 = '\x1b[24~'      # F
    KEY_F13 = '\x1b[25~'      # F
    KEY_F14 = '\x1b[26~'      # F
    KEY_F15 = '\x1b[28~'      # F
    KEY_F16 = '\x1b[29~'      # F

    E_RET  = 100
    E_UP   = 101
    E_DOWN = 102
    
    x = [ CUR_RETURN, CUR_UP, CUR_DOWN ]
    y = { E_RET:CUR_RETURN, 
          E_UP:CUR_UP, 
          E_DOWN:CUR_DOWN }

    @staticmethod
    def fg_8bit_color(c :int) -> str:
        return f"\x1b[38;5;{c}m"

    @staticmethod
    def bg_8bit_color(c :int) -> str:
        return f"\x1b[48;5;{c}m"

    @staticmethod
    def findEnd(data, idx):
        i = idx
        while (i-idx) < 12:
            ch = data.at(i)
            if ch.isalpha():
                return i
            else:
                i += 1
        return -1

    @staticmethod
    def is_escape_seq(s: str) -> bool:
        if s[0] == Esc.ESCAPE:
            return True
        else:
            return False



@dataclass
class TColor():
    BLACK : str = "#2e3436"
    RED : str = "#cc0000"
    GREEN : str = "#4e9a06"
    YELLOW : str = "#c4a000"
    BLUE : str = "#3465a4"
    MAGENTA : str = "#75507b"
    CYAN : str = "#06989a"
    WHITE : str = "#d3d7cf"
    BRIGHT_BLACK : str = "#555753"
    BRIGHT_RED : str = "#ef2929"
    BRIGHT_GREEN : str = "#8ae234"
    BRIGHT_YELLOW : str = "#fce94f"
    BRIGHT_BLUE : str = "#729fcf"
    BRIGHT_MAGENTA : str = "#ad7fa8"
    BRIGHT_CYAN : str = "#34e2e2"
    BRIGHT_WHITE : str = "#eeeeec"


FLAG_BLUE="\x1b[48;5;20m"
FLAG_YELLOW="\x1b[48;5;226m"

flag = f"""
{FLAG_BLUE}     {FLAG_YELLOW}  {FLAG_BLUE}          {Esc.END}
{FLAG_BLUE}     {FLAG_YELLOW}  {FLAG_BLUE}          {Esc.END}
{FLAG_YELLOW}                 {Esc.END}
{FLAG_BLUE}     {FLAG_YELLOW}  {FLAG_BLUE}          {Esc.END}
{FLAG_BLUE}     {FLAG_YELLOW}  {FLAG_BLUE}          {Esc.END}
"""
escape_attribute_test = f"""  
{Esc.UNDERLINE}Font attributes{Esc.END}

{Esc.NORMAL}Normal text{Esc.END}
{Esc.BOLD}Bold text{Esc.NORMAL}
{Esc.LOWINTENSITY}Dim text{Esc.NORMAL}
{Esc.ITALIC}Italic text{Esc.NORMAL}
{Esc.UNDERLINE}Underline text{Esc.NORMAL}
{Esc.SLOWBLINK}Slow blinking text{Esc.NORMAL}
{Esc.FASTBLINK}Fast blinking text{Esc.NORMAL}
{Esc.FRAMED}Framed text{Esc.NORMAL}
Subscript{Esc.SUBSCRIPT}text{Esc.NORMAL}
Superscript{Esc.SUPERSCRIPT}text{Esc.NORMAL}
{Esc.FRACTUR}Fractur/Gothic text{Esc.NORMAL}
{Esc.CROSSED}Crossed text{Esc.NORMAL}

{Esc.UNDERLINE}Standard foreground color attributes{Esc.END}

{Esc.BLACK}Black{Esc.END}
{Esc.RED}Red{Esc.NORMAL}
{Esc.GREEN}Green{Esc.END}
{Esc.YELLOW}Yellow{Esc.END}
{Esc.BLUE}Blue{Esc.END}
{Esc.MAGENTA}Magenta{Esc.END}
{Esc.CYAN}Cyan{Esc.END}
{Esc.WHITE}WHITE{Esc.END}
{Esc.WHITE}White{Esc.END}
{Esc.DARKGRAY}Dark Gray{Esc.END}
{Esc.BR_RED}Bright Red{Esc.END}
{Esc.BR_GREEN}Bright Green{Esc.END}
{Esc.BR_YELLOW}Bright Yellow{Esc.END}
{Esc.BR_BLUE}Bright Blue{Esc.END}
{Esc.BR_MAGENTA}Bright Magenta{Esc.END}
{Esc.BR_CYAN}Bright Cyan{Esc.END}

{Esc.UNDERLINE}Standard background color attributes{Esc.END}

{Esc.BG_BLACK} Black {Esc.END}
{Esc.BG_RED} Red {Esc.END}
{Esc.BG_GREEN} Green {Esc.END}
{Esc.BG_YELLOW} Yellow {Esc.END}
{Esc.BG_BLUE} Blue {Esc.END}
{Esc.BG_MAGENTA} Magenta {Esc.END}
{Esc.BG_CYAN} Cyan {Esc.END}

{Esc.UNDERLINE}256 Color attributes{Esc.END}
{Esc.fg_8bit_color(12)}Color 12{Esc.END}
{Esc.fg_8bit_color(45)}Color 45{Esc.END}
{Esc.fg_8bit_color(240)}Color 240{Esc.END}
{Esc.bg_8bit_color(32)}Color 32{Esc.END}
{Esc.bg_8bit_color(78)}Color 78{Esc.END}
{Esc.bg_8bit_color(249)}Color 249{Esc.END}

"""

def main() -> None:
    logging.basicConfig(format="[%(levelname)s] Line: %(lineno)d %(message)s", level=logging.DEBUG)
   
    #print(escape_attribute_test)
    #print(flag)

    



if __name__ == "__main__":
    main()
