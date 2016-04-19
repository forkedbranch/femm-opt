# femmopt #

An example 

## Installing Dependencies ##

We will guide you through installing all the tools needed to run the optimization experiment on your (Windows) machine.

**Install Python 3**

Go to: <https://www.python.org/downloads/windows/>

Download the latest version x86-64 version (3.5.1 at the time of writing). Double check you're downloading the 64-bit version. During installation choose 'Add Python 3.5 to PATH' - it makes things easier.

**Install Microsoft Visual C 2015 Runtime**

Go to: <http://www.microsoft.com/en-us/download/details.aspx?id=48145>

Download the x64 version of the package. Install.

**Install Required Python Libraries**

Go to: <http://www.lfd.uci.edu/~gohlke/pythonlibs>

Download the following WHL files (note that version numbers may change).
 * NLopt-2.4.2-cp35-none-win_amd64.whl
 * matplotlib-1.5.1-cp35-none-win_amd64.whl
 * Pillow-3.2.0-cp35-cp35m-win_amd64.whl

To install start a windows command line and use the Python pip tool (rep:

`C:\Users\bartek>pip install Downloads\NLopt-2.4.2-cp35-none-win_amd64.whl`

**Install Femm (Finite Element Method Magnetics)**

Go to: <http://www.femm.info/wiki/Download/>

Download the 640bit executable. Install.

**Install ffmpeg Encoder**

Go to: <https://ffmpeg.zeranoe.com/builds/>

Download the latest 64-bit statically (Static) linked version. Extract ffmpeg.exe (from /bin directory in the archive) to the `C:\ffmpeg` folder. 

## Running the experiment##

Download zip of this repository