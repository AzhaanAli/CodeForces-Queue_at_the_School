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

# Sadly I think no matter what, we have to iterate, therefore code will be linear time.
# Do a for loop that goes either until the entire queue is iterated though, or until swaps decrement to 0.
# Whenever we find a boy followed by a girl, cut him out and place him one index ahead.

data = input().split(' ')
queue = input()

queueLength = int(data[0])
swaps = int(data[1])

for i in range(0, queueLength):
    if swaps == 0:
        break
    if queue[i] == 'B' and queue[i + 1] == 'G':
        queue = queue[:i] + 'GB' + queue[i + 2:]
        swaps -= 1

print(queue)