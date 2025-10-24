#!/usr/bin/env python3
"""
WhatsApp Bulk Message Sender using pywhatkit
Sends personalized messages to all members of a WhatsApp group
"""

import os
import sys
import json
import time
from typing import List, Dict
import pywhatkit as kit
import pyautogui

class WhatsAppBulkSender:
    """Handles sending bulk messages via WhatsApp Web"""
    
    def __init__(self):
        """Initialize the sender"""
        self.delay_between_messages = 10  # Saniye cinsinden mesajlar arası bekleme
        print("📱 WhatsApp Web kullanılarak mesajlar gönderilecek.")
        print("⚠️  Not: İlk mesaj gönderilirken WhatsApp Web tarayıcıda açılacak.")
        print("⚠️  Not: Bilgisayarınızın başında olmanız gerekiyor.")
        print("⚠️  Not: Her mesajdan sonra sekme kapanacak, sonra yeni sekme açılacak.\n")
    
    def get_group_members(self, group_file: str = 'group_members.json') -> List[Dict[str, str]]:
        """
        Load group members from JSON file
        
        Args:
            group_file: Path to JSON file containing group member phone numbers
            
        Returns:
            List of member dictionaries with phone numbers and names
        """
        try:
            with open(group_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
                return data.get('members', [])
        except FileNotFoundError:
            print(f"❌ Hata: {group_file} dosyası bulunamadı!")
            print("Örnek format için group_members.example.json dosyasına bakın.")
            sys.exit(1)
        except json.JSONDecodeError:
            print(f"❌ Hata: {group_file} geçerli bir JSON dosyası değil!")
            sys.exit(1)
    
    def format_phone_number(self, phone: str) -> str:
        """
        Format phone number for WhatsApp (add + prefix if not present)
        
        Args:
            phone: Phone number
            
        Returns:
            Formatted phone number with + prefix
        """
        phone = phone.strip()
        if not phone.startswith('+'):
            phone = '+' + phone
        return phone
    
    def send_message(self, phone_number: str, message: str, wait_time: int = 15) -> bool:
        """
        Send a message to a single phone number using pywhatkit
        
        Args:
            phone_number: Recipient's phone number (international format with +)
            message: Message text to send
            wait_time: Time to wait before sending (seconds)
            
        Returns:
            True if message sent successfully, False otherwise
        """
        try:
            # pywhatkit şu anda + bir sonraki dakikada mesaj gönderir
            # wait_time: WhatsApp Web'in açılması ve yüklenmesi için bekleme süresi
            kit.sendwhatmsg_instantly(
                phone_no=phone_number,
                message=message,
                wait_time=wait_time,
                tab_close=True,
                close_time=3
            )
            
            # Extra wait to ensure tab is fully closed before next message
            time.sleep(2)  # Sekmenin tamamen kapanmasını bekle
            
            return True
            
        except Exception as e:
            print(f"   ❌ Hata: {e}")
            return False
    
    def send_bulk_messages(self, message: str):
        """
        Send the same message to all group members
        
        Args:
            message: The message text to send
        """
        members = self.get_group_members()
        
        if not members:
            print("❌ Grup üyesi bulunamadı!")
            return
        
        total = len(members)
        successful = 0
        failed = 0
        
        print(f"\n📱 {total} kişiye mesaj gönderiliyor...\n")
        print("⏰ Mesajlar arası bekleme süresi:", self.delay_between_messages, "saniye")
        print("─" * 60)
        
        for i, member in enumerate(members, 1):
            phone = member.get('phone')
            name = member.get('name', 'Bilinmeyen')
            
            if not phone:
                print(f"{i}/{total} ⚠️  {name}: Telefon numarası eksik, atlanıyor...")
                failed += 1
                continue
            
            # Format phone number
            formatted_phone = self.format_phone_number(phone)
            
            print(f"\n{i}/{total} 📤 {name} ({formatted_phone})...")
            print(f"   ⏳ WhatsApp Web açılıyor, lütfen bekleyin...")
            
            # İlk mesaj için daha fazla bekleme süresi
            wait_time = 20 if i == 1 else 15
            
            if self.send_message(formatted_phone, message, wait_time=wait_time):
                print(f"   ✅ Mesaj gönderildi!")
                successful += 1
            else:
                print(f"   ❌ Mesaj gönderilemedi!")
                failed += 1
            
            # Son mesaj değilse bekle
            if i < total:
                print(f"   ⏰ Sonraki mesaja kadar {self.delay_between_messages} saniye bekleniyor...")
                time.sleep(self.delay_between_messages)
        
        # Summary
        print("\n" + "─" * 60)
        print(f"\n📊 Özet:")
        print(f"   ✅ Başarılı: {successful}")
        print(f"   ❌ Başarısız: {failed}")
        print(f"   📊 Toplam: {total}\n")


def main():
    """Main entry point"""
    print("\n" + "=" * 60)
    print("   WhatsApp Toplu Mesaj Gönderici (pywhatkit)")
    print("=" * 60 + "\n")
    
    print("⚠️  ÖNEMLİ UYARILAR:")
    print("   • WhatsApp Web'de oturum açmış olmalısınız")
    print("   • İşlem sırasında bilgisayarınızın başında olmalısınız")
    print("   • Mouse ve klavyeye dokunmayın (otomatik kontrol edilecek)")
    print("   • Her mesaj için tarayıcı yeni sekme açacak")
    print("─" * 60 + "\n")
    
    input("Hazır olduğunuzda Enter'a basın...")
    
    sender = WhatsAppBulkSender()
    
    # Get message from user
    print("\nGöndermek istediğiniz mesajı yazın (Enter'a iki kez basarak bitirin):")
    print("─" * 60)
    
    lines = []
    empty_count = 0
    
    try:
        while True:
            line = input()
            if line == "":
                empty_count += 1
                if empty_count >= 2:
                    break
                lines.append(line)
            else:
                empty_count = 0
                lines.append(line)
    except KeyboardInterrupt:
        print("\n\n❌ İşlem iptal edildi.")
        sys.exit(0)
    
    message = '\n'.join(lines).strip()
    
    if not message:
        print("\n❌ Mesaj boş olamaz!")
        sys.exit(1)
    
    # Confirmation
    print("\n" + "─" * 60)
    print("📝 Gönderilecek mesaj:")
    print("─" * 60)
    print(message)
    print("─" * 60)
    
    members = sender.get_group_members()
    print(f"\n📊 Toplam {len(members)} kişiye gönderilecek.")
    
    confirm = input("\n⚠️  Bu mesajı tüm grup üyelerine göndermek istiyor musunuz? (evet/hayır): ").lower()
    
    if confirm not in ['evet', 'e', 'yes', 'y']:
        print("\n❌ İşlem iptal edildi.")
        sys.exit(0)
    
    print("\n🚀 Mesaj gönderimi başlıyor...")
    print("⚠️  Lütfen bilgisayarınızın başında kalın ve işleme müdahale etmeyin!\n")
    
    time.sleep(3)  # 3 saniye hazırlık süresi
    
    # Send messages
    sender.send_bulk_messages(message)


if __name__ == '__main__':
    main()
