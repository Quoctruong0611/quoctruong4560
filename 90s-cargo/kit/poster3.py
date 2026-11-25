"""Poster dự phòng phong cách WinGo (brand/phong-cach-poster.md) khi Canva hết lượt.
Trời xanh, logo thật góc trên trái, tiêu đề 3 tầng (ribbon xám than → chữ cực lớn → pill cam),
mô tả 2 dòng, hàng 3 icon hoặc thẻ thông tin, câu script "Biết hết trước khi hàng bay",
chân trang xám than cong viền cam + ô liên hệ.
Cách dùng: python3 poster3.py <key> <ra.jpg>   (key trong POSTERS)"""
import asyncio, pathlib, sys
from playwright.async_api import async_playwright
from poster2 import logo, ic, plane, bigbox, BRAND_OR, BRAND_CH

OR, CH = BRAND_OR, BRAND_CH
CSS = f"""*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:'Montserrat','Noto Color Emoji',sans-serif;
background:radial-gradient(ellipse at 80% 10%,#FFF3C4 0%,rgba(255,243,196,0) 30%),linear-gradient(180deg,#5FB3F2 0%,#9AD2FA 45%,#DCEFFC 70%,#F4F8FB 100%)}}
.abs{{position:absolute}}
.cloud{{position:absolute;background:#fff;border-radius:200px;opacity:.85;filter:blur(2px)}}
.lgbox{{position:absolute;left:40px;top:34px;background:rgba(255,255,255,.95);border-radius:22px;padding:14px 22px;box-shadow:0 6px 18px rgba(0,0,0,.12)}}
.rib{{position:absolute;left:40px;top:190px;background:{CH};color:#fff;font-weight:900;font-size:34px;letter-spacing:1px;
padding:14px 40px 14px 26px;transform:skewX(-12deg);display:flex;align-items:center;gap:14px;box-shadow:0 6px 14px rgba(0,0,0,.2)}}
.rib>*{{transform:skewX(12deg)}}
.rib:after{{content:'';position:absolute;right:-90px;top:50%;width:90px;height:6px;background:linear-gradient(90deg,{OR},rgba(242,126,41,0));border-radius:3px}}
.big{{position:absolute;left:40px;top:275px;font-weight:900;color:{CH};line-height:1.02;letter-spacing:-1px;
text-shadow:4px 4px 0 #fff,-2px -2px 0 #fff,2px -2px 0 #fff,-2px 2px 0 #fff,0 10px 20px rgba(0,0,0,.15)}}
.pill{{position:absolute;left:40px;background:{OR};color:#fff;font-weight:900;font-size:36px;padding:14px 34px;border-radius:60px;box-shadow:0 8px 18px rgba(242,126,41,.4)}}
.desc{{position:absolute;left:40px;background:rgba(255,255,255,.82);border-radius:16px;padding:14px 22px;font-size:27px;font-weight:700;color:{CH};line-height:1.45}}
.desc b{{color:{OR}}}
.icons{{position:absolute;left:30px;right:30px;display:flex;background:rgba(255,255,255,.92);border-radius:24px;padding:24px 6px;box-shadow:0 10px 24px rgba(0,0,0,.12)}}
.ii{{flex:1;display:flex;flex-direction:column;align-items:center;text-align:center;padding:0 12px;border-right:2px solid #D5DCE4}}
.ii:last-child{{border-right:none}}
.ii .c{{width:84px;height:84px;border-radius:50%;background:{CH};color:#fff;display:flex;align-items:center;justify-content:center;border:4px solid {OR}}}
.ii h4{{font-size:25px;font-weight:900;color:{CH};margin-top:12px}} .ii p{{font-size:20px;font-weight:600;color:#555;margin-top:6px;line-height:1.3}}
.card{{display:flex;align-items:center;gap:14px;background:#fff;border-radius:18px;padding:9px 18px;margin-bottom:11px;width:470px;box-shadow:0 8px 18px rgba(0,0,0,.12)}}
.card .c{{width:54px;height:54px;flex:none;border-radius:50%;background:{OR};color:#fff;display:flex;align-items:center;justify-content:center}}
.card b{{display:block;font-size:27px;font-weight:900;color:{OR};line-height:1.05}} .card span{{font-size:20px;font-weight:700;color:{CH}}}
.script{{position:absolute;left:44px;top:1080px;font-family:'Dancing Script','Pacifico','Brush Script MT',cursive;font-style:italic;font-weight:700;font-size:58px;color:#fff;
text-shadow:3px 3px 0 {CH},-1px -1px 0 {CH},1px -1px 0 {CH},-1px 1px 0 {CH};display:flex;align-items:center;gap:14px}}
.script:after{{content:'';position:absolute;left:10px;bottom:-12px;width:420px;height:6px;border-radius:3px;background:linear-gradient(90deg,{OR},rgba(242,126,41,0))}}
.foot{{position:absolute;left:0;right:0;bottom:0;height:190px}}
.ct{{position:absolute;bottom:26px;left:36px;display:flex;align-items:center;gap:18px;color:#fff}}
.ct .it{{display:flex;align-items:center;gap:12px}} .ct .ci{{width:54px;height:54px;border-radius:50%;background:{OR};display:flex;align-items:center;justify-content:center;flex:none}}
.ct .tx{{font-size:17px;font-weight:600;color:#DDD;line-height:1.3}} .ct .tx b{{display:block;font-size:27px;color:#fff;font-weight:900}}
.ct .sep{{width:2px;height:60px;background:rgba(255,255,255,.3)}}
"""

