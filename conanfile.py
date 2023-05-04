import os
 
from conans import ConanFile, CMake, tools

def get_verion_tag():
    git = tools.Git("stonex-cms-amqp-test-framework")
    try:
        return "%s" % (git.get_tag())
    except Exception as e:
        return e
        
class StonexCMSAMQPTests(ConanFile):
    name = "core-test"
    version = get_verion_tag()
    license = "<Put the package license here>"
    author = "krzysztof.obrebski@stonex.com"
    url = "<Package recipe repository url here, for issues about the package>"
    description = "cms client core test"
    topics = ("cms","amqp")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False], "fPIC": [True, False]}
    default_options = {"shared": False, "fPIC": True}
    requires = ["stonex-cms-amqp-test-cases/0.0.2@enterprise_messaging/test"]
    generators = "cmake"

    def config_options(self):
        if self.settings.os == "Windows":
            del self.options.fPIC

    def source(self):
        pass

    def build(self):
        cmake = CMake(self)
        cmake.configure()
        cmake.build()


    def package(self):
        self.copy("*.h", dst="include",src="include/")
        self.copy("*.config", dst="config",src="config/")
        self.copy("*.exe", dst="bin",src="bin", keep_path=False)
        self.copy("*.pdb", dst="bin",src="bin", keep_path=False)

    def package_info(self):
        pass

    
