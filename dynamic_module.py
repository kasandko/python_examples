from types import ModuleType
import sys

def load_module(source, name, docstr=""):
    module = ModuleType(name, docstr)
    exec(source, module.__dict__)
    sys.modules[name] = module

source_a = """
class TestA:
    def func(self):
        return 30
"""

load_module(source_a, "module_a")

source_b = """
from module_a import TestA
    
class TestB:
    def func(self):
        return TestA().func() + 12
"""

load_module(source_b, "module_b")

import module_b
print(module_b.TestB().func())