def clouds():
    return ("<div class='cloud' style='left:520px;top:120px;width:260px;height:70px'></div>"
            "<div class='cloud' style='left:760px;top:220px;width:200px;height:56px'></div>"
            "<div class='cloud' style='left:80px;top:150px;width:160px;height:44px;opacity:.5'></div>")

def skyline(route):
    """Line-art 2 đầu tuyến: Sài Gòn (Landmark 81 + Bến Thành) ↔ Seoul / Sydney."""
    s = "stroke='#fff' stroke-width='2.2' fill='none' stroke-linejoin='round' opacity='.85'"
    sg = (f"<path {s} d='M10 120V70h40v50M20 70V58h20v12M24 58l6-10 6 10'/>"  # Bến Thành
          f"<path {s} d='M70 120V30l10-28 10 28v90M74 50h12M74 70h12M74 90h12'/>")  # Landmark 81
    if route == "uc":
        dst = (f"<path {s} d='M250 120c4-30 14-46 24-52 2 18-2 34-8 52M268 120c6-34 18-54 32-60 2 22-4 42-12 60M290 120c8-30 20-46 34-50 0 20-6 36-14 50'/>"
               f"<path {s} d='M340 120c10-40 50-40 60 0M346 120V96M394 120V96M330 104h80'/>")
    else:
        dst = (f"<path {s} d='M270 120V60h6V30h-12v-6h24v6h-12M282 60h-12M276 24V6'/>"  # N Seoul Tower
               f"<path {s} d='M340 120V40q10-40 20 0v80M346 60h8M346 80h8'/>")  # Lotte Tower
    pl = "<path d='M170 50l26-8-6 6 12 2-4 4-10-1-8 8-3-1 4-8z' fill='#F27E29'/><path d='M120 70q40-40 80-26' stroke='#F27E29' stroke-width='2' stroke-dasharray='5 4' fill='none'/>"
    return f"<svg viewBox='0 0 420 125' width='420' class='abs' style='right:24px;bottom:22px'>{sg}{pl}{dst}</svg>"

