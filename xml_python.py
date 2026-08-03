import xml.etree.ElementTree as ET

xml_data = """
<user>
    <id>1</id>
    <first_name>John</first_name>
    <last_name>Doe</last_name>
    <age>30</age>
    <email>john.doe@example.com</email>
</user>
"""

root = ET.fromstring(xml_data)  #создает объект
print("User ID: ", root.find('id').text)
print("User Name: ", root.find('first_name').text, root.find('last_name').text)
print("User age: ", root.find('age').text)
