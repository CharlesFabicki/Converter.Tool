from tkinter import *


class UnitConverter:
    def __init__(self):
        self.window = Tk()
        self.window.title("Converter")
        self.window.minsize(width=250, height=300)
        self.window.config(pady=20, padx=20)
        self.radio_variable = IntVar()
        self.radio_value = 0

        self.unit_entry = Entry(width=10)
        self.unit_entry.grid(row=0, column=1)

        self.unit_label = Label(text="from")
        self.unit_label.grid(row=0, column=2)

        self.is_equal = Label(text="is equal")
        self.is_equal.grid(row=1, column=0)

        self.converted_unit = Label(text="0")
        self.converted_unit.grid(row=1, column=1)

        self.convert_to = Label(text="to")
        self.convert_to.grid(row=1, column=2)

        self.calculate_button = Button(text="Calculate", command=self.change_conversion)
        self.calculate_button.grid(row=2, column=1)

        self.conversion_options = [
            ("Kilometers to Miles", "km", "miles", self.km_to_miles),
            ("Miles to Kilometers", "miles", "km", self.miles_to_km),
            ("Kilograms to Pounds", "kg", "lb", self.kg_to_lb),
            ("Pounds to Kilograms", "lb", "kg", self.lb_to_kg),
            ("Fahrenheit to Celsius", "°F", "°C", self.fahrenheit_to_celsius),
            ("Celsius to Fahrenheit", "°C", "°F", self.celsius_to_fahrenheit),
            ("Inches to Centimeters", "inches", "cm", self.inches_to_cm),
            ("Centimeters to Inches", "cm", "inches", self.cm_to_inches),
            ("Feet to Meters", "feet", "meters", self.feet_to_meters),
            ("Meters to Feet", "meters", "feet", self.meters_to_feet)
        ]

        for i, (text, from_unit, to_unit, func) in enumerate(self.conversion_options, start=3):
            Radiobutton(text=text, value=i, variable=self.radio_variable, command=self.change_conversion).grid(row=i,
                                                                                                               column=1)

    def change_conversion(self):
        self.radio_value = self.radio_variable.get()
        if 2 < self.radio_value < len(self.conversion_options) + 3:
            _, from_unit, to_unit, func = self.conversion_options[self.radio_value - 3]
            self.unit_label.config(text=from_unit)
            self.convert_to.config(text=to_unit)
            self.calculate_button.config(command=func)

    def km_to_miles(self):
        input_value = float(self.unit_entry.get())
        miles = input_value * 0.621371
        self.converted_unit.config(text=round(miles, 2))

    def miles_to_km(self):
        input_value = float(self.unit_entry.get())
        km = input_value * 1.609
        self.converted_unit.config(text=round(km, 2))

    def kg_to_lb(self):
        input_value = float(self.unit_entry.get())
        lb = input_value * 2.20462
        self.converted_unit.config(text=round(lb, 2))

    def lb_to_kg(self):
        input_value = float(self.unit_entry.get())
        kg = input_value * 0.453592
        self.converted_unit.config(text=round(kg, 2))

    def fahrenheit_to_celsius(self):
        input_value = float(self.unit_entry.get())
        celsius = (input_value - 32) * 5 / 9
        self.converted_unit.config(text=round(celsius, 2))

    def celsius_to_fahrenheit(self):
        input_value = float(self.unit_entry.get())
        fahrenheit = (input_value * 9 / 5) + 32
        self.converted_unit.config(text=round(fahrenheit, 2))

    def inches_to_cm(self):
        input_value = float(self.unit_entry.get())
        cm = input_value * 2.54
        self.converted_unit.config(text=round(cm, 2))

    def cm_to_inches(self):
        input_value = float(self.unit_entry.get())
        inches = input_value / 2.54
        self.converted_unit.config(text=round(inches, 2))

    def feet_to_meters(self):
        input_value = float(self.unit_entry.get())
        meters = input_value * 0.3048
        self.converted_unit.config(text=round(meters, 2))

    def meters_to_feet(self):
        input_value = float(self.unit_entry.get())
        feet = input_value / 0.3048
        self.converted_unit.config(text=round(feet, 2))


unit_converter = UnitConverter()
unit_converter.window.mainloop()

