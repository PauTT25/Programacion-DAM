from lxml import etree

xml_doc = etree.parse("curriculum en xml.xml")
xsd_doc = etree.parse("002 esquema.xsd")

schema = etree.XMLSchema(xsd_doc)

print(schema.validate(xml_doc))
