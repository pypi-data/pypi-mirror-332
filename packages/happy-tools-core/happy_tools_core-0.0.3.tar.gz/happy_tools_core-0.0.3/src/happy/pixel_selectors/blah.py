from happy.base.core import ConfigurableObject

s = '{"class": "happy.pixel_selectors.MultiSelector", "selectors": [{"class": "happy.pixel_selectors.SimpleSelector", "n": 64}]}'
o = ConfigurableObject.from_json(s)
print(type(o))
print(o.to_dict())
