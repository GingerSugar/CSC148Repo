"""CSC148 Exercise 1: Basic Object-Oriented Programming

=== CSC148 Fall 2017 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto

=== Module description ===
This module contains starter code for Exercise 1.
It contains two classes that work together:
- SuperDuperManager, which manages all the cars in the system
- Car, a class which represents a single car in the system

Your task is to design and implement the Car class, and then modify the
SuperDuperManager methods so that they make proper use of the Car class.

You may not modify the public interface of any of the SuperDuperManager methods.
We have marked the parts of the code you should change with TODOs, which you
should remove once you've completed them.

Notes:
  1. We'll talk more about private attributes on Friday's class.
     For now, treat them the same as any other instance attribute.
  2. You'll notice we use a trailing underscore for the parameter name
     "id_" in a few places. It is used to avoid conflicts with Python
     keywords. Here we want to have a parameter named "id", but that is
     already the name of a built-in function. So we call it "id_" instead.
"""
from typing import Dict, Optional, Tuple


class SuperDuperManager:
    """A class that keeps track of all cars in the Super Duper system.
    """
    # === Private Attributes ===
    # _cars:
    #   A map of unique string identifiers to the corresponding Car.
    #   For example, _cars['car1'] would be a Car object corresponding to
    #   the id 'car1'.
    _cars: Dict[str, 'Car']

    def __init__(self) -> None:
        """Initialize a new SuperDuperManager.

        There are no cars in the system when first created.
        """
        self._cars = {}

    def add_car(self, id_: str, fuel: int) -> None:
        """Add a new car to the system.

        The new car is identified by the string <id_>, and has initial amount
        of fuel <fuel>.

        Do nothing if there is already a car with the given id.

        Precondition: fuel >= 0.
        """
        # Check to make sure the identifier isn't already used.
        if id_ not in self._cars:
            self._cars[id_] = Car(0, 0, fuel)

    def move_car(self, id_: str, new_x: int, new_y: int) -> None:
        """Move the car with the given id.

        The car called <id_> should be moved to position (<new_x>, <new_y>).
        Do nothing if there is no car with the given id,
        or if the corresponding car does not have enough fuel.
        """
        if id_ in self._cars:
            car = self._cars[id_]
            fuel_req = abs(new_x - car.x) + abs(new_y - car.y)

            if fuel_req <= car.fuel:
                """calculated the amount of fuel needed to move"""
                car.x = new_x
                car.y = new_y
                car.fuel -= fuel_req

    def get_car_position(self, id_: str) -> Optional[Tuple[int, int]]:
        """Return the position of the car with the given id.

        Return a tuple of the (x, y) position of the car with id <id_>.
        Return None if there is no car with the given id.
        """
        if id_ in self._cars:
            car = self._cars[id_]
            return car.x, car.y
        else:
            return None

    def get_car_fuel(self, id_: str) -> Optional[int]:
        """Return the amount of fuel of the car with the given id.

        Return None if there is no car with the given id.
        """
        if id_ in self._cars:
            return self._cars[id_].fuel
        else:
            return None

    def dispatch(self, x: int, y: int) -> None:
        """Move a car to the given location.

        Choose a car to move based on the following criteria:
        (1) Only consider cars that *can* move to the location.
            (Ignore ones that don't have enough fuel.)
        (2) After (1), choose the car that would move the *least* distance to
            get to the location.
        (3) If there is a tie in (2), pick the car whose id comes first
            alphabetically. Use < and/or > to compare the strings.
        (4) If no cars can move to the given location, do nothing.
        """
        w_id: str
        w_req: int = -1

        for id_, car in self._cars.items():
            req = abs(x - car.x) + abs(y - car.y)
            if req <= car.fuel:
                continue
            else:
                if w_req == -1:
                    w_id = id_
                    w_req = req
                elif req < w_req:
                    w_id = id_
                    w_req = req
                elif req == w_req:
                    w_id = id_ if id_ < w_id else w_id

        if w_req != -1:
            self.move_car(w_id, x, y)


class Car:
    """A car in the Super system.

    === Public attributes ===
    x: the x-coordinate of this car's position
    y: the y-coordinate of this car's position
    fuel: the amount of fuel remaining this car has remaining

    === Representation invariants ===
    fuel >= 0
    """
    x: int
    y: int
    fuel: int

    def __init__(self, x: int, y: int, fuel: int):
        """Initializes a car

        === Attributes ===
        x: the x coordinate of the vehicle
        y: the y coordinate of the vehicle
        fuel: the amount of fuel the car is initialized with
        """
        self.x = x
        self.y = y
        self.fuel = fuel


if __name__ == '__main__':
    # Run python_ta to ensure this module passes all checks for
    # code inconsistencies and forbidden Python features.
    # Useful for debugging!
    import python_ta

    python_ta.check_all()
