"""Bộ poster 90S Cargo phong cách 2 – học từ các mẫu logistics (TCG, ShipMore, Axis, ForwardAir).
Kỹ thuật dùng: headline chữ đặc cao (Anton) 2 màu, 1 chữ nổi bật trong khối màu, vật thể trung tâm
(thùng hàng có logo), hàng 4 icon cam kết có vạch ngăn, sóng/swoosh cam, thanh liên hệ navy, nút CTA."""
import asyncio, pathlib, sys
from playwright.async_api import async_playwright

OUT = pathlib.Path(__file__).resolve().parent / "posters2"; OUT.mkdir(exist_ok=True)
NAVY, NAVY2, OR1, OR2, YEL = "#0D2B5E", "#14408A", "#FF8A1F", "#F05A0F", "#FFE55C"
PHONE = "0334 477 577"

ICON = {
 "shield": "<path d='M12 2 4 5v6c0 5 3.4 9.4 8 11 4.6-1.6 8-6 8-11V5z' fill='none' stroke='currentColor' stroke-width='2'/><path d='M8.5 12l2.5 2.5 4.5-5' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round'/>",
 "clock": "<circle cx='13' cy='12' r='8' fill='none' stroke='currentColor' stroke-width='2'/><path d='M13 8v4l3 2M2 9h3M1 12h3M2 15h3' fill='none' stroke='currentColor' stroke-width='2' stroke-linecap='round'/>",
 "globe": "<circle cx='12' cy='12' r='9' fill='none' stroke='currentColor' stroke-width='2'/><path d='M3 12h18M12 3c3 3 3 15 0 18M12 3c-3 3-3 15 0 18' fill='none' stroke='currentColor' stroke-width='1.8'/>",
 "head": "<path d='M4 14v-2a8 8 0 0 1 16 0v2' fill='none' stroke='currentColor' stroke-width='2'/><rect x='3' y='13' width='4' height='6' rx='1.5' fill='currentColor'/><rect x='17' y='13' width='4' height='6' rx='1.5' fill='currentColor'/><path d='M19 19c0 2-2 3-5 3' fill='none' stroke='currentColor' stroke-width='2'/>",
 "plane": "<path d='M21 15.5v-2l-8-5V3.5a1.5 1.5 0 0 0-3 0V8.5l-8 5v2l8-2.5V18l-2 1.5V21l3.5-1 3.5 1v-1.5L13 18v-5z' fill='currentColor'/>",
 "truck": "<path d='M1 6h13v9H1zM14 9h4.5l3.5 3.5V15h-8z' fill='none' stroke='currentColor' stroke-width='2' stroke-linejoin='round'/><circle cx='5.5' cy='17' r='2' fill='currentColor'/><circle cx='17.5' cy='17' r='2' fill='currentColor'/>",
 "box": "<path d='M12 2 3 6.5v11L12 22l9-4.5v-11z M3 6.5 12 11l9-4.5 M12 11v11' fill='none' stroke='currentColor' stroke-width='2' stroke-linejoin='round'/>",
 "scale": "<path d='M12 3v18M6 21h12M4 8h16M4 8l-3 6a3 3 0 0 0 6 0zM20 8l-3 6a3 3 0 0 0 6 0z' fill='none' stroke='currentColor' stroke-width='2' stroke-linejoin='round'/>",
 "pin": "<path d='M12 2a7 7 0 0 0-7 7c0 5 7 13 7 13s7-8 7-13a7 7 0 0 0-7-7z' fill='none' stroke='currentColor' stroke-width='2'/><circle cx='12' cy='9' r='2.5' fill='currentColor'/>",
 "doc": "<path d='M6 2h9l5 5v15H6z M15 2v5h5 M9 12h8M9 16h8' fill='none' stroke='currentColor' stroke-width='2' stroke-linejoin='round'/>",
 "phone": "<path d='M6.6 10.8a15 15 0 0 0 6.6 6.6l2.2-2.2c.3-.3.7-.4 1-.2 1.1.4 2.3.6 3.6.6.6 0 1 .4 1 1V20c0 .6-.4 1-1 1A17 17 0 0 1 3 4c0-.6.4-1 1-1h3.5c.6 0 1 .4 1 1 0 1.3.2 2.5.6 3.6.1.3 0 .7-.2 1z' fill='currentColor'/>",
 "chat": "<path d='M4 4h16v12H8l-4 4z' fill='none' stroke='currentColor' stroke-width='2' stroke-linejoin='round'/><path d='M8 9h8M8 12h5' stroke='currentColor' stroke-width='2' stroke-linecap='round'/>",
 "arrow": "<path d='M5 12h13M13 6l6 6-6 6' fill='none' stroke='currentColor' stroke-width='2.6' stroke-linecap='round' stroke-linejoin='round'/>",
}
def ic(n, s=40, c="currentColor"):
    return f"<svg viewBox='0 0 24 24' width='{s}' height='{s}' style='color:{c}'>{ICON[n]}</svg>"

def logo(dark=False, size=96):
    txt = "#fff" if dark else NAVY
    return f"""<div class='logo'><div class='lc' style='width:{size}px;height:{size}px'><b style='font-size:{size*.38}px'>90S</b><i style='font-size:{size*.14}px'>CARGO</i></div>
<div class='lt'><b style='color:{txt}'>90S CARGO EXPRESS</b><span>VẬN CHUYỂN QUỐC TẾ</span></div></div>"""

