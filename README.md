<p align="center">
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-1-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->
<img alt="A small robot for captioning your performances" src="https://github.com/Elleo/scribe/blob/main/logo.png?raw=true"  width=256 height=auto)
</p>

# Scribe
Scribe is a device for automatically captioning live performances. Both the hardware and software are open source.

# Hardware
The device can be built for approximately £150, making it suitable for small theatres and individual artists on limited budgets.

## Components
 * [Raspberry Pi 4 (or later) with at least 2GB of RAM](https://thepihut.com/products/raspberry-pi-4-model-b?variant=20064052674622) - £45.50
 * [SD card](https://thepihut.com/products/noobs-preinstalled-sd-card) - £7
 * [Ada-Fruit 32x64 RGB Matrix](https://thepihut.com/products/adafruit-64x32-rgb-led-matrix-4mm-pitch) - £40.70
   - These are available in different element spacing sizes (pitch). Smaller pitch sizes are more appropriate for viewing at close range, while higher pitch values are better viewed at a distance. A 4mm pitch gives a good middle ground for most venues.
 * [Ada-Fruit RGB Matrix Driver Bonnet](https://thepihut.com/products/adafruit-rgb-matrix-bonnet-for-raspberry-pi-ada3211) - £15.20
 * [Power supply](https://thepihut.com/products/neopixel-power-brick-5v-5a-25w) - £23
   - [C7 lead](https://thepihut.com/products/figure-8-type-power-cable-2m-c7-uk) (if not included with power supply) - £1
 * [USB audio capture device](https://thepihut.com/products/mini-usb-microphone) - £5.20
 * [M3 x 12mm screws or hex screws](https://www.amazon.co.uk/12mm-Socket-Screw-Bolt-Head/dp/B084RFHZ2F) x 11 - £5.49 (pack of 20)
 * [M3 brass inserts](https://www.amazon.co.uk/sourcing-map-Knurled-Insert-Embedding/dp/B09MCWTGLZ) x 6 - £6.49 (pack of 50)
 * [DC extension cable](https://www.amazon.co.uk/dp/B0792HD7CC) - £4.99
   
  (You might be able to get screws and brass inserts cheaper by buying them individually from a local hardware store)
   
  All prices are including VAT, and were last updated in September 2022. Total cost: £154.57

## Case
 The case can be 3D printed using the STL files in [/case/stl](/case/stl). Select the appropriate case size based on your RGB matrix size and pitch. For each case size there is an STL for the complete case in one piece or if your print bed is not large enough to fit the whole case in one piece there is a version split into two parts.

# Software
The scribe software allows for multiple shows to be configured with individual settings. Performers can upload scripts to the device to guide the speech recognition system and provide for greatly increased accuracy. All speech recognition is done on the device itself and does not require any internet connection during perfomances.

# Logo
The logo was kindly designed by [Thomas Heasman-Hunt](https://twitter.com/smolrobots)

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Elleo"><img src="https://avatars.githubusercontent.com/u/59350?v=4?s=100" width="100px;" alt="Mike Sheldon"/><br /><sub><b>Mike Sheldon</b></sub></a><br /><a href="https://github.com/Elleo/scribe/commits?author=Elleo" title="Code">💻</a> <a href="#ideas-Elleo" title="Ideas, Planning, & Feedback">🤔</a> <a href="#infra-Elleo" title="Infrastructure (Hosting, Build-Tools, etc)">🚇</a> <a href="#maintenance-Elleo" title="Maintenance">🚧</a> <a href="#projectManagement-Elleo" title="Project Management">📆</a> <a href="#financial-Elleo" title="Financial">💵</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!