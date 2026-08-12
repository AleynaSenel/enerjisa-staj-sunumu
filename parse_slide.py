import xml.etree.ElementTree as ET

ns = {'p': 'http://schemas.openxmlformats.org/presentationml/2006/main',
      'a': 'http://schemas.openxmlformats.org/drawingml/2006/main'}

tree = ET.parse(r'c:\Users\Aleyna\Desktop\toroslar-tanitim\pptx_extracted\ppt\slides\slide2.xml')
root = tree.getroot()

def get_text(node):
    texts = node.findall('.//a:t', ns)
    return "".join([t.text for t in texts if t.text])

def get_rect(node):
    off = node.find('.//a:off', ns)
    ext = node.find('.//a:ext', ns)
    if off is not None and ext is not None:
        return int(off.get('x', 0)), int(off.get('y', 0)), int(ext.get('cx', 0)), int(ext.get('cy', 0))
    return 0, 0, 0, 0

print("--- TEXTS ---")
for sp in root.findall('.//p:sp', ns):
    text = get_text(sp).strip()
    if text:
        x, y, w, h = get_rect(sp)
        print(f"TEXT: {text[:30]:<30} | x={x:<8} y={y:<8} w={w:<8} h={h:<8}")

print("\n--- IMAGES ---")
for pic in root.findall('.//p:pic', ns):
    blip = pic.find('.//a:blip', ns)
    if blip is not None:
        rid = blip.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
        x, y, w, h = get_rect(pic)
        print(f"IMAGE: {rid:<10} | x={x:<8} y={y:<8} w={w:<8} h={h:<8}")