def footer(route):
    return f"""<div class='foot'><svg viewBox='0 0 1080 190' width='1080' height='190' class='abs' style='left:0;top:0'>
<path d='M0 60 Q540 -10 1080 40 V190 H0Z' fill='{CH}'/><path d='M0 60 Q540 -10 1080 40' stroke='{OR}' stroke-width='8' fill='none'/></svg>
<div class='ct'><div class='it'><div class='ci'>{ic('phone',28)}</div><div class='tx'>Zalo/WhatsApp<b>0334 477 577</b></div></div>
<div class='sep'></div><div class='it'><div class='ci'>{ic('pin',28)}</div><div class='tx'>Kho: 191A Gò Dưa,<br>P. Tam Bình, Thủ Đức</div></div></div>
{skyline(route)}</div>"""

def page(body, route):
    return (f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>{clouds()}"
            f"<div class='lgbox'>{logo(size=96)}</div>{body}"
            f"<div class='script'>Biết hết trước khi hàng bay {ic('plane',48,'#fff')}</div>{footer(route)}</body></html>")

def phone_tracking():
    dots = "".join(f"<div style='display:flex;align-items:center;gap:12px;margin:14px 0'><div style='width:22px;height:22px;border-radius:50%;background:{c};flex:none'></div><div style='height:12px;width:{w}px;border-radius:6px;background:#D5DCE4'></div></div>"
                   for c, w in [(OR,150),(OR,120),(OR,170),('#C9D1DA',130)])
    return f"""<div class='abs' style='right:50px;top:445px;width:280px;height:420px;border-radius:44px;background:{CH};padding:18px;box-shadow:0 20px 40px rgba(0,0,0,.3);transform:rotate(6deg)'>
<div style='background:#fff;border-radius:30px;height:100%;padding:30px 24px'>
<div style='font-weight:900;font-size:24px;color:{CH}'>TRACKING</div>
<div style='font-weight:700;font-size:18px;color:#888;margin-top:6px'>🇻🇳 Việt Nam ➜ 🇰🇷 Hàn Quốc</div>
<div style='margin-top:24px'>{dots}</div>
<div style='margin-top:10px;display:flex;justify-content:center'>{ic('box',70,OR)}</div></div></div>"""

def poster_han_tracking():
    body = f"""<div class='rib'>{ic('plane',36,'#fff')}<span>GỬI HÀNG ĐI HÀN QUỐC</span></div>
<div class='big' style='font-size:112px'>75.000Đ<span style='font-size:70px'>/KG</span></div>
<div class='pill' style='top:445px;font-size:31px'>CÓ MÃ TRACKING TỚI TAY NGƯỜI NHẬN</div>
<div class='desc' style='top:545px;width:700px;font-size:25px;white-space:nowrap'>Giao <b>3–5 ngày</b> kể từ ngày bay.<br>Free pickup 30km HCM – Bình Dương – Đồng Nai.</div>
{phone_tracking()}
<div class='abs' style='left:60px;top:705px'>{bigbox(200)}</div>
<div class='icons' style='top:880px'>
<div class='ii'><div class='c'>{ic('pin',44)}</div><h4>MÃ TRACKING</h4><p>Theo dõi tới tay người nhận</p></div>
<div class='ii'><div class='c'>{ic('clock',44)}</div><h4>3–5 NGÀY</h4><p>Kể từ ngày bay</p></div>
<div class='ii'><div class='c'>{ic('truck',44)}</div><h4>FREE PICKUP</h4><p>Nhỏ lớn gì 90S cũng nhận</p></div></div>"""
    return page(body, "han")

