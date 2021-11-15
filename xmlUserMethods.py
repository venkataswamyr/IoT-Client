from xml.etree.ElementTree import Element, SubElement, Comment, tostring
    
def xmlConstructLoad(ControlVal):
	DeviceTag = Element('Load')
	DataTag = SubElement(DeviceTag, 'Control')
	NameTag = SubElement(DataTag, 'Value')
	NameTag.text = ControlVal
	return tostring(DeviceTag)
