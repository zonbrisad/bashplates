#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
# libarary for interacting with bashplates.
#
# File:     bashplates.py
# Author:   Peter Malmberg  <peter.malmberg@gmail.com>
# Org:      
# Date:     2022-07-10
# License:  
# Python:   >= 3.0
#
# ----------------------------------------------------------------------------

# Imports --------------------------------------------------------------------


import readline
import os
import shutil
import sys
import atexit
from enum import Enum
from escape import Esc

# Variables ------------------------------------------------------------------


# Code -----------------------------------------------------------------------


class Bp():

    @staticmethod
    def name() -> str:
        return os.getenv('BP_NAME', "")

    @staticmethod
    def email() -> str:
        return os.getenv('BP_EMAIL', "")

    @staticmethod
    def license() -> str:
        return os.getenv('BP_LICENSE', "")

    @staticmethod
    def organisation() -> str:
        return os.getenv('BP_ORG', "")

    @staticmethod
    def msg(msg: str):
        print(msg)

    @staticmethod
    def msg_ok(msg: str):
        Bp.msg(f"[Ok] {msg}")

    @staticmethod
    def msg_error(msg: str):
        Bp.msg(f"[Error] {msg}")

    @staticmethod
    def mkdir(dir: str) -> bool:
        os.mkdir(dir)
        if os.path.exists(dir):
            Bp.msg_ok(f"Created dir {dir}.")
            return True
        else:
            Bp.msg_error(f"Failed to create dir {dir}.")
            return True

    @staticmethod
    def cp(src: str, dst: str):
        shutil.copyfile(src, dst)
        Bp.msg_ok(f"Copied file to {dst}.")

    C_QUERY : str = Esc.fg_8bit_color(194)
    C_QUERY_DEF : str= Esc.fg_8bit_color(240)
    C_EMPHASIS : str= Esc.fg_8bit_color(255)
    C_DEEMPHASIS : str =Esc.fg_8bit_color(250)

    @staticmethod
    def read_string(question: str, default=None) -> str:
        """Retrieve string input from user

        Args:
            question (str): Question string
            default (str, optional): Return value if pressing enter.
            Defaults to None.

        Returns:
            str: User answer
        """

        #histfile = os.path.join(os.path.expanduser("~"), ".python_history")
        # try:
        #     readline.read_history_file(histfile)
        #     readline.set_history_length(20)
        #     readline.clear_history()
        # except FileNotFoundError:
        #     pass
        # atexit.register(readline.write_history_file, histfile)
             
        while True:
            if default is None:
                s = ""
            else:
                s = default
            #sys.stdout.write(question + f"[{s}]>")
            choice = input(f"{Bp.C_QUERY}{question}{Esc.RESET} {Bp.C_QUERY_DEF}[{Esc.RESET}{s}{Bp.C_QUERY_DEF}]{Esc.RESET} > ")
            #choice = sys.stdin.readline()

            # if choice.isalnum():
            #    return choice

            if choice == "" and default is not None:
                return default
            else:
                return choice

    @staticmethod
    def read_integer(question: str, default=None, min=None, max=None) -> int:
        if default is not None:
            prompt = f"{Bp.C_QUERY_DEF}[{Esc.RESET}{default}{Bp.C_QUERY_DEF}]{Esc.RESET}"
        elif min is None and max is None:
            prompt = ""
        elif isinstance(min, int) and max is None:
            prompt = f"{Bp.C_QUERY_DEF}[{Esc.RESET}{min}-{Bp.C_QUERY_DEF}]{Esc.RESET}"
        elif min is None and isinstance(max, int):
            prompt = f"{Bp.C_QUERY_DEF}[{Esc.RESET}-{max}{Bp.C_QUERY_DEF}]{Esc.RESET}"
        elif isinstance(min, int) and isinstance(max, int):
            prompt = f"{Bp.C_QUERY_DEF}[{Esc.RESET}{min}-{max}{Bp.C_QUERY_DEF}]{Esc.RESET}"

        while True:
            choice = "aa"
            while True:
                choice = input(f"{Bp.C_QUERY}{question}{Esc.RESET} {prompt} > ")
                if choice.isnumeric():
                    val = int(choice)
                    break
                if choice == "" and isinstance(default, int):
                    val = default
                    break
            a = True
            b = True

            if min is not None and (val < min):
                a = False

            if max is not None and (val > max):
                b = False

            if a and b:
                return val

            if default is not None:
                return default

    @staticmethod
    def read_bool(question: str, default=None) -> bool:
        valid_true = ["yes", "y", "ye"]
        valid_false = ["no", "n"]

        if default is None:
            prompt = f"{Bp.C_QUERY_DEF}[{Esc.RESET}y/n{Bp.C_QUERY_DEF}]{Esc.RESET}"
        elif default is True:
            prompt = f"{Bp.C_QUERY_DEF}[{Esc.RESET}Y/n{Bp.C_QUERY_DEF}]{Esc.RESET}"
        elif default is False:
            prompt = f"{Bp.C_QUERY_DEF}[{Esc.RESET}y/N{Bp.C_QUERY_DEF}]{Esc.RESET}"
        else:
            raise ValueError(f"invalid default answer: {default}" )

        while True:
            #sys.stdout.write(f"{question} {prompt}")
            #choice = input().lower()
            choice = input(f"{Bp.C_QUERY}{question}{Esc.RESET} {prompt} > ")

            if choice == "" and default is not None:
                return default

            if choice in valid_true:
                return True

            if choice in valid_false:
                return False

            sys.stdout.write(
                    "Please respond with 'yes' or 'no' (or 'y' or 'n').\n")
    


def main() -> None:
    print(f"Name: {Bp.name()}")
    print(f"Name: {Bp.email()}")
    print(f"Name: {Bp.organisation()}")
    print(f"Name: {Bp.license()}")

    Bp.read_string("String question text", "default")        
    Bp.read_bool("Bool question text", True)        
    Bp.read_bool("Bool question text", False)        
    Bp.read_integer("Integer question text")
    Bp.read_integer("Integer question text", 42)
    #Bp.read_integer("Integer question text", 23, 10, 43)
    Bp.read_integer("Integer question text", None, 10, 43)


if __name__ == "__main__":
    main()
