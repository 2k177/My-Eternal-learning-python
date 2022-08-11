import xml.etree.ElementTree as ET

tree = ET.parse('country_data.xml')

root = tree.getroot()
print(root.tag)
print(root.attrib) #Attributes are dictionary containing details
for child in root:
     print(child.tag, child.attrib)
print(root[0][1].text)

"""Element has some useful methods that help iterate recursively over all the 
sub-tree below it (its children, their children, and so on)."""
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

"""Element.findall() finds only elements with a tag which are direct children 
of the current element. Element.find() finds the first child with a particular 
tag, and Element.text accesses the element’s text content. Element.get() 
accesses the element’s attributes"""

for country in root.findall('country'):
     rank = country.find('rank').text
     name = country.get('name')
     print(name, rank)


""" Modify xml """
#Update node
for rank in root.iter('rank'):
     new_rank = int(rank.text) + 1
     rank.text = str(new_rank)
     rank.set('updated', 'yes')
tree.write('output.xml')

#delete node
for country in root.findall('country'):
     # using root.findall() to avoid removal during traversal
     rank = int(country.find('rank').text)
     if rank > 50:
         root.remove(country)

tree.write('output_remove.xml')


"""Building XML documents"""
#The SubElement() function also provides a convenient way to create new
# sub-elements for a given element
