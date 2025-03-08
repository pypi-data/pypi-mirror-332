import subprocess
import dataclasses
import sys
import time
from subprocess import Popen
from tempfile import NamedTemporaryFile

import colorama
from colorama import Fore, Style
from wmi import WMI


#----------------------------------------CONSOLE----------------------------------------
_LOGO: str =\
r"""                                                   
 $$$$$$\  $$$$$$$\  $$$$$$$$\                                           $$\     
$$  __$$\ $$  __$$\ $$  _____|                                          $$ |    
$$ /  $$ |$$ |  $$ |$$ |    $$$$$$\   $$$$$$\  $$$$$$\$$$$\   $$$$$$\ $$$$$$\   
$$$$$$$$ |$$ |  $$ |$$$$$\ $$  __$$\ $$  __$$\ $$  _$$  _$$\  \____$$\\_$$  _|  
$$  __$$ |$$ |  $$ |$$  __|$$ /  $$ |$$ |  \__|$$ / $$ / $$ | $$$$$$$ | $$ |    
$$ |  $$ |$$ |  $$ |$$ |   $$ |  $$ |$$ |      $$ | $$ | $$ |$$  __$$ | $$ |$$\ 
$$ |  $$ |$$$$$$$  |$$ |   \$$$$$$  |$$ |      $$ | $$ | $$ |\$$$$$$$ | \$$$$  |
\__|  \__|\_______/ \__|    \______/ \__|      \__| \__| \__| \_______|  \____/  
"""


def green(text: str) -> str:
    return f"{Fore.GREEN}{text}{Style.RESET_ALL}"


def cls() -> None:
    subprocess.run("cls", shell=True)
    print(green(_LOGO))


#----------------------------------------SCRIPTS----------------------------------------
@dataclasses.dataclass
class UsbDisk:
    index: int
    name: str
    size: float

    def __lt__(self, other) -> bool:
        return self.index < other.index


def get_usb_disks() -> list[UsbDisk]:
    return sorted(
        [
            UsbDisk(
                disk.Index,
                disk.Caption,
                round(int(disk.Size) / 1024**3, 1)
            )
            for disk in WMI().Win32_DiskDrive()
            if "USB" in disk.Caption and disk.Size is not None
        ]
    )


def format_disk(disk: UsbDisk) -> Popen[str]:
    file: NamedTemporaryFile = NamedTemporaryFile("w", delete=False)
    file.write(
        f"""
        select disk {disk.index}
        clean
        create partition primary
        select partition 1
        active
        format fs=FAT32 quick
        assign
        """
    )
    file.close()
    return Popen(f"diskpart /s {file.name}", shell=True, text=True)


#----------------------------------------MAIN----------------------------------------
def main() -> None:
    colorama.init()

    cls()
    print(green("[*] Please select disks to flash (ex. 2-5):"))
    for disk in get_usb_disks():
        print(green(f"[{disk.index}] {disk.name} - {disk.size} Gb"))
    disks_raw: str = input(green("Select: "))
    indexes: tuple[int, ...]
    if disks_raw.isdigit():
        indexes = (int(disks_raw),)
    else:
        first, second = disks_raw.split("-")
        indexes = tuple(range(int(first), int(second) + 1))
    disks: list[UsbDisk] = [disk for disk in get_usb_disks() if disk.index in indexes]

    cls()
    print(green("[*] Selected USB disks:"))
    for disk in disks:
        print(green(f"[{disk.index}] {disk.name} - {disk.size} Gb"))
    print(green("Are you sure? Press any key to continue..."))
    input()

    cls()
    print(green("[...] Formating"))
    processes: list[Popen[str]] = [format_disk(disk) for disk in disks]
    for process in processes:
        process.wait()
    print(green("[*] Done!"))
    time.sleep(5)
    sys.exit()

if __name__ == "__main__":
    main()