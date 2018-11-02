from mobbage import bytes_to_human, num_to_human, seconds_to_human

def test_bytes_to_human():
    cases = (
        (1, "1.0B"),
        (999, "999.0B"),
        (1000, "1.0KB"),
        (999999, "1000.0KB"),
        (1000000, "1.0MB"),
        (999999999, "1000.0MB"),
        (1000000000, "1.0GB"),
        (999999999999, "1000.0GB"),
        (1000000000000, "1.0TB"),
        (999999999999999, "1000.0TB"),
        (1000000000000000, "1.0PB"),
        (999999999999988888, "1000.0PB"),
        (1000000000000000000, "1.0EB"),
        (999999999999988888888, "1000.0EB"),
        (1000000000000000000000, "1.0ZB"),
        (999999999999988888888888, "1000.0ZB"),
        (1000000000000000000000000, "1.0YB"),
        (2530000000000000000000000, "2.5YB"),
        (1000000000000000000000000000, "1000.0YB"),
        (1000000000000000000000000000000, "1000000.0YB"),
    )
    for (arg, exp) in cases:
        assert bytes_to_human(arg) == exp

def test_num_to_human():
    cases = (
        (1, 1),
        (999, 999),
        (1000, "1.00K"),
        (999999, "1000.00K"),
        (1000000, "1.00M"),
        (999999999, "1000.00M"),
        (1000000000, "1.00B"),
        (999999999999, "1000.00B"),
        (1000000000000, "1.00T"),
        (999999999999999, "1000.00T"),
        (1000000000000000, "1000.00T"),
    )
    for (arg, exp) in cases:
        assert num_to_human(arg) == exp

def test_seconds_to_human():
    cases = (
        (1, "00:00:01"),
        (59, "00:00:59"),
        (61, "00:01:01"),
        (3599, "00:59:59"),
        (3601, "01:00:01"),
    )
    for (arg, exp) in cases:
        assert seconds_to_human(arg) == exp
