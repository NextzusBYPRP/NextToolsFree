@echo off

::Restore Health your PC

echo Running SFC scan...
sfc /scannow

echo Running DISM Restore Health...
DISM /Online /Cleanup-Image /RestoreHealth

echo Running DISM CheckHealth...
DISM /Online /Cleanup-Image /CheckHealth

echo Running DISM ScanHealth...
DISM /Online /Cleanup-Image /ScanHealth

echo Running DISM StartComponentCleanup...
DISM /Online /Cleanup-Image /StartComponentCleanup

echo Running DISM StartComponentCleanup (ResetBase)...
DISM /Online /Cleanup-Image /StartComponentCleanup /ResetBase