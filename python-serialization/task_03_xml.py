#!/usr/bin/python3
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serialize a Python dictionary into XML and save it to a file.

    Args:
        dictionary (dict): The dictionary to serialize.
        filename (str): File to save the XML into.

    Returns:
        bool: True if serialization succeeds, False otherwise.
    """
    try:
        root = ET.Element("data")

        # Create XML elements for each key-value pair
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)

        # Build XML tree and write to file
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

        return True

    except Exception:
        return False


def deserialize_from_xml(filename):
    """Deserialize XML data from a file back into a Python dictionary.

    Args:
        filename (str): XML file to read.

    Returns:
        dict or None: The reconstructed dictionary, or None on failure.
    """
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}

        # Convert text back into the appropriate types
        for child in root:
            text = child.text

            # Attempt type reconstruction
            if text is None:
                value = None
            else:
                # Try to convert back to int or float if applicable
                if text.isdigit():
                    value = int(text)
                else:
                    # Try float conversion
                    try:
                        value = float(text)
                    except ValueError:
                        # Fall back to string
                        value = text

            result[child.tag] = value

        return result

    except Exception:
        return None
