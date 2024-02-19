
def gencombos( target, column ):
    if column == 1:
        yield [target]
    else:
        # print(f'for i in range( 0, target//column+1 ):')
        # print(f'for i in range( 0, {target//column+1} ):')
        for i in range( 0, target//column+1 ):
            # print(f'for row in gencombos( target-i*column, column-1 ):')
            # print(f'for row in gencombos( {target-i*column}, {column-1} ):')
            for row in gencombos( target-i*column, column-1 ):
                yield row+[i]

for row in gencombos( 7, 3 ):
    print(row)
