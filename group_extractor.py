#!/usr/bin/env python3
"""
WhatsApp Group Members Extractor
Extracts group members and creates group_members.json file
"""

import json
import sys

def create_group_members_file():
    """Interactive script to create group_members.json"""
    
    print("\n" + "=" * 60)
    print("   WhatsApp Grup Üyeleri Dosyası Oluşturucu")
    print("=" * 60 + "\n")
    
    # Get group name
    print("📝 Grup bilgileri:")
    print("─" * 60)
    group_name = input("Grup adı: ").strip()
    
    if not group_name:
        group_name = "WhatsApp Grubu"
    
    members = []
    
    print("\n" + "─" * 60)
    print("👥 Üye ekleme (bitirmek için üye adı yerine 'q' yazın)")
    print("─" * 60)
    
    member_count = 0
    
    while True:
        member_count += 1
        print(f"\n{member_count}. Üye:")
        
        name = input("  İsim: ").strip()
        
        # Exit condition
        if name.lower() in ['q', 'quit', 'exit', 'bitir', '']:
            if name == '' and member_count == 1:
                print("\n❌ En az bir üye eklemelisiniz!")
                member_count -= 1
                continue
            break
        
        phone = input("  Telefon (90XXXXXXXXXX): ").strip()
        
        # Validate phone
        if not phone:
            print("  ⚠️  Telefon numarası boş bırakılamaz, üye atlanıyor...")
            member_count -= 1
            continue
        
        # Remove + if present
        if phone.startswith('+'):
            phone = phone[1:]
        
        # Remove spaces and dashes
        phone = phone.replace(' ', '').replace('-', '')
        
        # Add country code if not present
        if not phone.startswith('90') and len(phone) == 10:
            phone = '90' + phone
            print(f"  ℹ️  Ülke kodu eklendi: {phone}")
        
        # Basic validation
        if not phone.isdigit():
            print("  ⚠️  Geçersiz telefon numarası, üye atlanıyor...")
            member_count -= 1
            continue
        
        members.append({
            "name": name,
            "phone": phone
        })
        
        print(f"  ✅ {name} eklendi!")
    
    if not members:
        print("\n❌ Hiç üye eklenmedi, dosya oluşturulmadı.")
        sys.exit(1)
    
    # Create the data structure
    data = {
        "group_name": group_name,
        "members": members
    }
    
    # Save to file
    try:
        with open('group_members.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print("\n" + "─" * 60)
        print("✅ group_members.json dosyası başarıyla oluşturuldu!")
        print("─" * 60)
        print(f"📊 Grup: {group_name}")
        print(f"👥 Toplam üye: {len(members)}")
        print("\n📋 Eklenen üyeler:")
        for i, member in enumerate(members, 1):
            print(f"  {i}. {member['name']} - {member['phone']}")
        print("\n🚀 Artık 'python main.py' komutuyla mesaj gönderebilirsiniz!")
        print("=" * 60 + "\n")
        
    except Exception as e:
        print(f"\n❌ Dosya oluşturulurken hata oluştu: {e}")
        sys.exit(1)


def add_members_to_existing():
    """Add members to existing group_members.json"""
    
    try:
        with open('group_members.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("❌ group_members.json bulunamadı. Önce dosyayı oluşturun.")
        return False
    except json.JSONDecodeError:
        print("❌ group_members.json geçerli bir JSON dosyası değil.")
        return False
    
    print(f"\n📊 Mevcut grup: {data.get('group_name', 'Bilinmeyen')}")
    print(f"👥 Mevcut üye sayısı: {len(data.get('members', []))}")
    
    members = data.get('members', [])
    
    print("\n" + "─" * 60)
    print("👥 Yeni üye ekleme (bitirmek için 'q' yazın)")
    print("─" * 60)
    
    new_count = 0
    
    while True:
        print(f"\nYeni üye:")
        
        name = input("  İsim: ").strip()
        
        if name.lower() in ['q', 'quit', 'exit', 'bitir', '']:
            break
        
        phone = input("  Telefon (90XXXXXXXXXX): ").strip()
        
        if not phone:
            print("  ⚠️  Telefon numarası boş bırakılamaz, üye atlanıyor...")
            continue
        
        # Clean phone number
        if phone.startswith('+'):
            phone = phone[1:]
        phone = phone.replace(' ', '').replace('-', '')
        
        if not phone.startswith('90') and len(phone) == 10:
            phone = '90' + phone
        
        if not phone.isdigit():
            print("  ⚠️  Geçersiz telefon numarası, üye atlanıyor...")
            continue
        
        members.append({
            "name": name,
            "phone": phone
        })
        
        new_count += 1
        print(f"  ✅ {name} eklendi!")
    
    if new_count == 0:
        print("\nℹ️  Yeni üye eklenmedi.")
        return False
    
    # Save updated data
    data['members'] = members
    
    try:
        with open('group_members.json', 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ {new_count} yeni üye eklendi!")
        print(f"📊 Toplam üye sayısı: {len(members)}")
        return True
        
    except Exception as e:
        print(f"\n❌ Dosya güncellenirken hata oluştu: {e}")
        return False


def main():
    """Main entry point"""
    
    import os
    
    # Check if file exists
    if os.path.exists('group_members.json'):
        print("\n⚠️  group_members.json dosyası zaten mevcut!")
        print("\nNe yapmak istersiniz?")
        print("1. Yeni dosya oluştur (mevcut dosya yedeklenecek)")
        print("2. Mevcut dosyaya üye ekle")
        print("3. İptal")
        
        choice = input("\nSeçiminiz (1/2/3): ").strip()
        
        if choice == '1':
            # Backup existing file
            import shutil
            from datetime import datetime
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            backup_name = f'group_members_backup_{timestamp}.json'
            shutil.copy('group_members.json', backup_name)
            print(f"✅ Mevcut dosya yedeklendi: {backup_name}")
            create_group_members_file()
        elif choice == '2':
            add_members_to_existing()
        else:
            print("\n❌ İşlem iptal edildi.")
            sys.exit(0)
    else:
        create_group_members_file()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ İşlem iptal edildi.")
        sys.exit(0)
