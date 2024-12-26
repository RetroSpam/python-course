def convert_to_hex(rgb):
    return '#{:02X}{:02X}{:02X}'.format(rgb[0], rgb[1], rgb[2])


print(convert_to_hex((255, 0, 0)))
print(convert_to_hex((0, 255, 0)))
print(convert_to_hex((0, 0, 255)))