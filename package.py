name = "llvm"

version = "18.1.1"

authors = [
    "Vikram Adve",
    "Chris Lattner",
    "LLVM Developer Group"
]

description = \
    """
    The LLVM Project is a collection of modular and reusable compiler and toolchain technologies.
    Despite its name, LLVM has little to do with traditional virtual machines. The name "LLVM" itself is not an
    acronym; it is the full name of the project.
    """

requires = [
    "cmake-3+",
    "gcc-11",
    "python-3.9.16",
    "zlib-1.2"
]

variants = [
    ["platform-linux","arch-x86_64"]
]

tools = [
    "clang",
    "clang++",
    "clang-cpp"
]

build_system = "cmake"

with scope("config") as config:
    config.build_thread_count = "logical_cores"

uuid = "llvm-{version}".format(version=str(version))

def commands():
    env.PATH.prepend("{root}/bin")
    env.LD_LIBRARY_PATH.prepend("{root}/lib")
    env.CMAKE_MODULE_PATH.prepend("{root}/lib/cmake/clang:{root}/lib/cmake/llvm")

    # Helper environment variables.
    env.LLVM_BINARY_PATH.set("{root}/bin")
    env.LLVM_INCLUDE_PATH.set("{root}/include")
    env.LLVM_LIBRARY_PATH.set("{root}/lib")
