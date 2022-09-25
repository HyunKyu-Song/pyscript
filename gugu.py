from xml.dom.minidom import Element


def gugudan(*a):
   result = Element("result")
   n = int(input("what num gugudan?"))
   gugu_str = ''
   for i in range(1, 10):
      gugu_str += f"{n} x {i} = {n*i}<br>"
   result.write(gugu_str)