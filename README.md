# femm-opt #

An example of parametric optimization procedure applied to a textbook electrostatics problem.

For associated article see: <a href="http://forkedbranch.eu/en/designing-curiosity-case-optimization-computer-aided-engineering/" target="_blank">Designing for Curiosity: A Case of Optimization in Computer Aided Engineering</a>

## Installing Dependencies ##

We will guide you through installing all the tools needed to run the optimization experiment on your (Windows) machine.

**Install Python 3**

Go to: <a href="https://www.python.org/downloads/windows/" target="_blank">https://www.python.org/downloads/windows/</a>

Download the latest version x86-64 version (3.5.1 at the time of writing). Double check you're downloading the 64-bit version. During installation choose 'Add Python 3.5 to PATH' - it makes things easier.

**Install Microsoft Visual C 2015 Runtime**

Go to: <a href="http://www.microsoft.com/en-us/download/details.aspx?id=48145" target="_blank">http://www.microsoft.com/en-us/download/details.aspx?id=48145</a>

Download the x64 version of the package. Install.

**Install Required Python Libraries**

Go to: <a href="http://www.lfd.uci.edu/~gohlke/pythonlibs" target="_blank">http://www.lfd.uci.edu/~gohlke/pythonlibs</a>

Download the following WHL files (note that version numbers may change).
 * NLopt-2.4.2-cp35-none-win_amd64.whl
 * matplotlib-1.5.1-cp35-none-win_amd64.whl

To install start a windows command line and use the Python pip tool (rep:

```
C:\Users\bartek>pip install Downloads\NLopt-2.4.2-cp35-none-win_amd64.whl
C:\Users\bartek>pip install Downloads\matplotlib-1.5.1-cp35-none-win_amd64.whl
C:\Users\bartek>pip install Pillow
```

**Install Femm (Finite Element Method Magnetics)**

Go to: <a href="http://www.femm.info/wiki/Download/" target="_blank">http://www.femm.info/wiki/Download/</a>

Download the 64-bit executable. Install.

**Install ffmpeg Encoder**

Go to: <a href="https://ffmpeg.zeranoe.com/builds/" target="_blank">https://ffmpeg.zeranoe.com/builds/</a>

Download the latest 64-bit statically (Static) linked version. Extract ffmpeg.exe (from /bin directory in the archive) to the `C:\ffmpeg` folder. 

## Running the experiment ##

Download zip of this repository. We will assume you extracted it in `c:\femm-opt-master`.
Edit `femm-opt-master\src\config.ini` to match locations of your executables. Set the output directory. An example configuration may look like:

```
[DEFAULT]
InputFolder = C:/femm-opt-master/input
OutputForlder = C:/Temp/Femmopt
FemmExe = C:/femm42/bin/femm.exe
FfmpegExe = C:/ffmpeg/ffmpeg.exe
FemmScrTempl = main.lua
FemmScrLib = calculate_field.lua
```

To run the experiment start windows command line and invoke the following:

```
C:\Users\bartek>cd c:\femm-opt-master\src
C:\femm-opt-master\src>python main.py
```

Go to your output folder and look for `OptimizationMovie.mp4`. you may also be interested in `_eval.dat` files.

## Using the code ##

Feel free to use the code in your research. We have included some comments in the source. We took some shortcuts though - treat it as a sketch. To explore the topic further - try inroducing a third design variable.

If you would like to apply optimization in your domain - get in touch with us by visiting [the forkedbranch website](http://forkedbranch.eu). 