def plane(w=460, rot=-10, livery=True):
    return f"""<svg viewBox='0 0 520 200' width='{w}' style='transform:rotate({rot}deg)'>
<defs><linearGradient id='fz{w}' x1='0' y1='0' x2='0' y2='1'><stop offset='0' stop-color='#fff'/><stop offset='.7' stop-color='#E7ECF4'/><stop offset='1' stop-color='#AEBBCD'/></linearGradient>
<linearGradient id='tl{w}' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='{OR1}'/><stop offset='1' stop-color='{OR2}'/></linearGradient></defs>
<path d='M300 110 L190 188 L228 188 L362 112 Z' fill='#C3CEDC'/>
<path d='M40 100 Q30 80 60 72 L430 66 Q500 68 510 92 Q500 118 430 120 L70 122 Q40 120 40 100Z' fill='url(#fz{w})'/>
<path d='M60 74 L18 6 L62 6 L132 72 Z' fill='url(#tl{w})'/><path d='M70 96 L18 92 L20 104 L72 108Z' fill='url(#tl{w})'/>
<path d='M300 92 L190 20 L228 20 L362 90 Z' fill='#D8E0EB'/>
<rect x='60' y='106' width='372' height='6' rx='3' fill='{NAVY}'/><rect x='60' y='112' width='372' height='4' rx='2' fill='{OR1}'/>
{"<text x='150' y='99' font-family='Montserrat' font-weight='900' font-style='italic' font-size='22' fill='"+NAVY+"'>90S CARGO</text>" if livery else ""}
<g fill='{NAVY}' opacity='.7'>{''.join(f"<rect x='{290+i*14}' y='80' width='8' height='9' rx='3'/>" for i in range(9))}</g>
<path d='M470 78 Q492 80 500 90 L472 90Z' fill='{NAVY}' opacity='.85'/>
<ellipse cx='272' cy='133' rx='36' ry='14' fill='#94A3B8'/><ellipse cx='246' cy='133' rx='9' ry='12' fill='#4B5B70'/>
</svg>"""

def bigbox(w=420):
    """Thùng carton 3D có logo 90S + ký hiệu hàng hóa – vật thể trung tâm."""
    h = w * .82; t = h * .26
    return f"""<svg viewBox='0 0 {w} {h}' width='{w}'>
<defs><linearGradient id='bf' x1='0' y1='0' x2='1' y2='1'><stop offset='0' stop-color='#DDA563'/><stop offset='1' stop-color='#C48443'/></linearGradient>
<linearGradient id='bs' x1='0' y1='0' x2='1' y2='0'><stop offset='0' stop-color='#AE6E31'/><stop offset='1' stop-color='#95592A'/></linearGradient></defs>
<path d='M0 {t} L{w*.64} {t} L{w*.64} {h} L0 {h}Z' fill='url(#bf)'/>
<path d='M{w*.64} {t} L{w} {t*.25} L{w} {h-t*.75} L{w*.64} {h}Z' fill='url(#bs)'/>
<path d='M0 {t} L{w*.36} {t*.25} L{w} {t*.25} L{w*.64} {t}Z' fill='#EAB878'/>
<path d='M{w*.28} {t} L{w*.6} {t*.25} L{w*.7} {t*.25} L{w*.38} {t}Z' fill='#C9B08C'/>
<rect x='{w*.28}' y='{t}' width='{w*.1}' height='{h*.3}' fill='#C9B08C'/>
<circle cx='{w*.2}' cy='{t+(h-t)*.55}' r='{w*.09}' fill='{OR1}'/>
<text x='{w*.2}' y='{t+(h-t)*.55+w*.03}' text-anchor='middle' font-family='Montserrat' font-weight='900' font-style='italic' font-size='{w*.075}' fill='#fff'>90S</text>
<text x='{w*.31}' y='{t+(h-t)*.52}' font-family='Montserrat' font-weight='900' font-style='italic' font-size='{w*.06}' fill='{NAVY}'>CARGO</text>
<text x='{w*.31}' y='{t+(h-t)*.52+w*.05}' font-family='Montserrat' font-weight='800' font-size='{w*.035}' fill='{OR2}'>EXPRESS</text>
<g stroke='{NAVY}' stroke-width='2' fill='none' opacity='.75' transform='translate({w*.4},{h*.8})'>
<rect x='0' y='0' width='{w*.06}' height='{w*.06}'/><path d='M{w*.015} {w*.045}V{w*.015}M{w*.045} {w*.045}V{w*.015}M{w*.008} {w*.025}l{w*.007} -{w*.01} {w*.007} {w*.01}M{w*.038} {w*.025}l{w*.007} -{w*.01} {w*.007} {w*.01}'/>
<rect x='{w*.08}' y='0' width='{w*.06}' height='{w*.06}'/><path d='M{w*.09} {w*.03}q{w*.02} -{w*.025} {w*.04} 0zM{w*.11} {w*.03}v{w*.022}'/>
</g></svg>"""

def globe(s=520, op=.9):
    lines = "".join(f"<ellipse cx='100' cy='100' rx='{r}' ry='96' fill='none' stroke='#9FD0FF' stroke-width='.8'/>" for r in (20,45,70,90))
    lat = "".join(f"<line x1='{100-((96**2-(y-100)**2)**.5)}' y1='{y}' x2='{100+((96**2-(y-100)**2)**.5)}' y2='{y}' stroke='#9FD0FF' stroke-width='.8'/>" for y in (30,55,80,100,120,145,170))
    dots = "".join(f"<circle cx='{x}' cy='{y}' r='1.6' fill='#CFE8FF'/>" for x,y in [(60,60),(72,70),(80,58),(130,65),(140,80),(120,120),(60,130),(150,140),(95,90),(110,50)])
    return f"""<svg viewBox='0 0 200 200' width='{s}' style='opacity:{op}'><defs><radialGradient id='gg' cx='.35' cy='.3'><stop offset='0' stop-color='#4FA3F0'/><stop offset='.6' stop-color='#1A5BB8'/><stop offset='1' stop-color='#0B2F6B'/></radialGradient></defs>
<circle cx='100' cy='100' r='96' fill='url(#gg)'/>{lines}{lat}{dots}
<path d='M45 75 Q100 20 160 70' fill='none' stroke='#FFD27A' stroke-width='1.6' stroke-dasharray='4 3'/><circle cx='45' cy='75' r='3.5' fill='{OR1}'/><circle cx='160' cy='70' r='3.5' fill='{OR1}'/>
<circle cx='100' cy='100' r='96' fill='none' stroke='#BFE0FF' stroke-width='2'/></svg>"""

