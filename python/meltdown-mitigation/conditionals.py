"""Functions to prevent a nuclear meltdown."""


def is_criticality_balanced(temperature, neutrons_emitted):
    is_balanced = temperature < 800 and neutrons_emitted > 500 and (temperature * neutrons_emitted <500000)
    return is_balanced


def reactor_efficiency(voltage, current, theoretical_max_power):
    generated_power = voltage * current
    efficiency = (generated_power/theoretical_max_power) *100
    if efficiency >= 80:
        return 'green'
    if  60 <= efficiency < 80:
        return 'orange'
    if 30<= efficiency < 60:
        return 'red'
    return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    if temperature *neutrons_produced_per_second < .9 * threshold:
        return 'LOW'
    if .9*threshold <= (temperature*neutrons_produced_per_second) <= 1.1 * threshold:
        return 'NORMAL'
    return 'DANGER'
