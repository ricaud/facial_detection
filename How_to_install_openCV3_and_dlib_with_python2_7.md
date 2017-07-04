### How to install openCV3 with python 2.7

install python2.7 using homebrew 
`brew install python`

you might have to uninstall openCV3 for some reason first
`brew uninstall opencv3`

install openCV3 using homebrew 
`brew install opencv3 --with-python`

link the packages or whatever (this is one big command)
`echo /usr/local/opt/opencv3/lib/python2.7/site-packages >> /usr/local/lib/python2.7/site-packages/opencv3.pth`

check to see if it worked (two seperate commands)
`python`
`import cv2`

if you don't get any errorrs then you know it worked


### How to install dlib HEAD (w/ python bindings) from github

These instructions assume you are on macOS, but basically the same on Linux.

Pre-reqs:
- Have Python 3 installed. On macOS, this could be installed from homebrew or even via standard 
  Python 3.6 downloaded installer from https://www.python.org/download. On Linux, just use your
  package manager.
- On macOS:
  - Install XCode from the Mac App Store (or install the XCode command line utils).
  - Have [homebrew](https://brew.sh/) installed
  - Install boost with this command: `brew install boost-python --with-python3 --without-python`
- On Linux:
  - Install boost. On Ubuntu, that's `sudo apt-get install libboost-all-dev`
- This assumes you don't have an nVidia GPU and don't have Cuda and cuDNN installed and don't want
  GPU acceleration (since none of the current Mac models support this).

Clone the code from github:

```bash
git clone https://github.com/davisking/dlib.git
```

Build the main dlib library:

```bash
cd dlib
mkdir build; cd build; cmake .. -DDLIB_USE_CUDA=0 -DUSE_AVX_INSTRUCTIONS=1; cmake --build .
```

Build and install the Python extensions:

```bash
cd ..
python3 setup.py install --yes USE_AVX_INSTRUCTIONS --no DLIB_USE_CUDA
```

At this point, you should be able to run `python3` and type `import dlib` successfully.