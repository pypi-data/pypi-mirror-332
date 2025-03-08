from setuptools import setup, find_packages
import platform
import shutil
import os

def get_shared_libraries():
    system = platform.system().lower()
    machine = platform.machine().lower()

    arch_map = {
        "amd64": "x86_64",
        "x86_64": "x86_64",
        "i386": "i686",
        "i686": "i686",
        "armv7l": "armv7",
        "aarch64": "aarch64",
    }

    machine_folder = arch_map.get(machine, machine)

    if system == "linux":
        src_files = [f"pinggy/linux/{machine_folder}/libpinggy.so", f"pinggy/linux/{machine_folder}/pinggyclient"]
    elif system == "darwin":
        src_files = ["pinggy/macos/universal/libpinggy.dylib", "pinggy/macos/universal/pinggyclient"]
    elif system == "windows":
        src_files = [f"pinggy/windows/{machine_folder}/pinggy.dll"]
    else:
        raise RuntimeError(f"Unsupported OS: {system}")

    dest_dir = "pinggy/bin"
    os.makedirs(dest_dir, exist_ok=True)

    copied_files = []
    for src in src_files:
        dest = os.path.join(dest_dir, os.path.basename(src))
        shutil.copy2(src, dest)
        copied_files.append(f"bin/{os.path.basename(src)}")  # Relative to `pinggy`

    return copied_files

setup(
    name="dev-pinggy",
    version="1.0.0",
    author="Bishnu",
    author_email="bishnuthakur284@gmail.com",
    description="Pinggy package for tunneling",
    packages=find_packages(),
    include_package_data=True,
    package_data={"pinggy": get_shared_libraries()}, 
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)