def poster_uc_du_hoc():
    cards = [("box","135.000đ/kg","Tuyến Úc"),("truck","FREE PICKUP 30KM","Nhỏ lớn gì 90S cũng nhận"),
             ("clock","3–5 NGÀY","Kể từ ngày bay"),("pin","MÃ TRACKING","Theo dõi tới tay người nhận")]
    c = "".join(f"<div class='card'><div class='c'>{ic(i,36)}</div><div><b>{a}</b><span>{b}</span></div></div>" for i,a,b in cards)
    body = f"""<div class='rib'>{ic('plane',36,'#fff')}<span>HỎI ĐÁP TUYẾN ÚC</span></div>
<div class='big' style='font-size:84px;width:1000px'>SẮP SANG ÚC HỌC,<br>ĐỒ NHIỀU QUÁ?</div>
<div class='pill' style='top:470px'>GỬI THÙNG – 135.000Đ/KG</div>
<div class='desc' style='top:570px;width:1000px;font-size:26px'>Nhắn danh sách đồ, 90S kiểm tra món nào gửi được,<br>rồi <b>cân, đo, chụp hình báo giá</b>.</div>
<div class='abs' style='left:40px;top:688px'>{c}</div>
<div class='abs' style='right:40px;top:640px'>{bigbox(400)}</div>
<div class='abs' style='right:20px;top:950px'>{plane(420,-8,livery=False)}</div>"""
    return page(body, "uc")

def poster_uc_kho_long():
    body = f"""<div class='rib'>{ic('plane',36,'#fff')}<span>GỬI HÀNG ĐI ÚC</span></div>
<div class='big' style='font-size:100px'>HÀNG KHÔ –<br>CHẤT LỎNG</div>
<div class='pill' style='top:500px;font-size:32px'>TÁCH RIÊNG TRƯỚC KHI ĐÓNG THÙNG</div>
<div class='desc' style='top:600px;width:620px'>Úc kiểm soát thực phẩm rất chặt.<br>Nhắn danh sách đồ để <b>90S kiểm tra trước</b>.</div>
<div class='abs' style='right:30px;top:250px'>{plane(380,-14,livery=False)}</div>
<div class='abs' style='right:50px;top:520px'>{bigbox(330)}</div>
<div class='icons' style='top:860px'>
<div class='ii'><div class='c'>{ic('chat',44)}</div><h4>KIỂM TRA</h4><p>Nhắn danh sách, 90S xem trước</p></div>
<div class='ii'><div class='c'>{ic('box',44)}</div><h4>PHÂN LOẠI</h4><p>Tách hàng khô, chất lỏng</p></div>
<div class='ii'><div class='c'>{ic('scale',44)}</div><h4>ĐÓNG THÙNG</h4><p>Hút chân không, cân, đo, chụp hình</p></div></div>"""
    return page(body, "uc")

def checklist():
    rows = "".join(f"<div style='display:flex;align-items:center;gap:12px;margin:16px 0'><div style='width:26px;height:26px;border-radius:6px;border:3px solid {OR};flex:none;display:flex;align-items:center;justify-content:center;color:{OR};font-weight:900;font-size:20px'>✓</div><div style='height:12px;width:{w}px;border-radius:6px;background:#D5DCE4'></div></div>"
                   for w in (150, 120, 170, 135))
    return f"""<div class='abs' style='right:70px;top:430px;width:270px;padding:26px 24px;background:#fffdf6;border-radius:14px;box-shadow:0 18px 36px rgba(0,0,0,.25);transform:rotate(5deg)'>
<div style='font-weight:900;font-size:24px;color:{CH}'>DANH SÁCH ĐỒ</div>{rows}</div>"""

