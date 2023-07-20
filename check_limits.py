def is_temperature_out_of_range(temperature):
    return temperature < 0 or temperature > 45


def is_soc_out_of_range(soc):
    return soc < 20 or soc > 80


def is_charge_rate_out_of_range(charge_rate):
    return charge_rate > 0.8


def battery_is_ok(temperature, soc, charge_rate):
    if is_temperature_out_of_range(temperature):
        print('Temperature is out of range!')
        return False
    elif is_soc_out_of_range(soc):
        print('State of Charge is out of range!')
        return False
    elif is_charge_rate_out_of_range(charge_rate):
        print('Charge rate is out of range!')
        return False

    return True


if __name__ == '__main__':
    # Positive test cases
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(0, 20, 0.8) is True

    # Negative test cases
    assert battery_is_ok(50, 85, 0) is False
    assert battery_is_ok(-5, 60, 0.5) is False
    assert battery_is_ok(30, 10, 0.9) is False
