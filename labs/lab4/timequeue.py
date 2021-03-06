"""CSC148 Lab 4: Abstract Data Types

=== CSC148 Fall 2017 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===

This module runs timing experiments to determine how the time taken
to enqueue or dequeue grows as the queue size grows.

To complete this code, you will use the Timer class.  Here is a template
for how to use it.

Read through the docstring of the Timer class to understand how to use it.
"""
from myqueue import Queue
from timer import Timer
import matplotlib.pyplot as plt


def _profile_enqueue(queue_size: int, n: int) -> float:
    """Report the time taken to perform enqueue operations.

    Specifically, report the time taken to perform a single Queue.enqueue
    operation on <n> queues, each of size <queue_size>.
    (We do this on multiple queues to slow down the trials a little.)
    """

    queues = []
    for i in range(n):
        current = Queue()
        current._items = list(range(queue_size))
        queues.append(Queue())

    with Timer("Enqueue ----------------") as timer:
        for queue in queues:
            queue.enqueue("")

    return timer.interval

    # Experiment preparation: make a list containing <n> queues,
    # each of size <queue_size>. The elements you enqueue don't matter.
    # You can "cheat" here and set your queue's _items attribute
    # directly to a list of the appropriate size by writing something like
    #
    # queue._items = list(range(queue_size))
    #
    # to save a bit of time in setting up the experiment.

    # First, make a list containing <n> queues of size <queue_size>.

    # Second, for each of the <n> queues, enqueue a single item.
    # (Wrap the code in a Timer block to measure the total time taken.)


def _profile_dequeue(queue_size: int, n: int) -> float:
    """Report the time taken to perform dequeue operations.

    Specifically, report the time taken to perform a single Queue.dequeue
    operation on <n> queues, each of size <queue_size>.
    (We do this on multiple queues to slow down the trials a little.)
    """

    queues = []
    for i in range(n):
        current = Queue()
        current._items = list(range(queue_size))
        queues.append(Queue())

    with Timer("Dequeue ----------------") as timer:
        for queue in queues:
            queue.dequeue()
    return timer.interval
    # Experiment preparation: make a list containing <n> queues,
    # each of size <queue_size>.
    # You can "cheat" here and set your queue's _items attribute
    # directly to a list of the appropriate size by writing something like
    #
    # queue._items = list(range(queue_size))
    #
    # to save a bit of time in setting up the experiment.


def time_queue() -> None:
    """Profile enqueue and dequeue on various queue sizes."""
    # The different parameters for our timing runs.
    # Feel free to adjust this a little if it runs very slowly
    # on your computers.
    sizes = [500, 1000, 2000, 4000, 8000, 10000, 20000, 40000, 80000, 160000]
    trials = 100000

    en = []
    de = []

    for i in sizes:
        print(f"Enqueue with {i} size and {trials} queues")
        en.append(_profile_enqueue(i, trials))
    for i in sizes:
        print(f"Dequeue with {i} size and {trials} queues")
        de.append(_profile_dequeue(i, trials))

    plt.plot([str(i) for i in sizes], en)
    plt.plot([str(i) for i in sizes], de)
    plt.title(f"Running {trials} Trials")
    plt.ylabel("Time in Seconds")
    plt.xlabel("Queue Size")

    # plt.axes.set_ticks([str(i) for i in sizes])

    plt.show()


if __name__ == '__main__':
    time_queue()
