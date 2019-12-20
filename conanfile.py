from conans import ConanFile, CMake, tools


class BinacppConan(ConanFile):
    name = "binacpp"
    settings = "os", "compiler", "build_type", "arch"
    description = "Binance C++ library "
    url = "https://github.com/tensaix2j/binacpp"
    license = "MIT"
    author = "https://github.com/tensaix2j"
    generators = "cmake"
    requires = [
        "jsoncpp/1.8.4@theirix/stable",
        "libcurl/7.56.1@bincrafters/stable",
        "libwebsockets/2.4.0@bincrafters/stable"
    ]

    def source(self):
        git = tools.Git()
        git.clone("https://github.com/sturd/binacpp.git")
        git.checkout("sturd_downstream_changes")

    def configure(self):
        if(self.settings.os == "Linux"):
            self.options["jsoncpp"].shared = True

    def build(self):
        cmake = CMake(self)
        cmake.verbose = True

        cmake.configure(build_folder="cmake")
        cmake.build()

    def package(self):
        self.copy("*.h", src="src", dst="include")
        self.copy("*.so*", src="cmake", dst="lib")
        self.copy("*.a", src="cmake", dst="lib")

    def package_info(self):
        self.cpp_info.libs = tools.collect_libs(self)
