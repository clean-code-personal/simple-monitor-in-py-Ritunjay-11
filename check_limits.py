def out_of_range(value, min_val, max_val, parameter_name):
    if value < min_val or value > max_val:
        print(f'{parameter_name} is out of range!')
        return True
    return False


def battery_is_ok(temperature, soc, charge_rate):
    if is_parameter_out_of_range(temperature, 0, 45, 'Temperature') \
            or is_parameter_out_of_range(soc, 20, 80, 'State of Charge') \
            or is_parameter_out_of_range(charge_rate, 0, 0.8, 'Charge rate'):
        return False

    return True


if __name__ == '__main__':
    # Test cases
    assert battery_is_ok(25, 70, 0.7) is True
    assert battery_is_ok(0, 20, 0.8) is True
    assert battery_is_ok(50, 85, 0) is False
    assert battery_is_ok(-5, 60, 0.5) is False
    assert battery_is_ok(30, 10, 0.9) is False
