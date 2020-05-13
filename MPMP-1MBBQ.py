import numpy as np
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt


def main( test ) :
    solutions = []
    one_million = 1000000

    for first in range( 0, tests ) :
        for second in range( 0, tests ) :
            if first + second == 0 or first + second >= one_million : continue
            result = MPMP( first, second, one_million )
            value = result[1] if result[0] else result[0]
            if value :
                solutions.append( {
                        "days" : value,
                        "first" : first,
                        "second" : second
                    } )

    solutions.sort( key=lambda x: x["days"], reverse=True )

    return solutions

def MPMP( day_one, day_two, target ) :
    next_day = day_one + day_two
    last_day = day_two
    count = 2

    while next_day < target :
        count += 1
        next_day, last_day = ( next_day + last_day ), next_day
        if next_day == target : 
            return ( True, count )
    
    return ( False, count )


if __name__ == "__main__":
    tests = 5000

    solutions = main( tests )

    fig = plt.figure( f'MPMP: 1 Million Bank Balance Question({tests}x{tests})' )
    fig.suptitle( f'MPMP: 1 Million Bank Balance Question({tests}x{tests})' )
    ax = plt.axes(projection="3d")

    z = []
    x = []
    y = []

    for data in solutions :
        z.append( data["days"] )
        x.append( data["first"] )
        y.append( data["second"] )
# fig.canvas.set_window_title('Test')

    ax.set_xlabel("First Deposit")
    ax.set_ylabel("Second Deposit")
    ax.set_zlabel("Total Days")
    ax.scatter3D( x, y, z, c=z, cmap='hsv')

    best_days = solutions[0]["days"]
    best_first = solutions[0]["first"]
    best_second = solutions[0]["second"]
    ax.text( best_first+0.25, best_second+0.25, best_days+0.25, f'{best_days} Days, First Deposit: £{best_first}, Second Deposit: £{best_second}', color='red' )

    plt.show()
