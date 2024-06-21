@REM USAGE::/ .bat  { Path } {.iso Path} { Memory }

qemu-system-x86_64.exe -cdrom %2 -boot menu=on -drive file=%1 -m %3G