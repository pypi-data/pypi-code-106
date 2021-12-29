import sys

import plico_motor
from guietta import Gui, _, G


class Runner(object):

    def __init__(self):
        self.motor = None

    def _setUp(self, host='localhost', port=7200, axis=1):

        def moveby(gui):
            nsteps = int(gui.nstepsby)
            if self.motor:
                self.motor.move_by(nsteps)

        def moveto(gui):
            nsteps = int(gui.nstepsto)
            if self.motor:
                self.motor.move_to(nsteps)

        def getstatus(gui):
            try:
                if self.motor:
                    gui.pos = self.motor.position()
                    gui.status = self.motor.status().as_dict()
                else:
                    gui.pos = '---'
                    gui.status = 'Not connected'
            except Exception as e:
                gui.pos = str(e)
                gui.status = 'Not connected'

        def connect(gui):
            host = gui.host
            port = gui.port
            axis = gui.axis
            self.motor = plico_motor.motor(host, int(port), int(axis))

        connection_gui = Gui(
             [ 'Host:', '__host__' ],
             [ 'Port:', '__port__' ],
             [ 'Axis:', '__axis__' ],
             [ ['Connect'] ]
        )
        connection_gui.host = host
        connection_gui.port = port
        connection_gui.axis = axis
        connection_gui.Connect = connect

        control_gui = Gui(
             [  'Pos:'     , 'pos'       , _       ],
             [ ['Move to'] , '__nstepsto__', 'steps' ],
             [ ['Move by'] , '__nstepsby__', 'steps' ],
             [ 'Status:'   , 'status'    , _       ]
        )
        control_gui.Moveby = moveby
        control_gui.Moveto = moveto
        control_gui.timer_start(getstatus, 0.1)

        self.gui = Gui(
             [ G('Connection') ],
             [ G('Motor') ]
        )

        self.gui.Connection = connection_gui
        self.gui.Motor = control_gui


    def run(self, argv):
        self._setUp(*argv)
        self.gui.run()

    def terminate(self, signal, frame):
        pass


if __name__ == '__main__':
    runner = Runner()
    sys.exit(runner.run(sys.argv[1:]))

