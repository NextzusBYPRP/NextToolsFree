@echo off
cls
echo Starting repair and maintenance tasks...

:: Restore default power plans
echo Restoring default power plans...
powercfg -restoredefaultschemes
echo Default power plans restored.

:: Re-establish the missing registry key
echo Attempting to re-establish the missing registry key...
reg add "HKLM\SYSTEM\CurrentControlSet\Control\MUI\StringCacheSettings" /f
reg add "HKLM\SYSTEM\CurrentControlSet\Control\MUI\StringCacheSettings" /v StringCacheGeneration /t REG_DWORD /d 0x38b /f
echo Registry key re-established.

exit
::Finished

