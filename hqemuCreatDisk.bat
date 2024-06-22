@REM USAGE::/ hqemuCreateVM.bat {path} {Size in GB}

qemu-img.exe create -f qcow2 %1 %2G