BASE = f"""*{{margin:0;padding:0;box-sizing:border-box}}
body{{width:1080px;height:1350px;overflow:hidden;position:relative;font-family:'Montserrat','Noto Color Emoji',sans-serif}}
.A{{font-family:'Anton','Montserrat',sans-serif;font-weight:400;letter-spacing:.5px}}
.logo{{display:flex;align-items:center;gap:14px}}
.lc{{border-radius:50%;background:radial-gradient(circle at 35% 30%,#FFB057,{OR1} 45%,{OR2});display:flex;flex-direction:column;align-items:center;justify-content:center;color:#fff;font-weight:900;font-style:italic;border:4px solid #fff;box-shadow:0 6px 16px rgba(240,90,15,.4)}}
.lc b{{line-height:.9}} .lc i{{letter-spacing:1px}}
.lt b{{display:block;font-size:30px;font-weight:900;font-style:italic;line-height:1}}
.lt span{{display:block;font-size:15px;font-weight:800;color:{OR2};letter-spacing:3px;margin-top:6px}}
.abs{{position:absolute}}
.bar{{position:absolute;left:0;right:0;bottom:0;height:120px;background:{NAVY};display:flex;align-items:center;justify-content:space-around;padding:0 30px;color:#fff}}
.bar .it{{display:flex;align-items:center;gap:14px}}
.bar .ci{{width:56px;height:56px;border-radius:50%;background:{OR1};display:flex;align-items:center;justify-content:center;color:#fff;flex:none}}
.bar .tx{{font-size:17px;font-weight:600;line-height:1.3;color:#C9D6EC}} .bar .tx b{{display:block;font-size:30px;color:#fff;font-weight:900}}
.icons4{{display:flex;justify-content:space-between}}
.i4{{flex:1;display:flex;align-items:center;gap:12px;padding:0 14px;border-right:2px solid rgba(255,255,255,.18)}}
.i4:last-child{{border-right:none}}
.i4 h4{{font-size:20px;font-weight:900;letter-spacing:.5px}} .i4 p{{font-size:16px;font-weight:600;line-height:1.3;margin-top:3px}}
"""

def bar():
    return f"""<div class='bar'>
<div class='it'><div class='ci'>{ic('phone',28)}</div><div class='tx'>Zalo / WhatsApp<b>{PHONE}</b></div></div>
<div class='it'><div class='ci'>{ic('pin',28)}</div><div class='tx'>Kho: 191A Gò Dưa, P. Tam Bình<br>VP: 585/12/18 QL13, P. Hiệp Bình, Thủ Đức</div></div></div>"""

def html(body, css): return f"<html><head><meta charset='utf-8'><style>{BASE}{css}</style></head><body>{body}</body></html>"

