# GreenHouseMonitor Project

This project is designed to run on raspberry pi with installed thermometers on the GPIO pins. It is responsible for reporting temperatures from any of it's thermometers to a REST api hosted on django (see project, GreenHouseRest)

- read json config
- start loop
- read GPIO thermometers (as files)
- register new thermometer is not found in DB
  - mac address
  - thermometer id
