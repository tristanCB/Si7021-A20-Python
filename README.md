# Simple function for the Si7021-A20 
## Description
A simple function which that uses smbus to get readings from the digital temperature and relative humidity sensor [Si7021-A20](https://www.silabs.com/documents/public/data-sheets/Si7021-A20.pdf).
This function is an adaptation of the following [blog post](https://www.silabs.com/documents/public/data-sheets/Si7021-A20.pdf).
This function was used to gather data from a single sensor connected to a Raspberry Pi.

## Requirements
```pip install smbus```

## Example use
```
import Si7021_A20

# Return a dictionary containing RH and Temp readings.
Si7021_A20.querySI(address=0x40) 
```

## Ensuring manufactured precision rating
To ensure that the precision specified by the manufacturer of ± 3% RH (max) at 0–80% RH was indeed met, a fix humidity was created according to ASTM standard E104 – 02 (2012) (standard practice for maintaining constant relative humidity by means of aqueous solutions).
1. 50ml of a salts listed in Table 1 were poured into a 500ml erlenmeyer flask.
2. A saturated soltion was created by adding just enough deionized water to fill it's void space. The mixture was stirred.
3. The RH sensor was placed inside the top portion of the flask.
4. The opening was sealed using parafilm.
5. Values were logged for the next 24 hours.
6. The difference in between the measured value and the corresponding ones listed in table 1 are callculated.

| t (°C) |Potassium acetate|  Magnesium chloride | Potassium carbonate  | Potassium sulfate |
|---|---|---|---|---|
|5| - | 33.6 ± 0.3|43.1 ± 0.5|98.5 ± 1.0|
|10| 23.4 ± 0.6|33.5 ± 0.3|43.1 ± 0.4|98.5 ± 1.0|
|15|23.4 ± 0.4|33.3 ± 0.3|43.2 ± 0.4|97.9 ± 0.7|
|20|23.1 ± 0.3|33.1 ± 0.2|43.2 ± 0.4|97.6 ± 0.6|
|25|22.5 ± 0.4|32.8 ± 0.2|43.2 ± 0.4|97.3 ± 0.5|
|30|21.6 ± 0.6|32.4 ± 0.2|43.2 ± 0.4|97.0 ± 0.4|

**Table 1:** Fixed humidity points for saturated aqueous solutions. Adaptation of table 2 from Greenspan and Lewis (1977).

## References
ASTM E104 – 02 (2012). __standard practice for maintaining constant relative humidity by means of aqueous solutions__.

Greenspan, Lewis. (1977). __Humidity Fixed Points of Binary Saturated Aqueous Solutions.__ Journal of Research of the National Bureau of Standards Section a: Physics and Chemistry, vol. 81a, no. 1, 1977, pp. 89–89., doi:10.6028/jres.081A.011.
