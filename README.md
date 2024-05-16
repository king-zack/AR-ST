UCONN IAC Smart Thermostat Calculator Written by -- Zachary King; Max Nelson

This program is meant to automatically estimate the possible savings a manufacturing plant is capable of when replacing all thermostats with smart thermostats.

The primary data source for this project is from section 3.2.5 of https://energizect.com/sites/default/files/documents/Final%202022%20PSD%20FILED%20110122.pdf, which outlines the possible thermostat savings given various heating and cooling methods. It is also important to note that upgrading to smart thermostats give the company a rebate of $85 per unit (source: https://energizect.com/explore-solutions/demand-response-smart-devices/smart-thermostats)

Future implementation will involve calculating the carbon emissions saved from the smart thermostat upgrade. As of now, these values are calculated by hand based on the current output of this program.

How to Use:

Upon running the program, you will be presented with a handful of prompts. It is important that the replies to these prompts are integers or floating point values. Any invalid value will cause the program to return an error. The output of this calculater will be written to a csv file known as output.csv. If the program does not automatically create this file, you must create a file under the exact same name.

If bugs occur, contact: zachary.n.king@uconn.edu This program is written under the GNU-3 licence: Any modification to this code for commercial purposes or otherwise is permitted.
