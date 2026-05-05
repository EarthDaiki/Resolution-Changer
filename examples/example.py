import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from resolution_changer import ResolutionChanger

rc = ResolutionChanger()
rc.change_resolution(
    "examples/input/example_input.jpg", 
    "examples/output", 
    [(16,16), (32,32), (48,48), (128,128)],
    True
)