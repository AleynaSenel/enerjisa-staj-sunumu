import sys
content = open('index.html', encoding='utf-8').read()

css = """
        .features-grid {
            display: grid;
            grid-template-columns: repeat(4, 1fr);
            gap: 30px;
        }
        .feature-card {
            background: #fff;
            border-radius: 20px;
            padding: 30px;
            box-shadow: 0 10px 30px rgba(0,0,0,0.05);
            border: 1px solid rgba(0,44,95,0.05);
            display: flex;
            flex-direction: column;
            transition: transform 0.3s ease;
        }
        .feature-card:hover {
            transform: translateY(-5px);
        }
        .feature-icon-container {
            width: 48px;
            height: 48px;
            background: #FFCA28;
            border-radius: 12px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 24px;
            margin-bottom: 20px;
        }
        .feature-title {
            color: #002c5f;
            font-size: 1.15rem;
            font-weight: 700;
            margin-bottom: 12px;
            margin-top: 0;
        }
        .feature-desc {
            color: #64748b;
            font-size: 0.95rem;
            line-height: 1.6;
            margin: 0;
        }
        @media (max-width: 1024px) {
            .features-grid {
                grid-template-columns: repeat(2, 1fr);
            }
        }
        @media (max-width: 768px) {
            .features-grid {
                gap: 12px;
            }
            .feature-card {
                padding: 16px;
                border-radius: 16px;
            }
            .feature-icon-container {
                width: 40px;
                height: 40px;
                font-size: 20px;
                margin-bottom: 12px;
            }
            .feature-title {
                font-size: 0.95rem;
                margin-bottom: 8px;
            }
            .feature-desc {
                font-size: 0.8rem;
                line-height: 1.4;
            }
        }
"""

content = content.replace('</style>', css + '\n    </style>')

content = content.replace('style="display: grid; grid-template-columns: repeat(auto-fit, minmax(250px, 1fr)); gap: 30px;"', 'class="features-grid"')

card_inline = 'style="background: #fff; border-radius: 20px; padding: 30px; box-shadow: 0 10px 30px rgba(0,0,0,0.05); border: 1px solid rgba(0,44,95,0.05); display: flex; flex-direction: column; transition: transform 0.3s ease;" onmouseover="this.style.transform=\'translateY(-5px)\'" onmouseout="this.style.transform=\'translateY(0)\'"'
content = content.replace(card_inline, 'class="feature-card"')

icon_inline = 'style="width: 48px; height: 48px; background: #FFCA28; border-radius: 12px; display: flex; align-items: center; justify-content: center; font-size: 24px; margin-bottom: 20px;"'
content = content.replace(icon_inline, 'class="feature-icon-container"')

title_inline = 'style="color: #002c5f; font-size: 1.15rem; font-weight: 700; margin-bottom: 12px; margin-top: 0;"'
content = content.replace(title_inline, 'class="feature-title"')

desc_inline = 'style="color: #64748b; font-size: 0.95rem; line-height: 1.6; margin: 0;"'
content = content.replace(desc_inline, 'class="feature-desc"')

open('index.html', 'w', encoding='utf-8').write(content)
print('Done')