def poster_han_chuan_bi():
    body = f"""<div class='rib'>{ic('plane',36,'#fff')}<span>GỬI ĐỒ SANG HÀN QUỐC</span></div>
<div class='big' style='font-size:104px'>CHUẨN BỊ<br>3 THỨ</div>
<div class='pill' style='top:500px'>TRƯỚC KHI NHẮN 90S</div>
<div class='desc' style='top:600px;width:600px'>Có danh sách sớm – 90S <b>kiểm tra,<br>phân loại</b> trước khi đóng thùng.</div>
{checklist()}
<div class='abs' style='right:60px;top:660px'>{bigbox(240)}</div>
<div class='icons' style='top:850px'>
<div class='ii'><div class='c'>{ic('doc',44)}</div><h4>DANH SÁCH ĐỒ</h4><p>Nhắn 90S kiểm tra trước</p></div>
<div class='ii'><div class='c'>{ic('box',44)}</div><h4>CHẤT LỎNG ĐỂ RIÊNG</h4><p>Phân loại hàng khô – lỏng</p></div>
<div class='ii'><div class='c'>{ic('pin',44)}</div><h4>ĐỊA CHỈ LẤY HÀNG</h4><p>Free pickup 30km hoặc gửi chành xe</p></div></div>"""
    return page(body, "han")

def van():
    return f"""<svg viewBox='0 0 420 220' width='420' class='abs' style='right:40px;top:760px'>
<rect x='10' y='40' width='250' height='140' rx='14' fill='#fff' stroke='{CH}' stroke-width='5'/>
<path d='M260 80h80l60 55v45H260z' fill='{OR}' stroke='{CH}' stroke-width='5' stroke-linejoin='round'/>
<path d='M285 95h50l35 35h-85z' fill='#CFE8FA'/><rect x='10' y='150' width='250' height='14' fill='{OR}'/>
<circle cx='80' cy='185' r='28' fill='{CH}'/><circle cx='80' cy='185' r='11' fill='#ddd'/>
<circle cx='330' cy='185' r='28' fill='{CH}'/><circle cx='330' cy='185' r='11' fill='#ddd'/>
<text x='135' y='115' text-anchor='middle' font-family='Montserrat' font-weight='900' font-size='38' fill='{CH}'>FREE</text>
<text x='135' y='142' text-anchor='middle' font-family='Montserrat' font-weight='800' font-size='22' fill='{OR}'>PICKUP 30KM</text></svg>"""

def poster_uc_pickup():
    cards = [("box","135.000đ/kg","Gửi hàng đi Úc"),("truck","FREE PICKUP 30KM","HCM – Bình Dương – Đồng Nai"),
             ("scale","NHỎ LỚN ĐỀU NHẬN","Cân, đo, chụp hình báo giá"),("clock","3–5 NGÀY","Kể từ ngày bay")]
    c = "".join(f"<div class='card'><div class='c'>{ic(i,36)}</div><div><b>{a}</b><span>{b}</span></div></div>" for i,a,b in cards)
    body = f"""<div class='rib'>{ic('plane',36,'#fff')}<span>GỬI HÀNG ĐI ÚC</span></div>
<div class='big' style='font-size:96px'>90S TỚI TẬN<br>NHÀ LẤY HÀNG</div>
<div class='pill' style='top:490px'>135.000Đ/KG – FREE PICKUP</div>
<div class='desc' style='top:590px;width:1000px;font-size:26px'>Bán kính 30km TP.HCM – Bình Dương – Đồng Nai.<br>Hàng nhỏ hay lớn, <b>90S đều nhận</b>.</div>
<div class='abs' style='left:40px;top:705px'>{c}</div>
{van()}
<div class='abs' style='right:230px;top:705px'>{bigbox(150)}</div>"""
    return page(body, "uc")

def route_map():
    return f"""<svg viewBox='0 0 440 330' width='440' class='abs' style='right:30px;top:470px'>
<circle cx='220' cy='165' r='160' fill='rgba(255,255,255,.55)'/>
<path d='M90 250 Q200 40 350 90' stroke='{OR}' stroke-width='5' stroke-dasharray='12 9' fill='none'/>
<circle cx='90' cy='250' r='16' fill='{CH}'/><circle cx='350' cy='90' r='16' fill='{OR}'/>
<text x='90' y='295' text-anchor='middle' font-family='Montserrat' font-weight='900' font-size='26' fill='{CH}'>🇻🇳 TP.HCM</text>
<text x='300' y='50' text-anchor='middle' font-family='Montserrat' font-weight='900' font-size='26' fill='{CH}'>🇰🇷 HÀN QUỐC</text>
<g transform='translate(215 115) rotate(35)'><path d='M21 15.5v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V8.5l-8 5v2l8-2.5V18l-2 1.5V21l3.5-1 3.5 1v-1.5L13 18v-5z' fill='{CH}' transform='scale(2.6) translate(-12 -12)'/></g></svg>"""

