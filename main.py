"""
DIRECTIONS:
During the break the schoolchildren, boys and girls, formed a queue of n people in the canteen.
Initially the children stood in the order they entered the canteen. However, after a while the boys started feeling
awkward for standing in front of the girls in the queue, and they started letting the girls move forward each second.

Let's describe the process more precisely. Let's say that the positions in the queue are sequentially numbered by
integers from 1 to n, at that the person in the position number 1 is served first. Then, if at time x a boy stands
on the i-th position and a girl stands on the (i + 1)-th position, then at time x + 1 the i-th position
will have a girl and the (i + 1)-th position will have a boy. The time is given in seconds.

You've got the initial position of the children, at the initial moment of time.
Determine the way the queue is going to look after t seconds.
"""

# Previously, I believed this could only be done in linear time to the size of the queue.
# Despite this, I think I've thought of a way to do it in linear time to the size of the amount of swaps.
# All boys are shifted to the right by the amount of swaps, except for those who are at the end of the line.
# (Let 'k' be the amount of swaps)
# Because of this, we can insert 'k' girls at the beginning of the line, and remove the last 'k' girls from the end.

data = input().split(' ')
queue = input()

queueLength = int(data[0])
swaps = int(data[1])

# Swaps cannot be greater than the amount of girls that there are.
# If there are fewer girls than swaps, set swaps to the amount of girls.
swaps = min(swaps, queue.count('G'))

# Reverse the string, so the replace method can be used to chop off the last k girls, then reverse it back.
queue = queue[:: -1].replace('G', '', swaps)[:: -1]

# Add as many girls as there are swaps to the front of the queue and the deed is done.
queue = 'G' * swaps + queue

print(queue)
