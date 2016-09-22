description = 'Lakeshore 336 controller in ESSIIP lab.'


class PvGenerator(object):
    def __init__(self, prefix=''):
        self._prefix = prefix

    def __call__(self, name):
        return self._prefix + name


pvs = PvGenerator('LabS-ESSIIP:SEE-TCtrl-1:')

devices = dict(
    T=device('devices.epics.EpicsWindowTimeoutDevice',
             description='Input channel B.',
             readpv=pvs('KRDG1'),
             writepv=pvs('SETP_S2'),
             window=60.0,
             timeout=None,
             ),


    heater=device('devices.epics.EpicsDigitalMoveable',
                  description='Heater setting for output 2.',
                  readpv=pvs('RANGE2'),
                  writepv=pvs('RANGE2_S2'),
                  lowlevel=True,
                  ),
    T_p=device('device.epics.EpicsAnalogMoveable',
               description='P-parameter of control loop channel B.',
               readpv=pvs('P2'),
               writepv=pvs('P_S2'),
               lowlevel=True,
               ),

    T_i=device('device.epics.EpicsAnalogMoveable',
               description='I-parameter of control loop channel B.',
               readpv=pvs('I2'),
               writepv=pvs('I_S2'),
               lowlevel=True,
               ),
    T_d=device('device.epics.EpicsAnalogMoveable',
               description='D-parameter of control loop channel B.',
               readpv=pvs('D2'),
               writepv=pvs('D_S2'),
               lowlevel=True,
               ),
)
