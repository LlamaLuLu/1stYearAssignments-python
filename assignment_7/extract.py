# To extract useful data from raw data stream obtained from sensor.
# Lulama Lingela
# 3 April 2023

def get_block(data):
    """Extracts sub-string starting with ‘BEGIN’ and ending with ‘END’."""
    start = data.find("BEGIN")
    end = data.find("END") + 3
    return data[start: end]


def location(block):
    """Returns location component in title case."""
    start_cut = block.find("BEGIN") + 6
    block = block[start_cut:]
    start = block.find("END") - 2
    end = block.find(" ")
    place = block[start:end:-1].title()
    return place


def pressure(block):
    """Returns pressure component as real number value."""
    start = block.find("_") + 1
    end = block.find(":")
    return float(block[start:end])


def temperature(block):
    """Returns temp. component as real number value."""
    start = block.find(" ") + 1
    end = block.find("_")
    return eval(block[start:end])


def y_coordinate(block):
    """Returns y-coordinate component as str."""
    start_cut = block.find(",") + 1
    block = block[start_cut:]
    end = block.find(" ")
    return block[:end]


def x_coordinate(block):
    """Returns x-coordinate component as str."""
    start = block.find(":") + 1
    end = block.find(",")
    return block[start:end]


def main():
    data = input('Enter the raw data:\n')
    block = get_block(data)
    print('Site information:')
    print('Location:', location(block))
    print('Coordinates:', y_coordinate(block), x_coordinate(block))
    print('Temperature: {:.2f} C'.format(temperature(block)))
    print('Pressure: {:.2f} hPa'.format(pressure(block)))


if __name__ == '__main__':
    main()
