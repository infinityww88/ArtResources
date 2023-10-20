import sys
import json
from pyquery import PyQuery as pq
from xml import etree

# fn = "双子座/双子座-位置.svg"
# msys 命令行用正斜线 双子座\双子座-位置.svg，否则反斜线 / 会被 msys 替换为 C:/msys64/

fn = sys.argv[1]
d = pq(filename=fn, encoding="utf-8")

g = d("#g1")
points = []
for e in g:
    circles = e.findall("{http://www.w3.org/2000/svg}circle")
    for c in circles:
        points.append({"x":c.attrib["cx"], "y":"-" + c.attrib["cy"]})
print(json.dumps({"data":points}))
