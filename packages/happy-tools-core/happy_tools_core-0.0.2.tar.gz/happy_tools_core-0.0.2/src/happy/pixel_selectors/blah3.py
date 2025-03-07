import shlex
from happy.criteria import Criteria

c1 = Criteria(operation="in", value=[1], key="mask").to_json()
simple_cmd1 = shlex.join(["ps-simple", "-n", "100", "-c", c1])
print(simple_cmd1)
