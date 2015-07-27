import random
import sys
from collections import defaultdict

def test_monty(num_doors, num_iters):
    result_dict = defaultdict(int)
    for i in xrange(num_iters):
        doors = range(1, num_doors+1)
        winner = random.randint(1, num_doors)
        choice = random.randint(1, num_doors)
        doors.remove(choice)
        if winner != choice:
            switch = winner
        else:
            switch = doors[random.randint(0, len(doors)-1)] 
        if switch == winner:
            result_dict['switch_win'] += 1
        else:
            result_dict['switch_loss'] += 1
        if choice == winner:
            result_dict['stick_win'] += 1
        else:
            result_dict['stick_loss'] += 1
    return result_dict


def main(argv=sys.argv):
    try:
        doors = int(argv[1])
        iterations = int(argv[2])
        print doors, iterations
    except Exception as e:
        doors, iterations = 3, 10000
        print 'Defaulting to 3 doors and 10000 iterations'        
        print 'Usage: python monty_hall.py <# of doors> <# of iterations>'
    result = test_monty(doors, iterations)
    print result
    print 'Wins while switching: {}'.format(result['switch_win'])
    print 'Wins while sticking: {}'.format(result['stick_win'])
    print 'Win Percentage:\nSwitch: {} \nStick: {}'.format(result['switch_win']*100.0/float(iterations), result['stick_win']*100.0/float(iterations))

if __name__ == "__main__":
    sys.exit(main())

