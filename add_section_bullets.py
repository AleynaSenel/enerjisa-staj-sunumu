import re

html_content = open('index.html', encoding='utf-8').read()

bullets = {
    "bolum-01": [
        "Şebekedeki arıza kaynakları elektriksel/mekanik, çevresel/iklimsel ve ekipman/izolasyon olmak üzere üç ana grupta sınıflandırıldı.",
        "Ağaç teması %21,3 ile en büyük paya sahip; kırsal bölgelerdeki etki kentsele kıyasla çok daha yüksek (%90,1)."
    ],
    "bolum-02": [
        "20.715 varlık, 8.513 kesinti kaydı ve 71.322 SCADA olayı tek bir veri setinde birleştirilip CEER (39 Avrupa ülkesi) referanslarıyla doğrulandı.",
        "Eksik kayıtlar rastgele değil; IQR yöntemiyle tespit edilen 104 aykırı kayıttan 93'ü kurtarılarak veri kalitesi artırıldı."
    ],
    "bolum-03": [
        "Reaktif müdahale yerine, geçmiş arıza ve operasyonel sinyallerden yola çıkarak her fider için önümüzdeki 7 günün arıza riski tahmin ediliyor.",
        "Decision Tree, Random Forest, XGBoost, SVM ve Gradient Boosting karşılaştırılarak en isabetli model ana karar motoru olarak seçildi."
    ],
    "bolum-04": [
        "Binlerce varlığın manuel önceliklendirilmesi imkânsız olduğundan, ISO 31000 uyumlu Olasılık × Etki modeliyle her varlık 0–100 arası tek bir risk skoruna indirgeniyor.",
        "Model EPDK'nın SAIFI/SAIDI/AENS hedefleriyle uyumlu çalışıyor ve kısıtlı ekip kaynağını en kritik varlıklara yönlendiriyor."
    ],
    "bolum-05": [
        "Kısıtlı bakım ekibi kapasitesiyle beklenen faydayı maksimize etmek için Operasyon Araştırması ve Lineer Programlama tabanlı bir önceliklendirme kuruldu.",
        "Toroslar EDAŞ bölgesindeki 20.715 varlık için risk ve bütçeyi dengeleyen çok yıllı bir yatırım programı oluşturuldu."
    ],
    "bolum-06": [
        "Mersin bölgesinde 2021–2025 arası 8.387 plansız kesinti kaydı incelendi; ağaç teması, hava koşulları ve ekipman yaşlanması olayların %56'sını oluşturuyor.",
        "Önerilen bakım programıyla kırsal SAIDI 2.607'den 987'ye, SAIFI 12,7'den 4,8'e düşürülerek hedefli bakımın etkisi sahada test edildi."
    ],
    "bolum-07": [
        "Geleneksel fiziksel denetimlerin yüksek maliyeti ve insan faktörüne bağlı öngörülemeyen risklerine karşı, saha görüntülerinden otonom tespit yapan bir YOLOv8 modeli geliştirildi.",
        "Model %84 kesinlik ve %67 mAP50 ile hasarlı direk, izolatör ve ağaç ihlallerini tespit ediyor; ince kablo kopukluklarında duyarlılığın artırılması hedefleniyor."
    ],
    "bolum-08": [
        "Veri, Analitik, Karar Destek ve Dashboard UI olmak üzere 4 katmanlı esnek ve modüler bir sistem mimarisi sıfırdan kurgulandı.",
        "OMS kesinti verilerinden canlı arayüze otomatik veri akışı sağlanarak ekip çıktıları ve maliyet kararları Streamlit dashboard'una entegre edildi."
    ]
}

# The sections have structure:
# <section id="bolum-01" ...>
#     <div class="huge-number">01</div>
#     <div class="fluid-content">
#         <h2 class="fluid-title">...</h2>
#     </div>

for section_id, bullet_list in bullets.items():
    # We find the section by id
    # Then find the end of fluid-title inside it and append the list
    
    # regex to find <section id="bolum-0X"...>...<h2 class="fluid-title">TITLE</h2>
    # we want to insert the ul right after </h2>
    
    pattern = r'(<section id="' + section_id + r'".*?<h2 class="fluid-title">.*?</h2>)'
    
    ul_html = '\n                    <ul class="fluid-list" style="margin-top: 30px;">\n'
    for b in bullet_list:
        ul_html += f'                        <li>{b}</li>\n'
    ul_html += '                    </ul>'
    
    html_content = re.sub(pattern, r'\1' + ul_html, html_content, flags=re.DOTALL)

open('index.html', 'w', encoding='utf-8').write(html_content)
print("Updated all sections successfully.")
