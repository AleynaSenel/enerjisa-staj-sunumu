import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

def replacer(match):
    inner_html = match.group(1)
    imgs = re.findall(r'<img[^>]+>', inner_html)
    if not imgs:
        return match.group(0)
    
    first_img = imgs[0]
    rest_imgs = imgs[1:]
    
    html = f'''<div class="slides-card" style="background: #ffffff; border-radius: 24px; padding: 24px; box-shadow: 0 12px 40px rgba(0, 44, 95, 0.08); display: flex; flex-direction: column; align-items: center; width: 100%;">
                        <div class="slides-visible" style="width: 100%;">
                            {first_img}
                        </div>
                        <div class="slides-hidden" style="display: none; width: 100%; flex-direction: column; gap: 30px; margin-top: 30px;">
                            {''.join(f"                            {img}\\n" for img in rest_imgs)}
                        </div>
                        <button class="show-more-btn" onclick="toggleSlides(this)" style="margin-top: 30px; background: #002C5F; color: #fff; border: none; border-radius: 30px; padding: 14px 40px; font-size: 1.1rem; font-weight: 600; cursor: pointer; transition: all 0.3s ease; display: flex; align-items: center; gap: 8px; box-shadow: 0 8px 20px rgba(0, 44, 95, 0.2);">
                            Diğer Slaytları Görüntüle <span class="arrow" style="font-size: 0.9em;">▼</span>
                        </button>
                    </div>'''
    return html

pattern = r'<div class="slide-container"[^>]*>([\s\S]*?)</div>'

new_content = re.sub(pattern, replacer, content)

js_code = """
            <script>
                function toggleSlides(btn) {
                    const card = btn.closest('.slides-card');
                    const hiddenDiv = card.querySelector('.slides-hidden');
                    
                    if (hiddenDiv.style.display === 'none') {
                        hiddenDiv.style.display = 'flex';
                        btn.innerHTML = 'Daha Az Göster <span class="arrow" style="font-size: 0.9em;">▲</span>';
                    } else {
                        hiddenDiv.style.display = 'none';
                        btn.innerHTML = 'Diğer Slaytları Görüntüle <span class="arrow" style="font-size: 0.9em;">▼</span>';
                        card.scrollIntoView({ behavior: 'smooth', block: 'center' });
                    }
                }
            </script>
"""

if "function toggleSlides" not in new_content:
    new_content = new_content.replace('<!-- AOS JS -->', js_code + '\n            <!-- AOS JS -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Updated successfully")
