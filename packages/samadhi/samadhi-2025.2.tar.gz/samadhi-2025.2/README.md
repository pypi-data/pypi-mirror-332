# Samadhi EEG / LSL

_Samadhi EEG_ is a project to build a Python/Qt/OpenGL based application
for visualising EEG and spectrum data in novel ways. Hooking onto an LSL stream, the software monitors
and displays EEG at realtime. The project has just started, implementation is not
mature yet and the content is mainly experimental. 

### Data Sources: LSL and Simulation

Data is received from an LSL stream which can be selected from a dropdown box on the left.
In addition there is a selftest which runs through single frequencies so you can check the behaviour
of spetrum displays.

### Display: Dancing Dots

**A wavy, rotating, jelly-fish like flower made up of single dots.** This is a spectrum display, visualising
the current value of the EEG frequency bands Delta, Theta, Alpha, Beta and Gamma.
![Image: Main page with EEG/PSD Tab](doc/main-window-dancing-dots.png)
The data from the spectrum analysis is averaged over rings of different lengths, arranged in concentric circles. The
hills and valleys of the sine waves add up or cancel out, depending on their frequency and the circumference
of the circle, creating a flower-like pattern with different colours and rotations.
This means the frequency of the spectrum band is represented in the symmetry of the dot display:

|                               Delta                               |                              Theta                               |                              Alpha                               |                              Beta                               |                              Gamma                               |
|:-----------------------------------------------------------------:|:----------------------------------------------------------------:|:----------------------------------------------------------------:|:---------------------------------------------------------------:|:----------------------------------------------------------------:|
| ![Image: Main page with EEG/PSD Tab](doc/dancing-dots-delta.png)  | ![Image: Main page with EEG/PSD Tab](doc/dancing-dots-theta.png) | ![Image: Main page with EEG/PSD Tab](doc/dancing-dots-alpha.png) | ![Image: Main page with EEG/PSD Tab](doc/dancing-dots-beta.png) | ![Image: Main page with EEG/PSD Tab](doc/dancing-dots-gamma.png) |

The actual display will be a superposition of these. The dancing dot flower display runs first inside
the window, a mouse click brings it to full-screen
(and back again). This display uses hardware acceleration (OpenGL).

### Display: Standard EEG and Spectrum

**Standard plots showing EEG and Spectrum.** The data is shown as received via LSL, a spectrum view (averaged power spectrum in log view),
a history of the last 10 minutes of spectrum, and the current spectrum as a bar plot.
![Image: Main page with EEG/PSD Tab](doc/main-window-eeg-psd.png)
The spectrum values are obtained from a Fourier Transform (power spectral density), divided by the spectrum
band width to prevent wider bands having more influence, and then normalised so the sum of all bands 
is 1.0.

### Installing and Running

The software is a python package on PyPi. To install and run, do:
`pip install samadhi`
`python3 -m samadhi`
To uninstall:
`pip uninstall samadhi`
(Non-Python installers for Linux and Windows will follow)