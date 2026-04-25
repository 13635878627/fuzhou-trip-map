# -*- coding: utf-8 -*-
"""
福州行程专属地图 - 二维码生成工具
使用方法：
1. 先把 fuzhou-personal-map.html 部署到公网（可用GitHub Pages、腾讯云COS等）
2. 填写下面的 MAP_URL 为你的部署地址
3. 运行脚本生成二维码
"""

import qrcode
import qrcode.image.svg
from PIL import Image
import os

# ========== 配置区 ==========
# 部署后的地图URL（把HTML上传到公网后填这里）
MAP_URL = "https://your-domain.com/fuzhou-personal-map.html"

# 二维码样式
QR_SIZE = 400          # 二维码像素大小
QR_FILL_COLOR = "#1a1a2e"  # 二维码颜色
QR_BACK_COLOR = "white"    # 背景色

# 输出文件
OUTPUT_FILE = "fuzhou-map-qrcode.png"
OUTPUT_SVG = "fuzhou-map-qrcode.svg"
# =============================

def generate_qrcode():
    if MAP_URL.startswith("https://your-domain"):
        print("⚠️  请先修改 MAP_URL 为实际部署地址！")
        print("   1. 把 fuzhou-personal-map.html 上传到GitHub Pages或其他托管服务")
        print("   2. 修改脚本中的 MAP_URL 为实际URL")
        print("   3. 重新运行脚本")
        return
    
    print(f"📍 正在生成二维码...")
    print(f"   目标地址: {MAP_URL}")
    
    # 生成PNG
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    qr.add_data(MAP_URL)
    qr.make(fit=True)
    
    img = qr.make_image(fill_color=QR_FILL_COLOR, back_color=QR_BACK_COLOR)
    img = img.resize((QR_SIZE, QR_SIZE), Image.LANCZOS)
    
    img.save(OUTPUT_FILE)
    print(f"✅ PNG二维码已生成: {OUTPUT_FILE}")
    
    # 生成SVG（矢量格式，适合印刷）
    svg_img = qr.make_image(image_factory=qrcode.image.svg.SvgImage)
    with open(OUTPUT_SVG, 'wb') as f:
        svg_img.write(f)
    print(f"✅ SVG矢量二维码已生成: {OUTPUT_SVG}")
    
    print(f"\n📱 使用方法：")
    print(f"   1. 用高德地图App扫描二维码")
    print(f"   2. 点击右上角【···】可分享给同行朋友")
    print(f"   3. 同行朋友扫码后也能看到完整地图")


if __name__ == "__main__":
    generate_qrcode()
