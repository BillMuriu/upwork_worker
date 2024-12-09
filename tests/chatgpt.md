### Step 1: wait fot the page to load.

### Step 2: Click the login button.

    - sb.cdp.click('button:contains("Login")')


    - (Login Button Element): body > div.relative.flex.h-full.w-full.overflow-hidden.transition-colors.z-0 > div.relative.flex.h-full.max-w-full.flex-1.flex-col.overflow-hidden > div.draggable.sticky.top-0.z-10.flex.min-h-\[60px\].items-center.justify-center.border-transparent.bg-token-main-surface-primary.pl-0.md\:hidden > div.no-draggable.absolute.bottom-0.right-0.top-0.mr-3.inline-flex.items-center.justify-center > button.

### Step 3: Move to the login page.

    - Login URL: [https://auth.openai.com/authorize?client_id=TdJIcbe16WoTHtN95nyywh5E4yOo6ItG&scope=openid%20email%20profile%20offline_access%20model.request%20model.read%20organization.read%20organization.write&response_type=code&redirect_uri=https%3A%2F%2Fchatgpt.com%2Fapi%2Fauth%2Fcallback%2Flogin-web&audience=https%3A%2F%2Fapi.openai.com%2Fv1&device_id=011c78c3-5abe-4c47-a8af-3a3fab23015e&prompt=login&screen_hint=login&ext-oai-did=011c78c3-5abe-4c47-a8af-3a3fab23015e&country_code=KE&state=vQQr2kSO0OtC9dK5CeRKsz_uIAMxLzC-TIDcbuKoNjI&code_challenge=WvbC25rw5LkAbZeiQH5fqeMAlRKFAiSHxsbPAw_smxs&code_challenge_method=S256]

### Step 4: Click on Login with Google.

    -(Google Button) -> button:contains("Continue with Google")

### Step 5: Enter Email Adress.

    - sb.cdp.press_keys("input#identifierId", "laureenchristina@gmail.com")

### Step 6: Click on Next.

    -sb.cdp.click('button:contains("Next")')

### Step 7: Enter Password.

    -sb.cdp.press_keys('input[name="Passwd"]', "Billbill98*")

### Step 8: Click on Next.

    -sb.cdp.click('button:contains("Next")')
