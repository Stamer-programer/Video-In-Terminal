Small Video player in terminal
The bad apple video(just download it):
[![Watch the video](Examples/ThumbNail.png)](Examples/Example.mp4)

# How To install 

```console
git clone https://github.com/Stamer-programer/Video-In-Terminal.git
```

## Make your own venv

```console
python -m venv V
```

## Cd into Folder
```console
cd V
```
## Then install some dependecies
### Arch/Arch-based

```console
sudo pacman -S atlas
sudo pacman -S gcc-fortran
sudo pacman -S gcc
sudo pacman -S python
sudo pacman -S pkgconf
sudo pacman -S portaudio
sudo pacman -S alsa-lib

```
### Fedora/rhel:
```console
sudo dnf install atlas-devel
sudo dnf install gcc-gfortran
sudo dnf install gcc-c++
sudo dnf install python3-devel
sudo dnf install pkg-config
sudo dnf install portaudio-devel
sudo dnf install alsa-lib-devel
```
### Ubuntu/Debian
```console
sudo apt install libatlas-base-dev
sudo apt install gfortran
sudo apt install g++
sudo apt install python3-dev
sudo apt install pkg-config
sudo apt install portaudio19-dev
sudo apt install libasound2-dev

```
### OpenSUSE
```console
sudo zypper install atlas-devel
sudo zypper install gcc-fortran
sudo zypper install gcc-c++
sudo zypper install python3-devel
sudo zypper install pkg-config
sudo zypper install portaudio-devel
sudo zypper install alsa-lib-devel
```

### Alpine linux

```console
sudo apk add atlas-dev
sudo apk add gfortran
sudo apk add g++
sudo apk add python3-dev
sudo apk add pkgconf
sudo apk add portaudio-dev
sudo apk add alsa-lib-dev

```

## Then install libraries using pip
```console
./bin/pip install -r ../Video-In-Terminal/req.txt
```
## Copy Some Files

```console
cp -r -p ../Video-In-Terminal/Examples/ .
cp ../Video-In-Terminal/main.py .
```
