import xml.dom.minidom

doc = xml.dom.minidom.parse("country_data.xml")
print(doc.nodeName)
print(doc.firstChild.tagName)

newexpertise = doc.createElement("expertise")
newexpertise.setAttribute("name", "BigData")


country_info = doc.getElementsByTagName("country")
for prop in country_info:
    print(prop.getAttribute("name"))
    if prop.getAttribute("name") == "Singapore":
        prop.appendChild(newexpertise)

xml_str = doc.toprettyxml(indent ="\t")
with open("country_data_copy.xml", "w") as f:
    f.write(xml_str)