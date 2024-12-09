from seleniumbase import SB

def test_bigwigpc():
    with SB(uc=True, test=True, locale_code="en", ad_block=True) as sb:
        url = "https://bigwigpc.com/"
        sb.activate_cdp_mode(url)
        sb.sleep(3.2)
        sb.cdp.type('input[name="s"]', "")
        sb.sleep(1.2)
        sb.cdp.select_option_by_text('select[name="product_cat"]', "Docking Stations (3)")
        sb.sleep(2.5)
        sb.cdp.click("button.header-search-button")
        sb.sleep(5)
        sb.cdp.scroll_down(amount=50)
        sb.sleep(2)
        sb.cdp.scroll_down(amount=50)
        sb.sleep(3)
        sb.cdp.scroll_down(amount=50)
        sb.sleep(5)
        sb.cdp.scroll_down(amount=50)
        sb.sleep(10)
