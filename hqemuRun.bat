@REM USAGE::/ hqemurun.bat {DiskPath} {Memory in GB}

qemu-system-x86_64.exe -drive file=%1 -m %2G