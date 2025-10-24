#!/usr/bin/env python3
"""
WhatsApp Group Members Extractor
Automatically extracts group members from WhatsApp Web using Playwright
"""

import json
import sys
import time
from playwright.sync_api import sync_playwright, TimeoutError as PlaywrightTimeout

def extract_group_members_from_whatsapp():
    """Extract group members from WhatsApp Web using Playwright"""
    
    print("\n" + "=" * 70)
    print("   WhatsApp Grup Üyeleri Otomatik Çıkarıcı (Playwright)")
    print("=" * 70 + "\n")
    
    print("📱 WhatsApp Web'den grup üyeleri otomatik olarak çıkarılacak.\n")
    
    with sync_playwright() as p:
        print("🌐 Tarayıcı başlatılıyor...")
        
        try:
            # Launch browser with persistent context
            browser = p.chromium.launch_persistent_context(
                user_data_dir="./whatsapp-session",
                headless=False,
                args=['--disable-blink-features=AutomationControlled']
            )
            
            page = browser.pages[0] if browser.pages else browser.new_page()
            page.goto("https://web.whatsapp.com", timeout=60000)
            
            print("\n" + "─" * 70)
            print("⚠️  ÖNEMLİ:")
            print("   1. QR kodu telefonunuzla okutun (ilk seferde)")
            print("   2. WhatsApp Web açıldıktan sonra istediğiniz GRUBU açın")
            print("   3. Grup sohbetini açtıktan sonra terminale dönün")
            print("─" * 70 + "\n")
            
            input("Grubu açtıktan sonra Enter'a basın...")
            
            print("\n🔍 Grup bilgileri alınıyor...")
            time.sleep(2)
            
            # Click on group header
            try:
                header = page.wait_for_selector("header[data-testid='conversation-header']", timeout=10000)
                header.click()
                print("✅ Grup başlığına tıklandı")
                time.sleep(2)
            except PlaywrightTimeout:
                print("⚠️  Grup başlığı bulunamadı. Manuel olarak grup adına tıklayın...")
                time.sleep(5)
            
            # Get group name
            group_name = "WhatsApp Grubu"
            try:
                group_name_elem = page.wait_for_selector("div[data-testid='drawer-body'] h1", timeout=5000)
                group_name = group_name_elem.inner_text()
                print(f"📊 Grup: {group_name}")
            except:
                print("⚠️  Grup adı alınamadı")
            
            # Scroll to load all members
            print("\n📜 Üyeler yükleniyor (kaydırma yapılıyor)...")
            
            try:
                members_container = page.wait_for_selector("div[data-testid='drawer-body']", timeout=10000)
                
                last_height = 0
                scroll_attempts = 0
                max_scrolls = 100
                
                while scroll_attempts < max_scrolls:
                    members_container.evaluate("element => element.scrollTo(0, element.scrollHeight)")
                    time.sleep(0.8)
                    
                    new_height = members_container.evaluate("element => element.scrollHeight")
                    
                    if new_height == last_height:
                        print(f"✅ Tüm üyeler yüklendi (kaydırma: {scroll_attempts})")
                        break
                    
                    last_height = new_height
                    scroll_attempts += 1
                    
                    if scroll_attempts % 10 == 0:
                        print(f"   📍 Kaydırma {scroll_attempts}/{max_scrolls}...")
                
                time.sleep(2)
                
            except PlaywrightTimeout:
                print("⚠️  Kaydırma yapılamadı")
            
            # Extract members
            print("\n👥 Üye bilgileri çıkarılıyor...")
            
            members = []
            
            try:
                member_elements = page.query_selector_all("div[role='listitem']")
                
                print(f"🔍 {len(member_elements)} üye bulundu\n")
                
                for idx, member_elem in enumerate(member_elements, 1):
                    try:
                        name_elem = member_elem.query_selector("span[dir='auto']")
                        if not name_elem:
                            continue
                        
                        name = name_elem.inner_text().strip()
                        
                        if not name or name.lower() in ['sen', 'you', '']:
                            continue
                        
                        if '+' in name:
                            name = name.split('+')[0].strip()
                        
                        phone = ""
                        if '~' in name:
                            parts = name.split('~')
                            name = parts[0].strip()
                            if len(parts) > 1:
                                phone = parts[1].strip().replace('+', '').replace(' ', '')
                        
                        if name and name not in [m['name'] for m in members]:
                            members.append({"name": name, "phone": phone})
                            
                            if idx % 10 == 0 or phone:
                                status = f"{idx}. ✅ {name}"
                                if phone:
                                    status += f" ({phone})"
                                print(status)
                    
                    except:
                        continue
                
            except Exception as e:
                print(f"❌ Üye çıkarma hatası: {e}")
                browser.close()
                return False
            
            browser.close()
            
            if not members:
                print("\n❌ Hiç üye çıkarılamadı!")
                return False
            
            # Save to file
            data = {"group_name": group_name, "members": members}
            
            try:
                with open('group_members.json', 'w', encoding='utf-8') as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                
                print("\n" + "─" * 70)
                print("✅ group_members.json dosyası oluşturuldu!")
                print("─" * 70)
                print(f"📊 Grup: {group_name}")
                print(f"👥 Toplam üye: {len(members)}")
                
                with_phone = sum(1 for m in members if m.get('phone'))
                print(f"   📱 Telefon numaralı: {with_phone}")
                print(f"   🔒 Telefon numarası yok: {len(members) - with_phone}")
                
                if with_phone < len(members):
                    print("\n⚠️  NOT: Bazı üyelerin telefon numaraları alınamadı.")
                    print("   Bu üyelere mesaj gönderilemeyecek.")
                    print("   Telefon numaralarını manuel eklemeniz gerekebilir.")
                
                print("\n🚀 'python3 main.py' ile mesaj gönderebilirsiniz!")
                print("=" * 70 + "\n")
                
                return True
                
            except Exception as e:
                print(f"\n❌ Dosya kaydedilemedi: {e}")
                return False
            
        except Exception as e:
            print(f"\n❌ Hata: {e}")
            print("\nSorun giderme:")
            print("1. pip install playwright")
            print("2. playwright install chromium")
            print("3. İnternet bağlantınızı kontrol edin")
            return False


