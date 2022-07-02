# simple-mrt-routing

A simple routing service for Singapore MRT

### Features

- Can suggest shortest route from start station to destination station

### Run project

```sh
python3 src/main.py
```

### Inputs

Input station code for the starting and destination station.

Sample Input:
```sh
Starting Station: NS1
Destination Station: CC2
```

Sample Output:
```sh
Travel from Jurong East to Bras Basah
Stations travelled: 16
Route: ( NS1 EW24 EW23 EW22 EW21 EW20 EW19 EW18 EW17 EW16 NE3 NE4 NE5 NE6 CC1 CC2 )

Change from NS line to EW line
Take EW line from Jurong East to Clementi
Take EW line from Clementi to Dover
Take EW line from Dover to Buona Vista
Take EW line from Buona Vista to Commonwealth
Take EW line from Commonwealth to Queenstown
Take EW line from Queenstown to Redhill
Take EW line from Redhill to Tiong Bahru
Take EW line from Tiong Bahru to Outram Park
Change from EW line to NE line
Take NE line from Outram Park to Chinatown
Take NE line from Chinatown to Clarke Quay
Take NE line from Clarke Quay to Dhoby Ghaut
Change from NE line to CC line
Take CC line from Dhoby Ghaut to Bras Basah
```