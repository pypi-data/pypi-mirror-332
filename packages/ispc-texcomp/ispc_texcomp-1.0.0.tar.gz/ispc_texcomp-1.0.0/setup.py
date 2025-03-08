import os
import platform

from setuptools import Extension, setup
from setuptools.command.build_ext import build_ext
from wheel.bdist_wheel import bdist_wheel

from typing import List


class build_ext_ispc(build_ext):
    def build_extension(self, ext):
        build_temp = os.path.realpath(self.build_temp)

        # remove ispc files from sources
        ispc_files = []
        i = 0
        while i < len(ext.sources):
            if ext.sources[i].endswith(".ispc"):
                ispc_files.append(ext.sources.pop(i))
            else:
                i += 1

        # compile ispc files
        extra_objects = self.build_ispc(ispc_files)
        # add ispc objects to extra_objects for linking
        ext.extra_objects.extend(extra_objects)
        # add build_temp to include_dirs to include generated .h files
        ext.include_dirs.append(build_temp)

        super().build_extension(ext)

    def build_ispc(self, ispc_files: List[str]) -> List[str]:
        extra_objects: List[str] = []
        for source in ispc_files:
            name = os.path.basename(source)[:-5]
            source = os.path.realpath(source)
            output = os.path.realpath(os.path.join(self.build_temp, f"{name}.o"))
            header = os.path.realpath(os.path.join(self.build_temp, f"{name}_ispc.h"))
            self.run_ispc(source, output, header)
            extra_objects.append(output)
        return extra_objects

    def run_ispc(self, src_fp: str, out_fp: str, header_fp: str):
        os.makedirs(os.path.dirname(out_fp), exist_ok=True)
        os.makedirs(os.path.dirname(header_fp), exist_ok=True)
        self.spawn([
            "ispc",
            "-O2",
            src_fp,
            "-o",
            out_fp,
            "-h",
            header_fp,
            "--opt=fast-math",
            "--pic",
        ])


class bdist_wheel_abi3(bdist_wheel):
    def get_tag(self):
        python, abi, plat = super().get_tag()

        if python.startswith("cp"):
            # on CPython, our wheels are abi3 and compatible back to 3.7
            return "cp311", "abi3", plat

        return python, abi, plat


def get_extra_compile_args():
    system = platform.system()
    if system == "Windows":
        return ["/std:c++17"]
    elif system == "Darwin":
        return ["-std=c++17"]
    else:
        return ["-std=c++17"]


setup(
    name="ispc_texcomp",
    packages=["ispc_texcomp"],
    package_data={"ispc_texcomp": ["*.py", "*.pyi", "py.typed"]},
    include_package_data=True,
    ext_modules=[
        Extension(
            name="ispc_texcomp._ispc_texcomp",
            sources=[
                "src/ispc_texcomp_py.cpp",
                "src/ISPCTextureCompressor/ispc_texcomp/ispc_texcomp.cpp",
                "src/ISPCTextureCompressor/ispc_texcomp/ispc_texcomp_astc.cpp",
                "src/ISPCTextureCompressor/ispc_texcomp/kernel.ispc",
                "src/ISPCTextureCompressor/ispc_texcomp/kernel_astc.ispc",
            ],
            depends=[
                "src/rgba_surface_py.hpp",
                "src/settings.hpp",
                "src/ISPCTextureCompressor/ispc_texcomp/ispc_texcomp.h",
                "src/ISPCTextureCompressor/ispc_texcomp/ispc_texcomp.def",
            ],
            language="c++",
            include_dirs=["src/ISPCTextureCompressor/ispc_texcomp"],
            extra_compile_args=get_extra_compile_args(),
            define_macros=[
                ("Py_LIMITED_API", "0x030b0000"),
            ],
            py_limited_api=True,
        ),
    ],
    cmdclass={"build_ext": build_ext_ispc, "bdist_wheel": bdist_wheel_abi3},
    zip_safe=False,
)
