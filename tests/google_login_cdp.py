from seleniumbase import SB

def test_google_login():
    with SB(uc=True, test=True, locale_code="en", ad_block=True) as sb:
        url = "https://www.google.com/"
        sb.activate_cdp_mode(url)
        sb.sleep(3.2)
        
        # Interact with the "Sign In" button
        sb.cdp.click('a[aria-label="Ingia"]')
        sb.sleep(7)
        
        # Enter the email address
        sb.cdp.press_keys("input#identifierId", "laureenchristina@gmail.com")
        sb.sleep(3)
        
        # Click "Next"
        sb.cdp.click('button:contains("Endelea")')
        sb.sleep(8)
        
        # Enter the password
        sb.cdp.press_keys('input[aria-label="Weka nenosiri lako"]', "Billbill98*")
        sb.sleep(6)
        
        # Click "Next" again
        sb.cdp.click('button:contains("Endelea")')
        sb.sleep(10)