def poster_han_may_ngay():
    body = f"""<div class='rib'>{ic('plane',36,'#fff')}<span>HỎI ĐÁP TUYẾN HÀN</span></div>
<div class='big' style='font-size:92px'>GỬI ĐI HÀN<br>MẤT MẤY NGÀY?</div>
<div class='pill' style='top:490px'>3–5 NGÀY KỂ TỪ NGÀY BAY</div>
<div class='desc' style='top:590px;width:560px'>Hỏi 90S ngày bay gần nhất<br>để biết hàng <b>tới tay khi nào</b>.</div>
{route_map()}
<div class='icons' style='top:860px'>
<div class='ii'><div class='c'>{ic('box',44)}</div><h4>ĐÓNG THÙNG</h4><p>Cân, đo, chụp hình báo giá</p></div>
<div class='ii'><div class='c'>{ic('plane',44)}</div><h4>ĐỢI NGÀY BAY</h4><p>Nhắn 90S hỏi ngày bay</p></div>
<div class='ii'><div class='c'>{ic('pin',44)}</div><h4>MÃ TRACKING</h4><p>Theo dõi tới tay người nhận</p></div></div>"""
    return page(body, "han")

def route_map_uc():
    return f"""<svg viewBox='0 0 440 330' width='400' class='abs' style='right:30px;top:500px'>
<circle cx='220' cy='165' r='160' fill='rgba(255,255,255,.55)'/>
<path d='M110 70 Q330 90 330 250' stroke='{OR}' stroke-width='5' stroke-dasharray='12 9' fill='none'/>
<circle cx='110' cy='70' r='16' fill='{CH}'/><circle cx='330' cy='250' r='16' fill='{OR}'/>
<text x='120' y='40' text-anchor='middle' font-family='Montserrat' font-weight='900' font-size='26' fill='{CH}'>🇻🇳 TP.HCM</text>
<text x='300' y='300' text-anchor='middle' font-family='Montserrat' font-weight='900' font-size='26' fill='{CH}'>🇦🇺 ÚC</text>
<g transform='translate(290 140) rotate(150)'><path d='M21 15.5v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V8.5l-8 5v2l8-2.5V18l-2 1.5V21l3.5-1 3.5 1v-1.5L13 18v-5z' fill='{CH}' transform='scale(2.6) translate(-12 -12)'/></g></svg>"""

def poster_uc_hoi_truoc():
    body = f"""<div class='rib'>{ic('plane',36,'#fff')}<span>GỬI ĐỒ SANG ÚC</span></div>
<div class='big' style='font-size:96px'>5 MÓN CẦN<br>HỎI TRƯỚC</div>
<div class='pill' style='top:490px;font-size:32px'>TRƯỚC KHI BỎ VÀO THÙNG</div>
<div class='desc' style='top:590px;width:560px;font-size:25px'>Úc kiểm soát thực phẩm rất chặt.<br>Nhắn danh sách đồ, <b>90S kiểm tra<br>trước khi đóng thùng</b>.</div>
{route_map_uc()}
<div class='abs' style='right:20px;top:250px'>{plane(330,-12,livery=False)}</div>
<div class='icons' style='top:830px'>
<div class='ii'><div class='c'>{ic('box',44)}</div><h4>GẠO – LÁ CHUỐI</h4><p>Hỏi 90S trước khi gửi</p></div>
<div class='ii'><div class='c'>{ic('box',44)}</div><h4>MĂNG TƯƠI</h4><p>Hỏi 90S trước khi gửi</p></div>
<div class='ii'><div class='c'>{ic('box',44)}</div><h4>LINH CHI –<br>ĐÔNG TRÙNG</h4><p>Thảo dược có nấm</p></div></div>"""
    return page(body, "uc")

