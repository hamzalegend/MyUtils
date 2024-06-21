@REM USAGE::/ hqemuCreateVM.bat {name} {Size in GB} {.iso Path}

echo %1.img
md %1
cd %1
qemu-img.exe create -f qcow2 %1.img %2G


qemu-system-x86_64.exe -cdrom %3 -boot menu=on -drive file=%1.img -m 2G