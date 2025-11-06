#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BEACH PLEASE 2026 - ULTRA SPEED VERSION
Pentru rulare în paralel - refresh la 0.2s, execuție sub 2s
"""

import time
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging minimal pentru viteză
logging.basicConfig(level=logging.ERROR)  # Doar erorile critice

class BeachPleaseUltraSpeed:
    def __init__(self):
        self.driver = None
        self.checkout_url = "https://www.emag.ro/cart/checkout"
        self.check_count = 0
        self.start_time = None
        
        # Setări ULTRA-RAPIDE
        self.max_retries = 3          # Doar 3 retry-uri
        self.retry_delay = 0.3        # Retry ultra-rapid
        self.step_delay = 0.1         # Pauze minime între pași
        self.refresh_interval = 0.2   # Refresh la 0.2 secunde!
        
    def setup_ultra_driver(self):
        """Setup pentru viteză EXTREMĂ"""
        try:
            options = Options()
            # Optimizări EXTREME pentru viteză maximă
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-images')
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-plugins')
            options.add_argument('--disable-logging')
            options.add_argument('--disable-background-timer-throttling')
            options.add_argument('--disable-renderer-backgrounding')
            options.add_argument('--disable-features=TranslateUI')
            options.add_argument('--aggressive-cache-discard')
            options.add_experimental_option("excludeSwitches", ["enable-automation", "enable-logging"])
            options.add_experimental_option('useAutomationExtension', False)
            
            self.driver = webdriver.Chrome(options=options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
            
            # Settings ULTRA-RAPIDE
            self.driver.set_page_load_timeout(5)  # Foarte scurt
            self.driver.implicitly_wait(0.5)      # Minimal
            self.driver.set_window_size(1920, 1080)
            
            print("🚀 ULTRA-SPEED Bot initialized!")
            return True
            
        except Exception as e:
            print(f"❌ Setup failed: {e}")
            return False
    
    def prepare_ultra_monitoring(self):
        """Pregătire ULTRA-RAPIDĂ"""
        print("\n⚡ BEACH PLEASE 2026 - ULTRA SPEED BOT ⚡")
        print("=" * 55)
        print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"👤 MihaiMunteanu1 - PARALEL MODE")
        print("⚡ REFRESH: la 0.2 secunde")
        print("⚡ EXECUȚIE: sub 2 secunde target")
        print("=" * 55)
        
        self.driver.get("https://www.emag.ro")
        input("\n🚀 Beach Please 2026 + ENTER >>> ")
        
        current_url = self.driver.current_url
        print(f"✅ Control preluat! {current_url[:50]}...")
        
        self.start_time = datetime.now()
        print(f"⚡ ULTRA-SPEED ACTIVAT la {self.start_time.strftime('%H:%M:%S')}!")
        print("=" * 55)
        
        return True
    
    def ultra_fast_check(self):
        """Verificare ULTRA-RAPIDĂ"""
        try:
            # Refresh INSTANT
            self.driver.refresh()
            time.sleep(0.1)  # Pauză minimă
            
            # Căutare RAPIDĂ cu JavaScript
            result = self.driver.execute_script("""
                var selectors = [
                    'button.yeahIWantThisProduct',
                    'button[data-test="main-add-to-cart-button"]',
                    'button[data-offer-id]:not([disabled])'
                ];
                
                for (var i = 0; i < selectors.length; i++) {
                    var btn = document.querySelector(selectors[i]);
                    if (btn && btn.offsetParent !== null && !btn.disabled) {
                        var text = btn.textContent.toLowerCase();
                        if (text.includes('adauga') || text.includes('cos') || text.includes('cumpara')) {
                            return btn;
                        }
                    }
                }
                return null;
            """)
            
            return result
            
        except Exception:
            return None
    
    def ultra_add_to_cart(self, add_button):
        """Adăugare ULTRA-RAPIDĂ"""
        print("⚡ [1/3] ADD...")
        
        for attempt in range(self.max_retries):
            try:
                # Click INSTANT cu JavaScript
                self.driver.execute_script("arguments[0].click();", add_button)
                time.sleep(self.step_delay)
                return True
            except Exception:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                    continue
                return False
        return False
    
    def ultra_checkout(self):
        """Checkout ULTRA-RAPID"""
        print("⚡ [2/3] CHECKOUT...")
        
        time.sleep(self.step_delay)
        
        for attempt in range(self.max_retries):
            try:
                # Navigare JavaScript INSTANT
                self.driver.execute_script(f"window.location.href = '{self.checkout_url}';")
                
                # Wait minimal
                WebDriverWait(self.driver, 3).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )
                
                time.sleep(self.step_delay)
                return True
            except Exception:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                    continue
                return False
        return False
    
    def ultra_send_order(self):
        """Trimite comandă ULTRA-RAPID"""
        print("⚡ [3/3] SEND...")
        
        time.sleep(self.step_delay)
        
        for attempt in range(self.max_retries):
            try:
                # Căutare și click cu JavaScript DIRECT
                result = self.driver.execute_script("""
                    var selectors = [
                        'button[data-test="summarySubmitBtn"]',
                        'button[type="submit"][data-type="submit"]'
                    ];
                    
                    for (var i = 0; i < selectors.length; i++) {
                        var btn = document.querySelector(selectors[i]);
                        if (btn && btn.offsetParent !== null && !btn.disabled) {
                            btn.click();
                            return btn.textContent.trim();
                        }
                    }
                    return null;
                """)
                
                if result:
                    time.sleep(0.5)  # Pauză minimă pentru procesare
                    return True
                else:
                    raise Exception("Buton nu găsit")
                    
            except Exception:
                if attempt < self.max_retries - 1:
                    time.sleep(self.retry_delay)
                    try:
                        self.driver.refresh()
                        time.sleep(0.5)
                    except:
                        pass
                    continue
                return False
        return False
    
    def execute_ultra_purchase(self, add_button):
        """Execuție ULTRA-RAPIDĂ"""
        purchase_start = time.time()
        detection_time = datetime.now().strftime('%H:%M:%S.%f')[:-3]  # Cu milisecunde
        
        print(f"\n{'⚡' * 30}")
        print(f"🚨 ULTRA-SPEED EXECUTION! 🚨")
        print(f"⏰ {detection_time}")
        print(f"🎯 TARGET: SUB 2 SECUNDE!")
        print(f"{'⚡' * 30}")
        
        success_count = 0
        
        # ETAPA 1: Add to cart ULTRA-RAPID
        if self.ultra_add_to_cart(add_button):
            success_count += 1
        else:
            print("❌ ADD FAILED!")
            return False
        
        # ETAPA 2: Checkout ULTRA-RAPID
        if self.ultra_checkout():
            success_count += 1
        else:
            print("❌ CHECKOUT FAILED!")
            return False
        
        # ETAPA 3: Send order ULTRA-RAPID
        if self.ultra_send_order():
            success_count += 1
        else:
            print("❌ SEND FAILED!")
            return False
        
        # SUCCES ULTRA!
        total_time = time.time() - purchase_start
        
        print(f"\n{'🏆' * 35}")
        print(f"⚡ BEACH PLEASE 2026 - ULTRA SUCCESS! ⚡")
        print(f"👤 MihaiMunteanu1")
        print(f"⚡ TIMP: {total_time:.3f} secunde")
        print(f"📊 Pași: {success_count}/3")
        print(f"⏰ Final: {datetime.now().strftime('%H:%M:%S.%f')[:-3]}")
        
        # Check final URL
        time.sleep(0.5)
        final_url = self.driver.current_url
        print(f"📋 URL: {final_url}")
        
        if "pay.emag.ro" in final_url:
            print(f"💳 ✅ PERFECT! ULTRA SUCCESS!")
        
        if total_time < 2.0:
            print(f"🔥 SUB 2 SECUNDE CONFIRMAT!")
        
        print(f"🏆" * 35)
        
        return True
    
    def run_ultra_monitoring(self):
        """Monitorizare ULTRA-RAPIDĂ"""
        try:
            if not self.setup_ultra_driver():
                return False
            
            if not self.prepare_ultra_monitoring():
                return False
            
            # MONITORIZARE ULTRA-RAPIDĂ
            while True:
                try:
                    self.check_count += 1
                    current_time = datetime.now()
                    
                    # Verificare ULTRA-RAPIDĂ
                    add_button = self.ultra_fast_check()
                    
                    if add_button:
                        # GĂSIT! Execuție ULTRA-RAPIDĂ!
                        print(f"\n🎯 BUTON GĂSIT - ULTRA EXECUTION!")
                        
                        success = self.execute_ultra_purchase(add_button)
                        
                        if success:
                            print("\n🎉 ULTRA MISSION COMPLETE!")
                            break
                        else:
                            print("\n⚠️ ULTRA execution incomplete!")
                            break
                    
                    # Status la fiecare 150 de verificări (30 secunde la 0.2s)
                    if self.check_count % 150 == 0:
                        elapsed = current_time - self.start_time
                        minutes = elapsed.total_seconds() // 60
                        print(f"📊 #{self.check_count} | {current_time.strftime('%H:%M:%S')} | {minutes:.0f}m")
                    
                    # PAUZĂ ULTRA-SCURTĂ - 0.2 secunde!
                    time.sleep(self.refresh_interval)
                    
                except KeyboardInterrupt:
                    print(f"\n🛑 ULTRA-SPEED STOPPED")
                    print(f"📊 Checks: {self.check_count}")
                    break
                    
                except Exception as e:
                    # Erori minime - continuă rapid
                    time.sleep(1)
                    continue
            
            return True
            
        finally:
            if self.driver:
                print("\n📋 ULTRA monitoring ended!")
                input("ENTER to close...")
                self.driver.quit()

if __name__ == "__main__":
    print("⚡ BEACH PLEASE 2026 - ULTRA SPEED BOT ⚡")
    print("=" * 50)
    print(f"📅 {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("⚡ REFRESH: la 0.2 secunde")
    print("⚡ EXECUȚIE: sub 2 secunde")
    print("🎯 Pentru rulare PARALEL")
    print("=" * 50)
    
    bot = BeachPleaseUltraSpeed()
    success = bot.run_ultra_monitoring()
    
    if success:
        print("\n✅ ULTRA-SPEED COMPLETE!")
    else:
        print("\n❌ Check logs")
