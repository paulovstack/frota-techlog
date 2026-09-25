# TechLog Solutions — Fleet Management System

A Python system for vehicle fleet management (trucks and forklifts), simulating the registration of each vehicle and the calculation of operating costs according to the specific characteristics of each type.

## Features

* Truck registration (including fuel consumption, distance traveled, and fuel price per liter)
* Forklift registration (including load capacity and battery level)
* Duplicate code validation during registration
* Automatic calculation of each vehicle's operating cost, with specific rules for each type
* Forklift battery status verification (Normal / Alert / Critical)
* Filtered reports: trucks only, forklifts only, complete fleet, or search by code
* Interactive terminal menu with visual feedback (colors and emojis)

## Concepts Practiced

This project was my way of deepening my knowledge of Object-Oriented Programming (OOP) in Python:

* **Inheritance**: `Truck` and `Forklift` inherit from `Vehicle`, reusing common attributes and behaviors (code, model, base cost) and implementing only what is specific to each type.
* **Method overriding**: each subclass implements its own version of `calculate_cost()`, following its own business rule — the truck considers distance and fuel consumption, while the forklift considers load capacity.
* **Consistent method signatures between subclasses**: initially, the truck's `calculate_cost()` method required additional parameters (`distance`, `fuel_price`) that the other classes did not. I refactored the code so these values are stored as object attributes (`self.distance`, `self.fuel_price`), keeping the method signature consistent across all classes — following the principle that a subclass should be able to be treated in the same way as its parent class.
* **Using `isinstance()`** to differentiate the behavior of each vehicle type within the same list (`fleet`), avoiding the need for separate lists for each type.
* **Encapsulation**: the forklift's battery level is a protected attribute (`_battery_level`), accessed through a method (`check_status()`) instead of being manipulated directly.

## How to Run

```bash
python main.py
```

The program opens a menu where you can register trucks, register forklifts, and view fleet cost reports.

## Technologies

* Python 3
* Standard libraries: `time`, `os`

## Next Steps

* Data persistence (saving the fleet to a file so registrations are not lost when the program is closed)
* More robust validation of numerical inputs (currently, the program may crash if the user enters text where a number is expected)
* Vehicle cost calculation history, instead of recalculating the cost with each query
