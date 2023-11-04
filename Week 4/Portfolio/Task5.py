#5. Write and test a function that converts a temperature measured in degrees centigrade into the equivalent in fahrenheit, and another that does the reverse conversion.
# Test both functions. (Google will find you the formulae).

def centIntoFahr(cent):
    """Converts temperature from centigrade into fahrenheit."""
    fahr = (cent * 1.8) + 32
    print(cent, "degreees centigrade is", fahr, "degrees in fahrenheit")

centIntoFahr(22)


def fahrIntoCent(fahr):
    """Converts temperature from fahrenheit into centigrade."""
    cent = int(fahr // 1.8) - 32
    print(fahr, "degrees fahrenheit is,", cent, "degrees in centigrade")

fahrIntoCent(60)