# ---------- A: Clean corporate (học TCG) ----------
def poster_A():
    css = f"""body{{background:linear-gradient(180deg,#fff 0%,#F3F7FC 55%,#E6EEF8 100%)}}
.map{{position:absolute;left:-60px;top:240px;opacity:.12}}
.h{{position:absolute;left:56px;top:190px;line-height:1.02}}
.h .l1{{font-size:78px;color:{NAVY}}} .h .l2{{font-size:96px;color:{OR2}}}
.tag{{position:absolute;left:56px;top:430px;background:{NAVY};color:#fff;font-weight:900;font-size:27px;padding:12px 70px 12px 24px;clip-path:polygon(0 0,100% 0,92% 100%,0 100%)}}
.tag:after{{content:'';}}
.lead{{position:absolute;left:56px;top:510px;width:520px;font-size:24px;line-height:1.5;color:#33435C;font-weight:500}} .lead b{{color:{OR2}}}
.sec{{position:absolute;background:{NAVY};color:#fff;font-weight:900;font-size:25px;padding:9px 56px 9px 20px;clip-path:polygon(0 0,100% 0,90% 100%,0 100%)}}
.svc{{position:absolute;left:56px;top:735px;width:500px;display:flex;flex-direction:column;gap:20px}}
.sv{{display:flex;gap:16px;align-items:center}} .sv .b{{width:64px;height:64px;border:3px solid {NAVY};border-radius:12px;display:flex;align-items:center;justify-content:center;color:{OR2};flex:none;background:#fff}}
.sv h5{{font-size:23px;font-weight:900;color:{OR2}}} .sv p{{font-size:19px;color:#33435C;font-weight:600;margin-top:2px}}
.why{{position:absolute;right:40px;top:760px;width:470px;background:#fff;border-radius:22px;box-shadow:0 12px 30px rgba(13,43,94,.12);display:grid;grid-template-columns:1fr 1fr;padding:22px 10px}}
.w{{text-align:center;padding:12px 10px;color:{NAVY}}} .w h6{{font-size:21px;font-weight:900;color:{NAVY};margin-top:6px}} .w p{{font-size:16px;color:#4A5A72;font-weight:600;line-height:1.3;margin-top:4px}}
.flags{{position:absolute;left:56px;right:40px;top:1140px;display:flex;gap:26px;align-items:center}}
.fl{{text-align:center;font-weight:900;font-size:17px;color:{NAVY}}} .fl div{{font-size:66px;line-height:1.05}}
.fl.more{{color:{OR2};font-size:16px;text-align:left;line-height:1.3;max-width:260px}}
"""
    body = f"""<div class='abs' style='top:40px;left:56px'>{logo()}</div>
<div class='abs' style='right:-90px;top:200px'>{globe(560)}</div>
<div class='abs' style='right:40px;top:40px'>{plane(520,-14)}</div>
<div class='abs' style='right:40px;top:400px'>{bigbox(340)}</div>
<div class='h A'><div class='l1'>VẬN CHUYỂN QUỐC TẾ</div><div class='l2'>GỬI HÀNG HÀN – ÚC</div></div>
<div class='tag'>NHANH CHÓNG – AN TOÀN – TIẾT KIỆM</div>
<div class='lead'><b>90S Cargo Express</b> – nhận hàng tận nơi, đóng gói kỹ, khai báo hải quan trọn gói. Một thùng hàng, tới tận tay người thân.</div>
<div class='sec' style='left:56px;top:680px'>DỊCH VỤ CỦA CHÚNG TÔI</div>
<div class='svc'>
<div class='sv'><div class='b'>{ic('plane',36)}</div><div><h5>CHUYÊN TUYẾN HÀN QUỐC</h5><p>Chỉ 75K/kg cho đơn từ 21kg</p></div></div>
<div class='sv'><div class='b'>{ic('plane',36)}</div><div><h5>GỬI HÀNG ĐI ÚC</h5><p>Chỉ 135K/kg cho đơn từ 21kg</p></div></div>
<div class='sv'><div class='b'>{ic('doc',34)}</div><div><h5>KHAI BÁO & THÔNG QUAN</h5><p>Hàng cá nhân và doanh nghiệp</p></div></div>
<div class='sv'><div class='b'>{ic('truck',36)}</div><div><h5>GOM HÀNG ĐẠI LÝ</h5><p>Free pickup 30km cho đơn từ 20kg</p></div></div>
</div>
<div class='sec' style='right:200px;top:705px'>VÌ SAO CHỌN 90S?</div>
<div class='why'>
<div class='w'>{ic('clock',46,OR2)}<h6>NHANH</h6><p>3–5 ngày kể từ ngày bay</p></div>
<div class='w'>{ic('scale',46,OR2)}<h6>MINH BẠCH</h6><p>Cân, đo, chụp hình báo giá</p></div>
<div class='w'>{ic('box',46,OR2)}<h6>ĐÓNG GÓI KỸ</h6><p>Hút chân không, thùng chắc</p></div>
<div class='w'>{ic('pin',46,OR2)}<h6>THEO DÕI</h6><p>Mã tracking tới tận tay</p></div>
</div>
<div class='sec' style='left:56px;top:1085px'>TUYẾN NỔI BẬT</div>
<div class='flags'><div class='fl'><div>🇻🇳</div>VIỆT NAM</div><div class='fl' style='font-size:40px;color:{OR2}'>✈</div>
<div class='fl'><div>🇰🇷</div>HÀN QUỐC</div><div class='fl'><div>🇦🇺</div>ÚC</div>
<div class='fl more'>Tuyến khác?<br><span style='color:{NAVY}'>Nhắn page để được báo giá</span></div></div>
{bar()}"""
    return html(body, css)

# ---------- B: Dramatic sunset + 3D headline (học ShipMore) ----------
def poster_B():
    css = f"""body{{background:linear-gradient(180deg,#0A1E45 0%,#1D3F7A 30%,#C9622A 62%,#F7A24B 74%,#1A2236 100%)}}
.glow{{position:absolute;left:640px;top:690px;width:520px;height:520px;border-radius:50%;background:radial-gradient(circle,#FFE3A6 0%,rgba(255,160,70,.55) 35%,rgba(255,120,40,0) 70%)}}
.pill{{position:absolute;top:140px;left:50%;transform:translateX(-50%);background:linear-gradient(90deg,{OR2},{OR1});color:#fff;font-weight:900;font-size:26px;padding:10px 34px;border-radius:12px;white-space:nowrap;box-shadow:0 8px 20px rgba(0,0,0,.3)}}
.t1{{position:absolute;top:225px;left:0;right:0;text-align:center;font-size:150px;color:#fff;line-height:1;text-shadow:0 6px 0 #B9C6DB,0 12px 24px rgba(0,0,0,.4)}}
.t2{{position:absolute;top:395px;left:0;right:0;text-align:center;font-size:190px;line-height:1;color:{OR1};
text-shadow:0 2px 0 #E06A10,0 4px 0 #D2600C,0 6px 0 #C4560A,0 8px 0 #B44C08,0 10px 0 #A04306,0 18px 30px rgba(0,0,0,.5)}}
.t3{{position:absolute;top:610px;left:0;right:0;text-align:center;font-size:27px;white-space:nowrap;font-weight:900;color:#fff;letter-spacing:1px}}
.t3 b{{color:{YEL}}}
.city{{position:absolute;left:0;right:0;top:820px;height:240px}}
.road{{position:absolute;left:-100px;right:-100px;top:1000px;height:120px;background:#2A3346;border-radius:50% 50% 0 0/100% 100% 0 0;border-top:6px solid #FFC56B}}
.icons{{position:absolute;left:30px;right:30px;top:1070px;color:#fff}}
.icons .i4 svg{{color:{OR1};flex:none}}
.cta{{position:absolute;left:56px;right:56px;bottom:34px;height:110px;display:flex;align-items:center;justify-content:space-between}}
.cta .s{{white-space:nowrap;color:{OR1};font-size:38px;font-style:italic}} .cta .s small{{display:block;font-family:Montserrat;font-size:17px;color:#fff;font-style:normal;font-weight:700;letter-spacing:1px}}
.btn{{white-space:nowrap;background:linear-gradient(180deg,{OR1},{OR2});color:#fff;font-weight:900;font-size:26px;border-radius:14px;padding:16px 22px;display:flex;align-items:center;gap:10px;box-shadow:0 8px 20px rgba(240,90,15,.5)}}
.ph{{white-space:nowrap;color:#fff;font-weight:900;font-size:30px;display:flex;align-items:center;gap:10px}}
"""
    bld = "".join(f"<rect x='{x}' y='{240-h}' width='{w}' height='{h}' fill='#14213D' opacity='.9'/>" for x,w,h in
                  [(0,60,120),(70,40,170),(120,70,110),(200,36,200),(246,60,140),(820,50,150),(880,40,210),(930,70,120),(1010,60,170)])
    body = f"""<div class='glow'></div>
<div class='abs' style='top:36px;left:40px'>{logo(dark=True,size=88)}</div>
<div class='pill'>GỬI HÀNG ĐI HÀN QUỐC</div>
<div class='t1 A'>GỬI NHIỀU</div><div class='t2 A'>TIẾT KIỆM</div>
<div class='t3'>CHỈ <b>75K/KG</b> CHO ĐƠN TỪ 21KG · TỚI TAY SAU 3–5 NGÀY BAY</div>
<div class='abs' style='left:-60px;top:690px'>{plane(300,-8)}</div>
<div class='abs' style='right:-60px;top:720px'>{plane(270,6,False)}</div>
<svg class='city' viewBox='0 0 1080 240' preserveAspectRatio='none'>{bld}</svg>
<div class='road'></div>
<div class='abs' style='left:50%;top:690px;transform:translateX(-50%)'>{bigbox(420)}</div>
<div class='icons icons4'>
<div class='i4'>{ic('shield',44)}<div><h4>ĐÓNG GÓI KỸ</h4><p>Hút chân không, thùng chắc</p></div></div>
<div class='i4'>{ic('clock',44)}<div><h4>3–5 NGÀY</h4><p>Kể từ ngày bay</p></div></div>
<div class='i4'>{ic('pin',44)}<div><h4>TRACKING</h4><p>Theo dõi tới tận tay</p></div></div>
<div class='i4'>{ic('truck',44)}<div><h4>FREE PICKUP</h4><p>30km, đơn từ 20kg</p></div></div>
</div>
<div class='cta'><div class='s A'>GỬI LÀ YÊN TÂM<small>KHAI BÁO & THÔNG QUAN TRỌN GÓI</small></div>
<div class='btn'>NHẮN TIN NGAY {ic('arrow',30)}</div><div class='ph'>{ic('phone',34,OR1)}{PHONE}</div></div>"""
    return html(body, css)

