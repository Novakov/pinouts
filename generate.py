from typing import NamedTuple, List

class Pin(NamedTuple):
    number: int
    name: str
    function: str = ""

def build_side_table(side: List[Pin]):
    result = []
    for i in range(0, len(side), 2):
        left = side[i + 1]
        right = side[i]

        result.append([
            left.function,
            left.name,
            left.number,
            right.number,
            right.name,
            right.function
        ])

    return result


def main():
    left = sorted([
        Pin(number=2, name='GND', function=''),
        Pin(number=4, name='GND', function=''),
        Pin(number=6, name='CLK', function=''),
        Pin(number=8, name='PWREN', function=''),
        Pin(number=10, name='DD6', function=''),
        Pin(number=12, name='VIO', function=''),
        Pin(number=14, name='DD3', function='CTS'),
        Pin(number=16, name='DD1', function='RXD'),
        Pin(number=18, name='CD7', function=''),
        Pin(number=20, name='CD5', function=''),
        Pin(number=22, name='VIO', function=''),
        Pin(number=24, name='CD2', function='RTS'),
        Pin(number=26, name='CD0', function='TXD'),

        Pin(number=1, name='VBUS', function=''),
        Pin(number=3, name='VCC', function=''),
        Pin(number=5, name='CS', function=''),
        Pin(number=7, name='DATA', function=''),
        Pin(number=9, name='DD7', function=''),
        Pin(number=11, name='DD5', function=''),
        Pin(number=13, name='DD4', function='DTR'),
        Pin(number=15, name='DD2', function='RTS'),
        Pin(number=17, name='DD0', function='TXD'),
        Pin(number=19, name='CD6', function=''),
        Pin(number=21, name='CD4', function='DTR'),
        Pin(number=23, name='CD3', function='CTS'),
        Pin(number=25, name='CD1', function='RXD'),
    ], key=lambda x: x.number)


    right = sorted([
        Pin(number=2, name='GND', function=''),
        Pin(number=4, name='GND', function=''),
        Pin(number=6, name='GND', function=''),
        Pin(number=8, name='RESET#', function=''),
        Pin(number=10, name='AD1', function='RXD'),
        Pin(number=12, name='AD3', function='CTS'),
        Pin(number=14, name='AD4', function='DTR'),
        Pin(number=16, name='AD6', function=''),
        Pin(number=18, name='BD0', function='TXD'),
        Pin(number=20, name='BD2', function='RTS'),
        Pin(number=22, name='BD4', function='DTR'),
        Pin(number=24, name='BD5', function=''),
        Pin(number=26, name='BD7', function=''),
        Pin(number=1, name='V3V3', function=''),
        Pin(number=3, name='V3V3', function=''),
        Pin(number=5, name='V3V3', function=''),
        Pin(number=7, name='AD0', function='TXD'),
        Pin(number=9, name='AD2', function='RTS'),
        Pin(number=11, name='VIO', function=''),
        Pin(number=13, name='AD5', function=''),
        Pin(number=15, name='AD7', function=''),
        Pin(number=17, name='BD1', function='RXD'),
        Pin(number=19, name='BD3', function='CTS'),
        Pin(number=21, name='VIO', function=''),
        Pin(number=23, name='BD6', function=''),
        Pin(number=25, name='SUSPEND', function=''),
    ], key=lambda x: x.number)

    left_tbl = build_side_table(left)
    right_tbl = build_side_table(right)

    table = []

    for (a, b) in zip(left_tbl, right_tbl):
        table.append([*a, '', *b])

    print('<table>')
    for row in table:
        print('    <tr>')
        for cell in row:
            print(f'        <td>{cell}</td>')
        print('    </tr>')
    print('</table>')


main()