def poster_han_bao_gia():
    cards = [("box","75.000đ/kg","Gửi hàng đi Hàn Quốc"),("scale","CÂN – ĐO – CHỤP HÌNH","Báo giá trước khi chốt"),
             ("truck","FREE PICKUP 30KM","Nhỏ lớn gì 90S cũng nhận"),("clock","3–5 NGÀY","Kể từ ngày bay")]
    c = "".join(f"<div class='card'><div class='c'>{ic(i,36)}</div><div><b>{a}</b><span>{b}</span></div></div>" for i,a,b in cards)
    body = f"""<div class='rib'>{ic('plane',36,'#fff')}<span>GỬI HÀNG ĐI HÀN QUỐC</span></div>
<div class='big' style='font-size:92px'>BIẾT GIÁ<br>TRƯỚC KHI BAY</div>
<div class='pill' style='top:490px'>HÀN QUỐC 75.000Đ/KG</div>
<div class='desc' style='top:590px;width:1000px;font-size:26px'>90S cân kg, đo kích thước, chụp hình thùng hàng<br>gửi bạn xem <b>rồi mới chốt giá</b>.</div>
<div class='abs' style='left:40px;top:705px'>{c}</div>
<div class='abs' style='right:40px;top:690px'>{bigbox(400)}</div>"""
    return page(body, "han")

def poster_uc_toi_dau():
    body = f"""<div class='rib'>{ic('plane',36,'#fff')}<span>HỎI ĐÁP TUYẾN ÚC</span></div>
<div class='big' style='font-size:88px'>THÙNG HÀNG<br>ĐANG TỚI ĐÂU?</div>
<div class='pill' style='top:490px;font-size:32px'>CÓ MÃ TRACKING TỚI TAY</div>
<div class='desc' style='top:590px;width:600px'>Hàng bay rồi, người nhà ở Úc<br>theo dõi bằng <b>mã tracking tới tận tay</b>.</div>
{phone_tracking().replace('🇰🇷 Hàn Quốc','🇦🇺 Úc').replace('top:445px','top:470px')}
<div class='icons' style='top:870px'>
<div class='ii'><div class='c'>{ic('box',44)}</div><h4>ĐÓNG THÙNG</h4><p>Cân, đo, chụp hình báo giá</p></div>
<div class='ii'><div class='c'>{ic('clock',44)}</div><h4>3–5 NGÀY</h4><p>Kể từ ngày bay</p></div>
<div class='ii'><div class='c'>{ic('pin',44)}</div><h4>MÃ TRACKING</h4><p>Theo dõi tới tay người nhận</p></div></div>"""
    return page(body, "uc")

POSTERS = {"uc_hoi_truoc": poster_uc_hoi_truoc, "han_bao_gia": poster_han_bao_gia, "uc_toi_dau": poster_uc_toi_dau,
           "han_tracking": poster_han_tracking, "uc_du_hoc": poster_uc_du_hoc, "uc_kho_long": poster_uc_kho_long,
           "han_chuan_bi": poster_han_chuan_bi, "uc_pickup": poster_uc_pickup, "han_may_ngay": poster_han_may_ngay}

async def main(key, out):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        f = pathlib.Path(out).with_suffix(".html"); f.write_text(POSTERS[key](), encoding="utf-8")
        await pg.goto(f.resolve().as_uri()); await pg.wait_for_timeout(500)
        await pg.screenshot(path=out, type="jpeg", quality=92); await b.close(); f.unlink()

if __name__ == "__main__":
    asyncio.run(main(sys.argv[1], sys.argv[2]))
