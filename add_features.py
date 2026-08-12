import sys

html_block = """
            <!-- ÖNE ÇIKAN ÖZELLİKLER BÖLÜMÜ -->
            <section id="ozellikler" style="width: 100%; max-width: 1200px; margin: 0 auto 120px auto; padding: 0 20px;">
                <h2 class="section-title" data-aos="fade-up" style="text-align: center; margin-bottom: 60px;">Öne Çıkan Özellikler</h2>
                <div style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px;" data-aos="fade-up" data-aos-delay="200">
                    
                    <div style="background: #fff; border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid rgba(0,44,95,0.05); display: flex; flex-direction: column; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <div style="width: 48px; height: 48px; background: rgba(253,185,19,0.15); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 20px;">🛠️</div>
                        <h3 style="color: #002c5f; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; margin-top: 0;">Kestirimci Bakım</h3>
                        <p style="color: #64748b; font-size: 0.95rem; line-height: 1.6; margin: 0;">Reaktif bakıma kıyasla plansız kesintilerde %40 düşüş, bakım maliyetinde %30 tasarruf sağlanıyor.</p>
                    </div>

                    <div style="background: #fff; border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid rgba(0,44,95,0.05); display: flex; flex-direction: column; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <div style="width: 48px; height: 48px; background: rgba(253,185,19,0.15); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 20px;">🧹</div>
                        <h3 style="color: #002c5f; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; margin-top: 0;">Temiz & Güvenilir Veri</h3>
                        <p style="color: #64748b; font-size: 0.95rem; line-height: 1.6; margin: 0;">20.715 varlık ile 100 binin üzerinde SCADA/OMS kaydı birleştirilip standardize edildi, SAIDI göstergesi %4 düzeltildi.</p>
                    </div>

                    <div style="background: #fff; border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid rgba(0,44,95,0.05); display: flex; flex-direction: column; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <div style="width: 48px; height: 48px; background: rgba(253,185,19,0.15); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 20px;">🧠</div>
                        <h3 style="color: #002c5f; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; margin-top: 0;">7 Günlük Arıza Tahmini</h3>
                        <p style="color: #64748b; font-size: 0.95rem; line-height: 1.6; margin: 0;">Random Forest modeli ilk 350 hedefte %59,7 sahada isabet ve 2,53 kat lift ile arızaları önceden işaret ediyor.</p>
                    </div>

                    <div style="background: #fff; border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid rgba(0,44,95,0.05); display: flex; flex-direction: column; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <div style="width: 48px; height: 48px; background: rgba(253,185,19,0.15); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 20px;">📊</div>
                        <h3 style="color: #002c5f; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; margin-top: 0;">0–100 Risk Skoru</h3>
                        <p style="color: #64748b; font-size: 0.95rem; line-height: 1.6; margin: 0;">ISO 31000 uyumlu model, 20.715 varlığın tamamını tek bir risk skoruna indirgiyor; kritik varlıklar anında görünür.</p>
                    </div>

                    <div style="background: #fff; border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid rgba(0,44,95,0.05); display: flex; flex-direction: column; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <div style="width: 48px; height: 48px; background: rgba(253,185,19,0.15); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 20px;">💰</div>
                        <h3 style="color: #002c5f; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; margin-top: 0;">Optimum Bakım Planı</h3>
                        <p style="color: #64748b; font-size: 0.95rem; line-height: 1.6; margin: 0;">Lineer programlama ile 6.278 varlık önceliklendirildi; 40,9M TL beklenen fayda, kısıtlı ekip kapasitesine göre planlandı.</p>
                    </div>

                    <div style="background: #fff; border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid rgba(0,44,95,0.05); display: flex; flex-direction: column; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <div style="width: 48px; height: 48px; background: rgba(253,185,19,0.15); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 20px;">📉</div>
                        <h3 style="color: #002c5f; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; margin-top: 0;">SAIDI–SAIFI İyileşmesi</h3>
                        <p style="color: #64748b; font-size: 0.95rem; line-height: 1.6; margin: 0;">Mersin pilot bölgesinde önerilen program ile kırsal SAIDI 2.607'den 987'ye, SAIFI 12,7'den 4,8'e düşürülüyor.</p>
                    </div>

                    <div style="background: #fff; border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid rgba(0,44,95,0.05); display: flex; flex-direction: column; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <div style="width: 48px; height: 48px; background: rgba(253,185,19,0.15); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 20px;">📷</div>
                        <h3 style="color: #002c5f; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; margin-top: 0;">Görüntüyle Arıza Tespiti</h3>
                        <p style="color: #64748b; font-size: 0.95rem; line-height: 1.6; margin: 0;">YOLOv8 tabanlı model, saha fotoğraflarında hasarlı direk/izolatör ve ağaç ihlalini %84 kesinlikle tespit ediyor.</p>
                    </div>

                    <div style="background: #fff; border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid rgba(0,44,95,0.05); display: flex; flex-direction: column; transition: transform 0.3s ease;" onmouseover="this.style.transform='translateY(-5px)'" onmouseout="this.style.transform='translateY(0)'">
                        <div style="width: 48px; height: 48px; background: rgba(253,185,19,0.15); border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 20px;">🗺️</div>
                        <h3 style="color: #002c5f; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; margin-top: 0;">Canlı İzleme Ekranı</h3>
                        <p style="color: #64748b; font-size: 0.95rem; line-height: 1.6; margin: 0;">4 katmanlı mimari üzerine kurulu Streamlit dashboard'u, risk haritasını ve canlı arıza uyarılarını tek ekranda topluyor.</p>
                    </div>
                </div>
            </section>
"""

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<!-- CANLI DEMO BÖLÜMÜ -->', html_block + '\n            <!-- CANLI DEMO BÖLÜMÜ -->')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Added features section successfully")
