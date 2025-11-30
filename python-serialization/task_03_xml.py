#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML, preserving data types."""
    try:
        root = ET.Element("data")

        for key, value in dictionary.items():
            child = ET.SubElement(root, key)

            # Store type information
            child.set("type", type(value).__name__)
            child.text = str(value)

        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)
        return True

    except Exception:
        return False


def deserialize_from_xml(filename):
    """Deserialize XML back into a Python dictionary with correct types."""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        for child in root:
            value_type = child.get("type")
            text = child.text

            if value_type == "int":
                value = int(text)
            elif value_type == "float":
                value = float(text)
            elif value_type == "bool":
                value = True if text == "True" else False
            elif value_type == "NoneType":
                value = None
            else:
                value = text  # default: string

            result[child.tag] = value

        return result

    except Exception:
        return None