# ---------- C: Highlight box + orange wave (học ForwardAir) ----------
def poster_C():
    css = f"""body{{background:linear-gradient(180deg,#F6F9FD 0%,#fff 60%)}}
.h{{position:absolute;left:56px;top:190px;line-height:1.05}}
.h .a{{font-size:84px;color:#222}} .h .b{{display:inline-block;font-size:96px;color:#fff;background:linear-gradient(90deg,{OR2},{OR1});padding:4px 22px 10px;margin:8px 0}}
.h .c{{font-size:84px;color:{NAVY}}}
.sub{{position:absolute;left:56px;top:560px;width:520px;font-size:30px;font-weight:900;color:{OR2}}} .sub span{{color:#333;font-weight:600;display:block;font-size:24px;margin-top:6px}}
.route{{position:absolute;left:0;top:0}}
.wave{{position:absolute;left:0;right:0;bottom:0;height:470px}}
.circ{{position:absolute;left:40px;top:960px;display:flex;gap:22px}}
.cc{{width:150px;text-align:center;color:#fff;font-weight:900;font-size:17px;line-height:1.25}}
.cc .o{{width:96px;height:96px;border-radius:50%;background:#fff;color:{OR2};display:flex;align-items:center;justify-content:center;margin:0 auto 10px;box-shadow:0 6px 14px rgba(0,0,0,.15)}}
.contact{{position:absolute;right:40px;bottom:46px;width:470px;background:#fff;border-radius:60px;border:3px solid {OR1};padding:18px 30px;color:{NAVY};font-weight:900;font-size:30px;display:flex;flex-direction:column;gap:8px}}
.contact small{{white-space:nowrap}} .contact div{{display:flex;align-items:center;gap:12px}} .contact small{{font-size:16px;font-weight:700;color:#55657A}}
"""
    wave = f"""<svg class='wave' viewBox='0 0 1080 470' preserveAspectRatio='none'>
<path d='M0 120 Q270 20 540 110 T1080 60 L1080 470 L0 470Z' fill='{OR1}'/>
<path d='M0 170 Q300 70 560 160 T1080 120 L1080 470 L0 470Z' fill='{OR2}'/>
<path d='M560 470 Q600 330 760 300 L1080 290 L1080 470Z' fill='#fff' opacity='.0'/></svg>"""
    route = f"""<svg class='route' viewBox='0 0 1080 1350' width='1080' height='1350'>
<path d='M660 600 Q800 380 960 470' fill='none' stroke='{NAVY}' stroke-width='3' stroke-dasharray='10 8' opacity='.6'/>
<circle cx='660' cy='600' r='10' fill='{OR1}'/><circle cx='960' cy='470' r='10' fill='{OR1}'/></svg>"""
    body = f"""<div class='abs' style='top:40px;left:56px'>{logo(size=92)}</div>
{route}
<div class='abs' style='right:30px;top:120px'>{plane(470,-16)}</div>
<div class='abs' style='left:628px;top:520px;font-size:54px'>🇻🇳</div><div class='abs' style='left:930px;top:395px;font-size:54px'>🇰🇷</div>
<div class='h A'><div class='a'>MỘT THÙNG HÀNG</div><div class='b'>VỊ QUÊ NHÀ</div><div class='c'>TỚI TAY CON Ở HÀN</div></div>
<div class='sub'>Chỉ 75K/kg · đơn từ 21kg<span>Đồ khô, gia vị, quần áo… nhắn danh sách để 90S kiểm tra món gửi được</span></div>
<div class='abs' style='right:60px;top:640px'>{bigbox(400)}</div>
{wave}
<div class='circ'>
<div class='cc'><div class='o'>{ic('truck',50)}</div>FREE PICKUP<br>30KM</div>
<div class='cc'><div class='o'>{ic('box',50)}</div>HÚT CHÂN<br>KHÔNG</div>
<div class='cc'><div class='o'>{ic('clock',50)}</div>3–5 NGÀY<br>TỪ NGÀY BAY</div>
<div class='cc'><div class='o'>{ic('pin',50)}</div>TRACKING<br>TẬN TAY</div>
</div>
<div class='contact'><div>{ic('phone',30,OR2)}{PHONE}</div><small>Zalo/WhatsApp · Kho 191A Gò Dưa, Thủ Đức</small></div>
<div class='abs' style='left:40px;bottom:50px;color:#fff;font-weight:900;font-size:26px;width:520px;line-height:1.3'>Mẹ gom đồ – 90S lo phần còn lại 🧡</div>"""
    return html(body, css)

