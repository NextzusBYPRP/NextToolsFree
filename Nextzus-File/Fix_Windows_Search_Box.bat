@echo off
echo Fixing Windows Search Box...
echo.

:: Stop the search service
echo Stopping the search service...
net stop wsearch

:: Rename the Data folder
echo Renaming the Data folder...
ren %systemroot%\System32\Search\Data\Data %systemroot%\System32\Search\Data\Data.bak

:: Delete the registry keys for the search index
echo Deleting the registry keys for the search index...
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Search" /f
reg delete "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows Search\CrawlScopeManager" /f

:: Restart the search service
echo Restarting the search service...
net start wsearch

:: Rebuild the search index
echo Rebuilding the search index...
echo This may take a while. Please wait...
"C:\Program Files\Microsoft Office\Office16\SCANPST.EXE" /ioutlook.pst

:: Additional fix: Re-register Cortana app package
echo Re-registering Cortana app package...
powershell -Command "Get-AppXPackage -Name Microsoft.Windows.Cortana | Foreach {Add-AppxPackage -DisableDevelopmentMode -Register "$($_.InstallLocation)\AppXManifest.xml"}"

echo.
echo Windows Search Box has been fixed!
pause
