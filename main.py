# -*- coding: utf-8 -*-
from mvc.controller import Controller


class MainScript:
    def __init__(self):
        self.controll = Controller()

    def main(self):
        self.controll.run()


if __name__ == "__main__":
    main_script = MainScript()
    main_script.main()
