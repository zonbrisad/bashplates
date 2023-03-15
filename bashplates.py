#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ----------------------------------------------------------------------------
#
# libarary for interacting with bashplates.
#
# File:     bashplates.py
# Author:   Peter Malmberg  <peter.malmberg@gmail.com>
# Org:      __ORGANISTATION__
# Date:     2022-07-10
# License:  
# Python:   >= 3.0
#
# ----------------------------------------------------------------------------

# Imports --------------------------------------------------------------------


import os
import shutil

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


def main() -> None:
    print(f"Name: {Bp.name()}")
    print(f"Name: {Bp.email()}")
    print(f"Name: {Bp.organisation()}")
    print(f"Name: {Bp.license()}")
            
    pass


if __name__ == "__main__":
    main()