def create_group_members_manually():
    """Manual member entry"""
    
    print("\n" + "=" * 70)
    print("   Manuel Üye Ekleme")
    print("=" * 70 + "\n")
    
    group_name = input("Grup adı: ").strip() or "WhatsApp Grubu"
    members = []
    
    print("\n👥 Üye ekleme (bitirmek için 'q'):")
    
    count = 0
    while True:
        count += 1
        print(f"\n{count}. Üye:")
        name = input("  İsim: ").strip()
        
        if name.lower() in ['q', 'quit', '']:
            if count == 1:
                print("❌ En az bir üye ekleyin!")
                count = 0
                continue
            break
        
        phone = input("  Telefon (90XXXXXXXXXX): ").strip()
        
        if not phone:
            print("  ⚠️  Telefon atlandı")
            count -= 1
            continue
        
        phone = phone.replace('+', '').replace(' ', '').replace('-', '')
        
        if not phone.startswith('90') and len(phone) == 10:
            phone = '90' + phone
            print(f"  ℹ️  Ülke kodu eklendi: {phone}")
        
        if not phone.isdigit():
            print("  ⚠️  Geçersiz numara")
            count -= 1
            continue
        
        members.append({"name": name, "phone": phone})
        print(f"  ✅ {name} eklendi")
    
    if not members:
        print("\n❌ Hiç üye eklenmedi")
        return False
    
    data = {"group_name": group_name, "members": members}
    
    try:
        with open('group_members.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ {len(members)} üye eklendi!")
        return True
    except Exception as e:
        print(f"\n❌ Dosya kaydedilemedi: {e}")
        return False


def main():
    """Main entry point"""
    import os
    
    if os.path.exists('group_members.json'):
        print("\n⚠️  group_members.json zaten var!")
        confirm = input("Üzerine yaz? (evet/hayır): ").strip().lower()
        
        if confirm not in ['evet', 'e', 'yes', 'y']:
            print("\n❌ İptal edildi")
            return
        
        # Backup
        import shutil
        from datetime import datetime
        timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
        backup = f'group_members_backup_{timestamp}.json'
        shutil.copy('group_members.json', backup)
        print(f"✅ Yedek: {backup}\n")
    
    print("\nÜyeleri nasıl eklemek istersiniz?")
    print("1. Otomatik çıkar (WhatsApp Web) - ÖNERİLEN")
    print("2. Manuel gir")
    print("3. İptal")
    
    choice = input("\nSeçim (1/2/3): ").strip()
    
    if choice == '1':
        extract_group_members_from_whatsapp()
    elif choice == '2':
        create_group_members_manually()
    else:
        print("\n❌ İptal edildi")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ İptal edildi")
        sys.exit(0)
