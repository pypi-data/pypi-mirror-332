import shlex
from happy.criteria import Criteria
from happy.pixel_selectors import PixelSelector

c1 = Criteria(operation="in", value=[1], key="mask").to_json()
c2 = Criteria(operation="in", value=[2], key="mask").to_json()
simple_cmd1 = shlex.join(["ps-simple", "-n", "100", "-c", c1])
print(simple_cmd1)
simple_cmd2 = shlex.join(["ps-simple", "-n", "100", "-c", c2])
multi_cmd = shlex.join(["ps-multi", "-s", simple_cmd1, simple_cmd2])
print(multi_cmd)
multi = PixelSelector.parse_pixel_selector(multi_cmd)
print(multi.to_dict())
