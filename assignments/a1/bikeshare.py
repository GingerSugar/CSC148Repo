"""Assignment 1 - Bike-share objects

=== CSC148 Fall 2017 ===
Diane Horton and David Liu
Department of Computer Science,
University of Toronto


=== Module Description ===

This file contains the Station and Ride classes, which store the data for the
objects in this simulation.

There is also an abstract Drawable class that is the superclass for both
Station and Ride. It enables the simulation to visualize these objects in
a graphical window.
"""
from datetime import datetime
from typing import Tuple

# Sprite files
STATION_SPRITE = 'stationsprite.png'
RIDE_SPRITE = 'bikesprite.png'


class Drawable:
    """A base class for objects that the graphical renderer can be drawn.

    === Public Attributes ===
    sprite:
        The filename of the image to be drawn for this object.
    """
    sprite: str

    def __init__(self, sprite_file: str) -> None:
        """Initialize this drawable object with the given sprite file.
        """
        self.sprite = sprite_file

    def get_position(self, time: datetime) -> Tuple[float, float]:
        """Return the (long, lat) position of this object at the given time.
        """
        raise NotImplementedError


class Station(Drawable):
    """A Bixi station.

    === Public Attributes ===
    capacity:
        the total number of bikes the station can store
    location:
        the location of the station in long/lat coordinates
        **UPDATED**: make sure the first coordinate is the longitude,
        and the second coordinate is the latitude.
    name: str
        name of the station
    num_bikes: int
        current number of bikes at the station
    bikes_started_here:
        the number of bikes that started here during the simulation
    bikes_ended_here:
        the number of bikes that ended here during the simulation
    low_availability:
        the amount of time in seconds spent with at most 5 bikes in the station
    low_unoccupied:
        the amount of time in seconds spent with at most 5 unoccupied spots

    === Representation Invariants ===
    - 0 <= num_bikes <= capacity
    - bikes_started_here, bikes_ended_here, low_availability, low_unoccupied >= 0
    """
    name: str
    location: Tuple[float, float]
    capacity: int
    num_bikes: int

    bikes_started_here: int
    bikes_ended_here: int
    low_availability: int
    low_unoccupied: int

    def __init__(self, pos: Tuple[float, float], cap: int,
                 num_bikes: int, name: str) -> None:
        """Initialize a new station.

        Precondition: 0 <= num_bikes <= cap
        """
        super().__init__(STATION_SPRITE)
        self.location = pos
        self.capacity = cap
        self.num_bikes = num_bikes
        self.name = name
        self.bikes_started_here = 0
        self.bikes_ended_here = 0
        self.low_availability = 0
        self.low_unoccupied = 0

    def get_position(self, time: datetime) -> Tuple[float, float]:
        """Return the (long, lat) position of this station for the given time.

        Note that the station's location does *not* change over time.
        The <time> parameter is included only because we should not change
        the header of an overridden method.
        """
        return self.location


class Ride(Drawable):
    """A ride using a Bixi bike.

    === Attributes ===
    start:
        the station where this ride starts
    end:
        the station where this ride ends
    start_time:
        the time this ride starts
    end_time:
        the time this ride ends

    === Representation Invariants ===
    - start_time < end_time
    """
    start: Station
    end: Station
    start_time: datetime
    end_time: datetime

    def __init__(self, start: Station, end: Station,
                 times: Tuple[datetime, datetime]) -> None:
        """Initialize a ride object with the given start and end information.
        """
        super().__init__(RIDE_SPRITE)
        self.start, self.end = start, end
        self.start_time, self.end_time = times[0], times[1]

    def get_position(self, time: datetime) -> Tuple[float, float]:
        """Return the (long, lat) position of this ride for the given time.

        A ride travels in a straight line between its start and end stations
        at a constant speed.
        """
        pos_start = self.start.get_position(time)
        pos_end = self.end.get_position(time)

        ride_time = (self.end_time - self.start_time).total_seconds()
        pass_time = (time - self.start_time).total_seconds()

        new_x = (pos_end[0] - pos_start[0]) * (pass_time / ride_time) + pos_start[0]
        new_y = (pos_end[1] - pos_start[1]) * (pass_time / ride_time) + pos_start[1]

        return pos_start if time < self.start_time else (pos_end if time > self.end_time else (new_x, new_y))


if __name__ == '__main__':
    import python_ta

    python_ta.check_all(config={
        'allowed-import-modules': [
            'doctest', 'python_ta', 'typing',
            'datetime'
        ],
        'max-attributes': 15
    })
