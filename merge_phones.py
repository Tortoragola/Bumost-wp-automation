#!/usr/bin/env python3
"""
Create group_members.json from phone number list
"""

import json

def merge_phone_numbers():
    """Create group members file from phone numbers"""
    
    print("\n" + "=" * 70)
    print("   Telefon Numarası Listesi → group_members.json")
    print("=" * 70 + "\n")
    
    # Read phone numbers from file
    print("📱 Telefon numaraları okunuyor...")
    try:
        with open('/Users/tolgakula/Desktop/pnum.txt', 'r', encoding='utf-8') as f:
            phone_lines = f.readlines()
        
        phones = []
        for line in phone_lines:
            phone = line.strip().replace('+', '').replace(' ', '').replace('-', '')
            if phone and phone.isdigit() and len(phone) >= 10:
                phones.append(phone)
        
        print(f"✅ {len(phones)} telefon numarası bulundu")
        
        # Remove duplicates but keep order
        seen = set()
        unique_phones = []
        for phone in phones:
            if phone not in seen:
                seen.add(phone)
                unique_phones.append(phone)
        
        phones = unique_phones
        print(f"✅ Tekrarlar temizlendi: {len(phones)} benzersiz numara")
        
    except FileNotFoundError:
        print("❌ /Users/tolgakula/Desktop/pnum.txt bulunamadı!")
        return False
    
    if not phones:
        print("❌ Geçerli telefon numarası bulunamadı!")
        return False
    
    # Create members list
    print(f"\n� {len(phones)} üye oluşturuluyor...")
    
    members = []
    for idx, phone in enumerate(phones, 1):
        members.append({
            "name": f"Üye {idx}",  # Basit isim
            "phone": phone
        })
    
    # Create data structure
    data = {
        "group_name": "BUMOST WhatsApp Grubu",
        "members": members
    }
    
    # Save to file
    try:
        # Backup if exists
        import os
        if os.path.exists('group_members.json'):
            import shutil
            from datetime import datetime
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup = f'group_members_backup_{timestamp}.json'
            shutil.copy('group_members.json', backup)
            print(f"💾 Yedek oluşturuldu: {backup}")
        
        # Save
        with open('group_members.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print("\n" + "─" * 70)
        print("✅ group_members.json oluşturuldu!")
        print("─" * 70)
        print(f"📊 Toplam üye: {len(members)}")
        print(f"📱 Tüm üyelerin telefon numarası var!")
        
        print("\n🚀 Artık 'python3 main.py' ile mesaj gönderebilirsiniz!")
        print("=" * 70 + "\n")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Dosya kaydedilemedi: {e}")
        return False


if __name__ == '__main__':
    try:
        merge_phone_numbers()
    except KeyboardInterrupt:
        print("\n\n❌ İptal edildi")
        exit(0)