# ---------- D: Sunset runway + swoosh (học Axis) – tuyến Úc ----------
def poster_D():
    css = f"""body{{background:linear-gradient(180deg,#9CC9EE 0%,#F4D7B5 48%,#F6B26B 60%,#59606E 61%,#3C4352 100%)}}
.sun{{position:absolute;left:120px;top:640px;width:360px;height:360px;border-radius:50%;background:radial-gradient(circle,#FFF2C9 0%,rgba(255,200,120,.6) 40%,rgba(255,180,90,0) 70%)}}
.pre{{position:absolute;left:56px;top:160px;font-size:30px;font-weight:900;color:{OR2}}}
.h{{position:absolute;left:56px;top:225px;font-size:82px;line-height:1.15;color:{NAVY}}} .h span{{color:{OR2}}}
.s{{position:absolute;left:56px;top:450px;font-size:28px;font-weight:700;color:#253650}}
.price{{position:absolute;right:50px;top:200px;background:{NAVY};border-radius:24px;padding:18px 26px;color:#fff;text-align:center;border:4px solid {OR1};box-shadow:0 12px 24px rgba(13,43,94,.3)}}
.price p{{font-size:20px;font-weight:800}} .price b{{display:block;font-size:84px;color:{YEL};line-height:1}} .price small{{font-size:18px;font-weight:700;color:#C9D6EC}}
.runway{{position:absolute;left:0;right:0;top:820px;height:300px}}
.icons{{position:absolute;left:30px;right:30px;top:1100px;color:{NAVY}}}
.icons .i4{{border-right:2px solid rgba(13,43,94,.2);flex-direction:column;text-align:center;gap:8px}} .icons .i4 svg{{color:{OR2}}}
.icons .i4 h4{{font-size:20px}}
.wh{{position:absolute;left:0;right:0;top:1060px;height:170px;background:#fff;border-radius:40px 40px 0 0}}
.sw{{position:absolute;right:0;bottom:120px;width:420px;height:200px}}
"""
    runway = f"""<svg class='runway' viewBox='0 0 1080 300' preserveAspectRatio='none'>
<path d='M300 0 L780 0 L1080 300 L0 300Z' fill='#4A5162'/>
{''.join(f"<rect x='{536-i*3}' y='{20+i*45}' width='{8+i*6}' height='{18+i*6}' fill='#F2F2F2' opacity='.85'/>" for i in range(6))}
<path d='M300 0 L0 300' stroke='{OR1}' stroke-width='6'/><path d='M780 0 L1080 300' stroke='{OR1}' stroke-width='6'/></svg>"""
    sw = f"""<svg class='sw' viewBox='0 0 420 200' preserveAspectRatio='none'><path d='M0 200 Q200 160 420 20 L420 200Z' fill='{NAVY}'/><path d='M60 200 Q250 150 420 70 L420 90 Q260 165 120 200Z' fill='{OR1}'/></svg>"""
    body = f"""<div class='sun'></div>
<div class='abs' style='top:40px;left:56px'>{logo(size=88)}</div>
<div class='abs' style='right:56px;top:60px;font-size:22px;font-weight:800;color:{NAVY};border-left:4px solid {OR1};padding-left:14px;line-height:1.3'>CHUYÊN TUYẾN<br>VIỆT NAM – ÚC 🇦🇺</div>
<div class='pre'>CÙNG 90S CARGO EXPRESS</div>
<div class='h A'>GỬI QUÀ SANG ÚC<br><span>TỚI TAY TRƯỚC TẾT</span></div>
<div class='s'>Kiểm tra hàng kỹ – Úc kiểm dịch rất chặt.</div>
<div class='price'><p>CƯỚC ƯU ĐÃI</p><b class='A'>135K</b><small>/kg · đơn từ 21kg</small></div>
{runway}
<div class='abs' style='left:50%;top:470px;transform:translateX(-50%)'>{plane(640,-12)}</div>
<div class='abs' style='left:50%;top:800px;transform:translateX(-50%)'>{bigbox(330)}</div>
<div class='wh'></div>
<div class='icons icons4'>
<div class='i4'>{ic('box',44)}<h4>ĐÓNG GÓI KỸ</h4></div>
<div class='i4'>{ic('clock',44)}<h4>3–5 NGÀY BAY</h4></div>
<div class='i4'>{ic('pin',44)}<h4>CÓ TRACKING</h4></div>
<div class='i4'>{ic('truck',44)}<h4>FREE PICKUP</h4></div>
</div>
<div class='abs' style='left:0;right:0;bottom:120px;height:8px;background:linear-gradient(90deg,{NAVY},{OR1})'></div>{bar()}"""
    return html(body, css)


