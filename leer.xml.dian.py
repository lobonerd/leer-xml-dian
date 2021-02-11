import xml.etree.ElementTree as ET

tree = ET.parse('xml/832000662_101-FVP-91631.xml')
root = tree.getroot()

namespace = {
    'cac': 'urn:oasis:names:specification:ubl:schema:xsd:CommonAggregateComponents-2',
    'cbc': 'urn:oasis:names:specification:ubl:schema:xsd:CommonBasicComponents-2',
    'cdt': 'urn:DocumentInformation:names:specification:ubl:colombia:schema:xsd:DocumentInformationAggregateComponents-1',
    'chl': 'urn:carvajal:names:specification:ubl:colombia:schema:xsd:CarvajalHealthComponents-1',
    'clm54217': 'urn:un:unece:uncefact:codelist:specification:54217:2001',
    'clm66411': 'urn:un:unece:uncefact:codelist:specification:66411:2001',
    'clmIANAMIMEMediaType': 'urn:un:unece:uncefact:codelist:specification:IANAMIMEMediaType:2003',
    'cts': 'urn:carvajal:names:specification:ubl:colombia:schema:xsd:CarvajalAggregateComponents-1',
    'ds': 'http://www.w3.org/2000/09/xmldsig#',
    'ext': 'urn:oasis:names:specification:ubl:schema:xsd:CommonExtensionComponents-2',
    'grl': 'urn:General:names:specification:ubl:colombia:schema:xsd:GeneralAggregateComponents-1',
    'ipt': 'urn:DocumentInformation:names:specification:ubl:colombia:schema:xsd:InteroperabilidadPT-1',
    'qdt': 'urn:oasis:names:specification:ubl:schema:xsd:QualifiedDatatypes-2',
    'sts': 'dian:gov:co:facturaelectronica:Structures-2-1',
    'udt': 'urn:un:unece:uncefact:data:specification:UnqualifiedDataTypesSchemaModule:2',
    'xades': 'http://uri.etsi.org/01903/v1.3.2#',
    'xades141': 'http://uri.etsi.org/01903/v1.4.1#',
    'xsi': 'http://www.w3.org/2001/XMLSchema-instance'
}

attachments = []

for document in root.findall('cac:Attachment', namespace):
    for child in document.findall('cac:ExternalReference', namespace):
        attachment = child.find('cbc:Description', namespace).text
        tr = ET.XML(attachment)
        for b in tr:
            attachments.append(b.text)

print(attachments)