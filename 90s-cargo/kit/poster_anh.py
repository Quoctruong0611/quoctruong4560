"""Poster dùng ẢNH THẬT của 90S (kho, đóng gói, thùng hàng) – giữ đúng nhận diện navy/cam.
Cách dùng:
  python3 poster_anh.py <anh.jpg> <ra.jpg> "<NHÃN NHỎ>" "<DÒNG 1>" "<CHỮ NỔI BẬT>" "<DÒNG 3>" "chip1|chip2|chip3"
Ví dụ:
  python3 poster_anh.py ../anh-thuc-te/kho_01.jpg out.jpg "ẢNH THẬT TẠI KHO 90S" "HÀNG ĐI HÀN" "75K/KG" "CÂN – ĐO – CHỤP HÌNH TRƯỚC KHI BAY" "Free pickup nhỏ lớn đều nhận|Giao 3–5 ngày từ ngày bay|Lấy hàng tận nhà"
Ảnh được cắt vừa khung (object-fit: cover). Chọn ảnh rõ, không lộ tên/SĐT/địa chỉ người nhận trên nhãn thùng."""
import asyncio, base64, mimetypes, pathlib, sys
from playwright.async_api import async_playwright
from poster2 import html, logo, bar, ic, NAVY, OR1, OR2, YEL

def poster_anh(img, tag, l1, hl, l3, chips):
    mime = mimetypes.guess_type(img)[0] or "image/jpeg"
    data = base64.b64encode(pathlib.Path(img).read_bytes()).decode()
    css = f"""body{{background:{NAVY}}}
.ph{{position:absolute;left:0;top:0;width:1080px;height:860px;background:url(data:{mime};base64,{data}) center/cover no-repeat}}
.sh{{position:absolute;left:0;top:0;width:1080px;height:860px;background:linear-gradient(180deg,rgba(13,43,94,.55) 0%,rgba(13,43,94,0) 22%,rgba(13,43,94,0) 55%,{NAVY} 100%)}}
.lg{{position:absolute;left:40px;top:34px;background:rgba(255,255,255,.94);border-radius:60px;padding:14px 26px}}
.tag{{position:absolute;right:40px;top:52px;background:{YEL};color:{NAVY};font-weight:900;font-size:22px;letter-spacing:1px;padding:12px 22px;border-radius:40px;display:flex;gap:10px;align-items:center}}
.dot{{width:14px;height:14px;border-radius:50%;background:{OR2}}}
.h{{position:absolute;left:48px;right:48px;top:640px;line-height:1.12}}
.h .a{{font-size:76px;color:#fff;text-shadow:0 4px 14px rgba(0,0,0,.35)}}
.h .b{{display:inline-block;font-size:118px;color:#fff;background:linear-gradient(90deg,{OR2},{OR1});padding:8px 26px 0;margin:10px 0 14px;transform:skew(-6deg)}}
.h .c{{font-size:44px;color:{OR1}}}
.chips{{position:absolute;left:48px;right:48px;top:1000px;display:flex;gap:14px;flex-wrap:wrap}}
.chip{{background:rgba(255,255,255,.1);border:2px solid rgba(255,255,255,.25);color:#fff;font-size:23px;font-weight:800;padding:12px 20px;border-radius:40px;display:flex;align-items:center;gap:10px}}
"""
    ch = "".join(f"<div class='chip'><span style='color:{OR1}'>✔</span> {c}</div>" for c in chips if c)
    body = f"""<div class='ph'></div><div class='sh'></div>
<div class='lg'>{logo(size=78)}</div>
<div class='tag'><span class='dot'></span>{tag}</div>
<div class='h A'><div class='a'>{l1}</div><div class='b'>{hl}</div><div class='c'>{l3}</div></div>
<div class='chips'>{ch}</div>
{bar()}"""
    return html(body, css)

async def render(img, out, *texts):
    tag, l1, hl, l3, chips = (list(texts) + [""]*5)[:5]
    h = poster_anh(img, tag, l1, hl, l3, chips.split("|"))
    tmp = pathlib.Path(out).with_suffix(".html"); tmp.write_text(h, encoding="utf-8")
    async with async_playwright() as p:
        exe = "/usr/bin/google-chrome"
        b = await p.chromium.launch(**({"executable_path": exe} if pathlib.Path(exe).exists() else {}))
        pg = await b.new_page(viewport={"width":1080,"height":1350})
        await pg.goto(tmp.resolve().as_uri()); await pg.wait_for_timeout(500)
        await pg.screenshot(path=out, type="jpeg", quality=90); await b.close()
    tmp.unlink()

if __name__ == "__main__":
    asyncio.run(render(*sys.argv[1:]))
