#/usr/bin/python3

from time import sleep

from Devices import Relay, HTSensor, PinAssignments
from Meat import Meat


def lock(device) -> None:
    return


def release_lock(device) -> None:
    return


def setup_devices() -> dict:
    ht_pin_1= PinAssignments.get('HT1')
    relay_pin_1 = PinAssignments.get('RELAY1')

    HT = HTSensor(ht_pin_1)
    R1 = Relay(relay_pin_1)

    return {'HT1': HT, 'RELAY1': R1}


def check_temp(temp, meat) -> list:
    if temp > meat.t_high:
        return ['COMP_ON', 'LAMP_OFF']

    if temp < meat.t_low:
        return ['COMP_OFF', 'LAMP_ON']

    return ['COMP_OFF', 'LAMP_OFF']


def check_hum(hum, meat) -> list:

    if hum > meat.h_high:
        return ['FAN_ON', 'HUM_OFF']

    if hum < meat.h_low:
        return ['FAN_OFF','HUM_ON']

    return ['FAN_OFF', 'HUM_OFF']


def check_env(temp, hum, meat):
    temp_cmds = check_temp(temp, meat)
    hum_cmds = check_hum(hum, meat)
    return temp_cmds + hum_cmds