# ---------- E: Danh sách được / không được gửi (bài hướng dẫn) ----------
def poster_E():
    css = f"""body{{background:linear-gradient(180deg,#fff 0%,#F2F6FB 100%)}}
.h{{position:absolute;left:56px;right:56px;top:170px;line-height:1.08}}
.h .a{{font-size:62px;color:{NAVY}}} .h .b{{display:inline-block;font-size:92px;color:#fff;background:#D7261E;padding:2px 22px 8px;margin:6px 0}}
.h .c{{font-size:62px;color:{NAVY}}}
.list{{position:absolute;left:56px;top:520px;width:600px;display:flex;flex-direction:column;gap:14px}}
.x{{display:flex;align-items:center;gap:18px;background:#fff;border-radius:18px;padding:14px 18px;box-shadow:0 6px 16px rgba(13,43,94,.1);border-left:8px solid #D7261E}}
.x .n{{width:56px;height:56px;border-radius:50%;background:#D7261E;color:#fff;font-size:34px;font-weight:900;display:flex;align-items:center;justify-content:center;flex:none}}
.x h5{{font-size:27px;font-weight:900;color:{NAVY}}} .x p{{font-size:19px;font-weight:600;color:#55657A;margin-top:2px}}
.ok{{position:absolute;right:40px;top:560px;width:350px;background:{NAVY};border-radius:24px;padding:24px;color:#fff}}
.ok h4{{font-size:26px;font-weight:900;color:{YEL};margin-bottom:12px}} .ok li{{list-style:none;font-size:21px;font-weight:700;margin:10px 0;display:flex;gap:10px;align-items:flex-start}}
.ok li span{{color:#3BD16F;font-weight:900}}
.note{{position:absolute;left:56px;right:56px;top:1085px;background:linear-gradient(90deg,{OR2},{OR1});border-radius:20px;color:#fff;padding:18px 26px;font-size:24px;font-weight:800;line-height:1.35}}
.note b{{color:{YEL}}}
"""
    items = [("Thịt khô, khô bò, khô heo","Sản phẩm thịt bị hải quan Hàn kiểm soát gắt"),
             ("Ruốc, chà bông","Cũng là sản phẩm từ thịt"),
             ("Thịt gà, vịt chế biến","Kể cả đã hút chân không"),
             ("Trái cây tươi","Xoài, cam, táo… dễ bị tiêu hủy"),
             ("Cây, rau còn dính đất","Nguy cơ sâu bệnh nông nghiệp")]
    lst = "".join(f"<div class='x'><div class='n'>✕</div><div><h5>{a}</h5><p>{b}</p></div></div>" for a,b in items)
    body = f"""<div class='abs' style='top:40px;left:56px'>{logo(size=88)}</div>
<div class='abs' style='right:56px;top:46px;font-size:64px'>🇰🇷</div>
<div class='h A'><div class='a'>GỬI ĐỒ SANG HÀN</div><div class='b'>5 MÓN KHÔNG NÊN GỬI</div><div class='c'>KẺO BỊ GIỮ HÀNG</div></div>
<div class='list'>{lst}</div>
<div class='ok'><h4>✓ THƯỜNG GỬI ĐƯỢC</h4><ul>
<li><span>✓</span>Bánh kẹo, snack đóng gói có nhãn</li><li><span>✓</span>Quần áo, giày dép</li>
<li><span>✓</span>Mỹ phẩm đóng gói sẵn</li><li><span>✓</span>Đồ dùng cá nhân, sách vở</li></ul>
<div style='margin-top:14px'>{bigbox(240)}</div></div>
<div class='note'>Không chắc món nào? <b>Nhắn danh sách cho 90S</b> – kiểm tra trước khi đóng thùng, tránh mất hàng, mất tiền.</div>
{bar()}"""
    return html(body, css)

