from avx.devices import Device

import requests


class Bridge(Device):

    def __init__(self, deviceID, avista_url, avista_power_device, **kwargs):
        super(Bridge, self).__init__(deviceID, **kwargs)
        self.avista_url = avista_url
        self.avista_power_device = avista_power_device

    def initialise(self):
        '''
        Called after avx system power-on; needs to tell avista system to power
        on.
        '''
        r = requests.post(
            self.avista_url,
            json={
                "procedure": "{}.power_on".format(self.avista_power_device)
            }
        )
        self.log.info('Sent power-on message to avista system (status code: {})'.format(r.status_code))

    def deinitialise(self):
        '''
        Called during avx system power-off; needs to tell avista system to power
        off.
        '''
        r = requests.post(
            self.avista_url,
            json={
                "procedure": "{}.power_off".format(self.avista_power_device)
            }
        )
        self.log.info('Sent power-off message to avista system (status code: {})'.format(r.status_code))
