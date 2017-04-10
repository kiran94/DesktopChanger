
import subprocess
from sys import platform

# Service for desktop operations
class desktopService:
    
    # Changes the Desktop wallpaper to the given filename for the appropiate operating system.
    def changeDesktop(self, filename):
        if (platform == "darwin"):
            self.__setMacBackground(filename)
        elif (platform == "win32"):
            self.__setWindowsBackground(filename)
    
    # Changes the Mac OS wallpaper to the given filename.
    def __setMacBackground(self, filename):
        MacSCRIPT = """/usr/bin/osascript<<END
        tell application "Finder"
        set desktop picture to POSIX file "%s"
        end tell"""

        subprocess.Popen(MacSCRIPT%filename, shell=True)
        
    # Changes the Windows OS wallpaper to the given filename. 
    def __setWindowsBackground(self, filename):
        raise NotImplementedError("Windows not implemented.")