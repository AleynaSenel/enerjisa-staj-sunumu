import sys
html = open('index.html', encoding='utf-8').read()

replacements = [
    ('Aydanur Akın</h3>\n                        <p class="member-role">Proje Lideri</p>\n                        <div class="social-links">\n                            <a href="#"', 'Aydanur Akın</h3>\n                        <p class="member-role">Proje Lideri</p>\n                        <div class="social-links">\n                            <a href="https://www.linkedin.com/in/aydanur-akin"'),
    ('Gökalp Eke</h3>\n                        <p class="member-role">Teknik Lider (AI)</p>\n                        <div class="social-links">\n                            <a href="#"', 'Gökalp Eke</h3>\n                        <p class="member-role">Teknik Lider (AI)</p>\n                        <div class="social-links">\n                            <a href="https://www.linkedin.com/in/gökalp-eke-900b663a1?utm_source=share_via&utm_content=profile&utm_medium=member_ios"'),
    ('Yasemin Uslu</h3>\n                        <p class="member-role">Optimizasyon Lideri</p>\n                        <div class="social-links">\n                            <a href="#"', 'Yasemin Uslu</h3>\n                        <p class="member-role">Optimizasyon Lideri</p>\n                        <div class="social-links">\n                            <a href="https://tr.linkedin.com/in/yasemin-uslu-76734a29a"'),
    ('Özgür Sakallı</h3>\n                        <p class="member-role">Veri Analizi Lideri</p>\n                        <div class="social-links">\n                            <a href="#"', 'Özgür Sakallı</h3>\n                        <p class="member-role">Veri Analizi Lideri</p>\n                        <div class="social-links">\n                            <a href="https://www.linkedin.com/in/özgür-sakallı-20667b374?utm_source=share_via&utm_content=profile&utm_medium=member_ios"'),
    ('Selin Efesoy</h3>\n                        <p class="member-role">Pilot Uygulama Lideri</p>\n                        <div class="social-links">\n                            <a href="#"', 'Selin Efesoy</h3>\n                        <p class="member-role">Pilot Uygulama Lideri</p>\n                        <div class="social-links">\n                            <a href="http://linkedin.com/in/selin-efesoy-248bb7313"'),
    ('Arzu Güven</h3>\n                        <p class="member-role">Literatür ve Bakım Süreçleri Lideri</p>\n                        <div class="social-links">\n                            <a href="#"', 'Arzu Güven</h3>\n                        <p class="member-role">Literatür ve Bakım Süreçleri Lideri</p>\n                        <div class="social-links">\n                            <a href="https://www.linkedin.com/in/arzu-güven-88132a357?utm_source=share_via&utm_content=profile&utm_medium=member_android"'),
    ('Aleyna Şenel</h3>\n                        <p class="member-role">Görüntü İşleme Lideri</p>\n                        <div class="social-links">\n                            <a href="#" target="_blank" title="GitHub">', 'Aleyna Şenel</h3>\n                        <p class="member-role">Görüntü İşleme Lideri</p>\n                        <div class="social-links">\n                            <a href="https://github.com/AleynaSenel" target="_blank" title="GitHub">'),
    ('</a>\n                            <a href="#" target="_blank" title="LinkedIn">', '</a>\n                            <a href="https://www.linkedin.com/in/aleyna-şenel" target="_blank" title="LinkedIn">')
]

for old, new in replacements:
    if old in html:
        html = html.replace(old, new)
        print(f"Replaced successfully for {new[-30:]}")
    else:
        print(f"Failed to find block for {new[-30:]}")

open('index.html', 'w', encoding='utf-8').write(html)
