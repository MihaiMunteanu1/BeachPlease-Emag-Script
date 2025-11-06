#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
BEACH PLEASE 2026 - EXECUȚIE RAPIDĂ
Monitorizare normală, execuție RAPIDĂ când găsește butonul
"""

import time
import logging
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s',
    handlers=[
        logging.FileHandler('beach_please_fast.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)


class BeachPleaseFastBot:
    def __init__(self):
        self.driver = None
        self.checkout_url = "https://www.emag.ro/cart/checkout"
        self.check_count = 0
        self.start_time = None

        # Setări RAPIDE pentru execuție
        self.max_retries_fast = 5  # Mai puține retry-uri pentru viteză
        self.retry_delay_fast = 0.6  # Delay mai mic între retry-uri
        self.step_delay_fast = 0.2  # Pauze foarte mici între pași

    def setup_fast_driver(self):
        """Setup optimizat pentru viteză"""
        try:
            options = Options()
            options.add_argument('--no-sandbox')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--disable-blink-features=AutomationControlled')
            options.add_argument('--disable-images')  # Pentru viteză
            options.add_argument('--disable-extensions')
            options.add_argument('--disable-plugins')
            options.add_argument('--disable-background-timer-throttling')
            options.add_experimental_option("excludeSwitches", ["enable-automation"])
            options.add_experimental_option('useAutomationExtension', False)

            self.driver = webdriver.Chrome(options=options)
            self.driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

            # Settings pentru viteză + stabilitate
            self.driver.set_page_load_timeout(10)  # Redus pentru viteză
            self.driver.implicitly_wait(1)  # Foarte rapid
            self.driver.set_window_size(1920, 1080)

            logging.info("🚀 FAST Bot WebDriver initialized")
            return True

        except Exception as e:
            logging.error(f"❌ Setup failed: {e}")
            return False


    def prepare_fast_monitoring(self):
        """Pregătește monitorizarea rapidă"""
        print("\n🎪 BEACH PLEASE 2026 - BOT RAPID 🎪")
        print("=" * 60)
        print(f"📅 Data: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"👤 User: MihaiMunteanu1")
        print("⚡ Mod: RAPID după detectare")
        print("=" * 60)
        print("📋 PREGĂTIRE:")
        print("📋 1. Navighează MANUAL la Beach Please 2026")
        print("📋 2. Rămâi pe pagina biletului")
        print("📋 3. Apasă ENTER pentru start")
        print("=" * 60)
        print("⚡ EXECUȚIE RAPIDĂ:")
        print("⚡ - Monitorizare: 1 secundă între verificări")
        print("⚡ - Execuție: 0.3 secunde între pași")
        print("⚡ - Retry: maximum 5 încercări rapide")
        print("⚡ - Target: sub 3 secunde total")
        print("=" * 60)

        # Preia controlul
        self.driver.get("https://www.emag.ro")

        input("\n🚀 Du-te pe Beach Please 2026 și apasă ENTER >>> ")

        current_url = self.driver.current_url
        page_title = self.driver.title

        print(f"✅ Control preluat!")
        print(f"📋 URL: {current_url}")
        print(f"📋 Titlu: {page_title}")

        self.start_time = datetime.now()

        print(f"\n⚡ MONITORIZARE RAPIDĂ ACTIVATĂ!")
        print(f"🕐 Start: {self.start_time.strftime('%H:%M:%S')}")
        print("=" * 60)

        return True

    def check_for_add_button(self):
        """Verifică rapid pentru buton pe pagina curentă"""
        try:
            # Refresh rapid
            self.driver.refresh()
            time.sleep(0.3)  # Pauză minimă

            # Selectori pentru "Adaugă în coș"
            selectors = [
                "button.yeahIWantThisProduct",
                "button[data-test='main-add-to-cart-button']",
                "button[data-offer-id]:not([disabled])",
                "//button[contains(text(), 'Adauga in Cos')]"
            ]

            for selector in selectors:
                try:
                    if selector.startswith('//'):
                        element = self.driver.find_element(By.XPATH, selector)
                    else:
                        element = self.driver.find_element(By.CSS_SELECTOR, selector)

                    if element.is_displayed() and element.is_enabled():
                        button_text = element.text.strip().lower()
                        if any(word in button_text for word in ['adauga', 'cos', 'cumpara']):
                            return element
                except:
                    continue

            return None

        except Exception:
            return None

    def lightning_add_to_cart(self, add_button):
        """Adăugare FULGER în coș"""
        print("⚡ [1/3] ADĂUGARE FULGER...")

        for attempt in range(self.max_retries_fast):
            try:
                # Click instant
                self.driver.execute_script("arguments[0].click();", add_button)

                time.sleep(self.step_delay_fast)  # Pauză minimă
                return True

            except Exception as e:
                if attempt < self.max_retries_fast - 1:
                    time.sleep(self.retry_delay_fast)  # Retry rapid
                    continue
                else:
                    print(f"❌ Adăugare eșuată!")
                    return False

        return False

    def lightning_checkout(self):
        """Checkout FULGER"""
        print("⚡ [2/3] CHECKOUT FULGER...")

        time.sleep(self.step_delay_fast)  # Pauză minimă

        for attempt in range(self.max_retries_fast):
            try:
                # Navigare instant
                self.driver.get(self.checkout_url)

                # Wait minimal pentru încărcare
                WebDriverWait(self.driver, 6).until(
                    EC.presence_of_element_located((By.TAG_NAME, "body"))
                )

                # print(f"✅ CHECKOUT! (#{attempt + 1})")
                # logging.info(f"✅ Checkout rapid la attempt {attempt + 1}")

                time.sleep(self.step_delay_fast)  # Pauză minimă
                return True

            except Exception as e:
                if attempt < self.max_retries_fast - 1:
                    time.sleep(self.retry_delay_fast)  # Retry rapid
                    continue
                else:
                    print(f"❌ Checkout eșuat!")
                    return False

        return False

    def lightning_send_order(self):
        """Trimite comandă FULGER"""
        print("⚡ [3/3] TRIMITE FULGER...")

        time.sleep(self.step_delay_fast)  # Pauză minimă

        # Selectori pentru "Trimite comanda"
        selectors = [
            "button[data-test='summarySubmitBtn']",
            "//button[contains(text(), 'Trimite comanda')]",
            "//button[contains(text(), 'Trimite Comanda')]",
            "button[type='submit'][data-type='submit']"
        ]

        for attempt in range(self.max_retries_fast):
            try:
                element_found = None

                # Caută rapid butonul
                for selector in selectors:
                    try:
                        if selector.startswith('//'):
                            element = WebDriverWait(self.driver, 3).until(
                                EC.element_to_be_clickable((By.XPATH, selector))
                            )
                        else:
                            element = WebDriverWait(self.driver, 3).until(
                                EC.element_to_be_clickable((By.CSS_SELECTOR, selector))
                            )

                        if element.is_displayed() and element.is_enabled():
                            element_found = element
                            break
                    except:
                        continue

                if element_found:
                    # Click instant fără scroll lung
                    self.driver.execute_script("arguments[0].click();", element_found)

                    print(f"✅ COMANDĂ TRIMISĂ! (#{attempt + 1})")
                    logging.info(f"✅ Comandă trimisă rapid la attempt {attempt + 1}")

                    time.sleep(1)  # Pauză pentru procesare
                    return True
                else:
                    raise Exception("Buton nu găsit")

            except Exception as e:
                if attempt < self.max_retries_fast - 1:
                    time.sleep(self.retry_delay_fast)  # Retry rapid
                    # Refresh rapid pentru retry
                    try:
                        self.driver.refresh()
                        time.sleep(1)
                    except:
                        pass
                    continue
                else:
                    print(f"❌ Trimitere eșuată!")
                    return False

        return False

    def execute_lightning_purchase(self, add_button):
        """Execuție FULGER când găsește butonul"""
        purchase_start = time.time()
        detection_time = datetime.now().strftime('%H:%M:%S')

        print(f"\n{'⚡' * 35}")
        print(f"🚨 BEACH PLEASE 2026 - EXECUȚIE FULGER! 🚨")
        print(f"⏰ Detectare: {detection_time}")
        print(f"👤 User: MihaiMunteanu1")
        print(f"🎯 Target: SUB 3 SECUNDE!")
        print(f"{'⚡' * 35}")

        logging.info(f"🎯 BUTON DETECTAT - început execuție fulger la {detection_time}")

        success_steps = 0

        # ETAPA 1: Adăugare FULGER
        if self.lightning_add_to_cart(add_button):
            success_steps += 1
        else:
            print("❌ STOP la adăugare!")
            return False

        # ETAPA 2: Checkout FULGER
        if self.lightning_checkout():
            success_steps += 1
        else:
            print("❌ STOP la checkout!")
            return False

        # ETAPA 3: Trimite FULGER
        if self.lightning_send_order():
            success_steps += 1
        else:
            print("❌ STOP la trimitere!")
            return False

        # SUCCES FULGER!
        total_time = time.time() - purchase_start

        print(f"\n{'🏆' * 40}")
        print(f"🎪 BEACH PLEASE 2026 - FULGER SUCCES! 🎪")
        print(f"👤 Cumpărător: MihaiMunteanu1")
        print(f"⚡ TIMP FULGER: {total_time:.2f} secunde")
        print(f"📊 Pași: {success_steps}/3 completați")
        print(f"⏰ Finalizare: {datetime.now().strftime('%H:%M:%S')}")

        # Verificare finală
        time.sleep(1)
        final_url = self.driver.current_url
        print(f"📋 URL final: {final_url}")

        if "pay.emag.ro" in final_url:
            print(f"💳 ✅ PERFECT! La plată!")
            logging.info("💳 SUCCES FULGER! La plată!")
        elif total_time < 3.0:
            print(f"🔥 FULGER SUB 3 SECUNDE!")

        print(f"🏆" * 40)

        logging.info(f"🎉 SUCCES FULGER în {total_time:.2f} secunde!")

        return True

    def run_fast_monitoring(self):
        """Monitorizare cu execuție rapidă"""
        try:
            # Setup
            if not self.setup_fast_driver():
                return False

            # Pregătire
            if not self.prepare_fast_monitoring():
                return False

            # MONITORIZARE CU EXECUȚIE RAPIDĂ
            while True:
                try:
                    self.check_count += 1
                    current_time = datetime.now()

                    # Verifică pentru buton
                    add_button = self.check_for_add_button()

                    if add_button:
                        # BUTON GĂSIT - EXECUȚIE FULGER!
                        print(f"\n🎯 BUTON GĂSIT - EXECUȚIE FULGER!")
                        logging.info(f"🎯 Buton detectat la check #{self.check_count}")

                        success = self.execute_lightning_purchase(add_button)

                        if success:
                            print("\n🎉 MISIUNE FULGER FINALIZATĂ!")
                            break
                        else:
                            print("\n⚠️ Execuție incompletă!")
                            break

                    # Status la 2 minute
                    # if self.check_count % 120 == 0:
                    #     elapsed = current_time - self.start_time
                    #     minutes = elapsed.total_seconds() // 60
                    #
                    #     status = f"📊 Check #{self.check_count} | {current_time.strftime('%H:%M:%S')} | {minutes:.0f}m"
                    #     print(status)
                    #     logging.info(status)

                    # Pauză normală între verificări
                    time.sleep(0.8)

                except KeyboardInterrupt:
                    print(f"\n🛑 MONITORIZARE OPRITĂ")
                    print(f"📊 Verificări: {self.check_count}")
                    print(f"🕐 Runtime: {datetime.now() - self.start_time}")
                    break

                except Exception as e:
                    logging.error(f"❌ Eroare: {e}")
                    time.sleep(2)
                    continue

            return True

        finally:
            if self.driver:
                print("\n📋 Monitorizare încheiată!")
                input("Apasă ENTER pentru închidere...")
                self.driver.quit()


if __name__ == "__main__":
    print("🎪 BEACH PLEASE 2026 - BOT FULGER 🎪")
    print("=" * 50)
    print(f"📅 Current: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print("⚡ Execuție FULGER după detectare")
    print("🎯 Target: SUB 3 secunde")
    print("=" * 50)

    bot = BeachPleaseFastBot()
    success = bot.run_fast_monitoring()

    if success:
        print("\n✅ BOT FULGER FINALIZAT!")
    else:
        print("\n❌ Verifică log-urile")