# ---------- F: Free pickup tận nhà – tuyến Hàn (bài bán hàng) ----------
def poster_F():
    css = f"""body{{background:linear-gradient(180deg,#fff 0%,#EEF3FA 70%,#E3EBF6 100%)}}
.h{{position:absolute;left:56px;top:170px;line-height:1.06}}
.h .a{{font-size:80px;color:{NAVY}}} .h .b{{display:inline-block;font-size:104px;color:#fff;background:linear-gradient(90deg,{OR2},{OR1});padding:4px 24px 10px;margin:8px 0}}
.h .c{{font-size:80px;color:{NAVY}}}
.sub{{position:absolute;left:56px;top:560px;width:560px;font-size:26px;font-weight:700;color:#33435C;line-height:1.4}} .sub b{{color:{OR2}}}
.price{{position:absolute;right:50px;top:180px;background:{NAVY};border-radius:24px;padding:18px 26px;color:#fff;text-align:center;border:4px solid {OR1};box-shadow:0 12px 24px rgba(13,43,94,.3)}}
.price p{{font-size:20px;font-weight:800}} .price b{{display:block;font-size:92px;color:{YEL};line-height:1}} .price small{{font-size:18px;font-weight:700;color:#C9D6EC}}
.zone{{position:absolute;left:56px;top:700px;display:flex;gap:10px}}
.zone div{{background:#fff;border:3px solid {NAVY};border-radius:40px;padding:8px 16px;font-weight:900;font-size:20px;color:{NAVY};display:flex;gap:8px;align-items:center}}
.zone svg{{color:{OR2}}}
.ring{{position:absolute;right:30px;top:540px;width:400px;height:400px;border-radius:50%;border:4px dashed {OR1};display:flex;align-items:center;justify-content:center}}
.ring .km{{position:absolute;top:-24px;left:50%;transform:translateX(-50%);background:{OR2};color:#fff;font-weight:900;font-size:26px;padding:6px 20px;border-radius:30px;white-space:nowrap}}
.steps{{position:absolute;left:30px;right:30px;top:1060px;background:{NAVY};border-radius:24px;padding:26px 10px;color:#fff}}
.steps .i4 svg{{color:{OR1};flex:none}}
"""
    body = f"""<div class='abs' style='top:40px;left:56px'>{logo(size=88)}</div>
<div class='h A'><div class='a'>GỬI HÀNG ĐI HÀN</div><div class='b'>LẤY TẬN NHÀ</div><div class='c'>MIỄN PHÍ 30KM</div></div>
<div class='price'><p>🇰🇷 HÀN QUỐC</p><b class='A'>75K</b><small>/kg · đơn từ 21kg</small></div>
<div class='sub'>Free pickup cho <b>đơn từ 20kg</b>. Ở tỉnh xa? Gửi chành xe về kho, <b>90S chụp hình & đóng gói</b> giúp bạn.</div>
<div class='zone'><div>{ic('pin',22)}TP.HCM</div><div>{ic('pin',22)}BÌNH DƯƠNG</div><div>{ic('pin',22)}ĐỒNG NAI</div></div>
<div class='ring'><div class='km'>BÁN KÍNH 30KM</div>{bigbox(300)}</div>
<div class='abs' style='left:70px;top:830px;color:{NAVY}'>{ic('truck',150,NAVY)}</div>
<div class='abs' style='left:250px;top:870px'>{plane(300,-10)}</div>
<div class='steps icons4'>
<div class='i4'>{ic('truck',44)}<div><h4>NHẬN HÀNG</h4><p>Tận nơi hoặc về kho</p></div></div>
<div class='i4'>{ic('box',44)}<div><h4>ĐÓNG GÓI</h4><p>Hút chân không</p></div></div>
<div class='i4'>{ic('scale',44)}<div><h4>CÂN – ĐO</h4><p>Chụp hình báo giá</p></div></div>
<div class='i4'>{ic('clock',44)}<div><h4>3–5 NGÀY</h4><p>Kể từ ngày bay</p></div></div>
</div>
{bar()}"""
    return html(body, css)

# ---------- G: Hỏi đáp – món này gửi sang Úc được không? (bài tương tác) ----------
def poster_G():
    css = f"""body{{background:linear-gradient(180deg,#0A1E45 0%,#14408A 60%,#1D4F9E 100%)}}
.h{{position:absolute;left:40px;right:40px;top:160px;line-height:1.28;text-align:center}}
.h .a{{font-size:80px;color:#fff}} .h .b{{display:inline-block;font-size:104px;line-height:1.15;color:#fff;background:linear-gradient(90deg,{OR2},{OR1});padding:14px 26px 6px;margin:14px 0}}
.h .c{{font-size:62px;color:{OR1};white-space:nowrap}}
.bub{{position:absolute;background:#fff;border-radius:28px;padding:20px 28px;font-size:28px;font-weight:800;color:{NAVY};box-shadow:0 10px 24px rgba(0,0,0,.3)}}
.bub:after{{content:'';position:absolute;bottom:-18px;width:0;height:0;border:18px solid transparent;border-top-color:#fff;border-bottom:0}}
.bl:after{{left:40px}} .br:after{{right:40px}}
.ans{{position:absolute;left:56px;right:56px;top:980px;background:linear-gradient(90deg,{OR2},{OR1});border-radius:24px;padding:22px 28px;color:#fff;font-size:27px;font-weight:800;line-height:1.4;display:flex;gap:20px;align-items:center}}
.ans b{{color:{YEL}}} .ans svg{{flex:none}}
.warn{{position:absolute;left:56px;right:56px;top:905px;text-align:center;color:#C9D6EC;font-size:22px;font-weight:700}}
"""
    body = f"""<div class='abs' style='top:40px;left:56px'>{logo(dark=True,size=88)}</div>
<div class='abs' style='right:56px;top:50px;font-size:64px'>🇦🇺</div>
<div class='h A'><div class='a'>MÓN NÀY GỬI SANG ÚC</div><div class='b'>ĐƯỢC KHÔNG?</div><div class='c'>HỎI 90S TRƯỚC KHI ĐÓNG THÙNG</div></div>
<div class='bub bl' style='left:56px;top:640px'>Bánh kẹo đóng gói gửi được không? 🍬</div>
<div class='bub br' style='right:56px;top:770px'>Gạo, đồ khô có bị giữ không? 🤔</div>
<div class='abs' style='left:50%;top:560px;transform:translateX(-50%);opacity:.0'></div>
<div class='warn'>Úc kiểm dịch rất chặt – nhất là thực phẩm</div>
<div class='ans'>{ic('chat',64,'#fff')}<div>Comment hoặc nhắn <b>danh sách đồ</b> – 90S kiểm tra từng món trước khi gửi. Cước <b>135K/kg</b> cho đơn từ 21kg.</div></div>
{bar()}"""
    return html(body, css)

POSTERS = {"F_han_pickup": poster_F, "G_uc_hoi_dap": poster_G, "E_han_mon_cam": poster_E, "A_tong_quan": poster_A, "B_han_tiet_kiem": poster_B, "C_han_vi_que": poster_C, "D_uc_tet": poster_D}

async def main(keys):
    async with async_playwright() as p:
        b = await p.chromium.launch(**({"executable_path": "/usr/bin/google-chrome"} if pathlib.Path("/usr/bin/google-chrome").exists() else {}))
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        for k in keys:
            f = OUT / f"{k}.html"; f.write_text(POSTERS[k](), encoding="utf-8")
            await pg.goto(f.as_uri()); await pg.wait_for_timeout(400)
            await pg.screenshot(path=str(OUT / f"{k}.jpg"), type="jpeg", quality=92)
        await b.close()

asyncio.run(main(sys.argv[1:] or list(POSTERS)))
