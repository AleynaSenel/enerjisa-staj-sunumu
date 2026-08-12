import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def generate_html(start, end):
    html = '<div class="slide-container" style="display: flex; flex-direction: column; gap: 30px; width: 100%;">\n'
    for i in range(start, end + 1):
        html += f'                        <img src="slides/Slide{i}.jpg" alt="Slide {i}" style="width: 100%; border-radius: 12px; box-shadow: 0 8px 30px rgba(0,0,0,0.15); border: 1px solid rgba(0,0,0,0.05);">\n'
    html += '                    </div>'
    return html

sections = {
    'bolum-01': (4, 9),
    'bolum-02': (10, 14),
    'bolum-03': (15, 20),
    'bolum-04': (21, 25),
    'bolum-05': (26, 31),
    'bolum-06': (32, 37),
    'bolum-07': (38, 43),
    'bolum-08': (44, 48)
}

for section_id, (start, end) in sections.items():
    pattern = rf'(<section id="{section_id}"[^>]*>\s*<div class="huge-number">\d+</div>\s*<div class="fluid-content">\s*<h2 class="fluid-title">[^<]+</h2>)[\s\S]*?(?=</section>)'
    
    match = re.search(pattern, content)
    if match:
        prefix = match.group(1)
        slides_html = generate_html(start, end)
        new_content = prefix + "\n                </div>\n                <div class=\"fluid-media\" style=\"background: none; border: none; box-shadow: none; min-height: auto;\">\n                    " + slides_html + "\n                </div>\n            "
        content = content[:match.start()] + new_content + content[match.end():]
    else:
        print(f"Could not find {section_id}")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done")
