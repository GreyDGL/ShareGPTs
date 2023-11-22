import undetected_chromedriver as uc

driver = uc.Chrome(headless=True, use_subprocess=False)
driver = uc.Chrome(
    headless=True,
    use_subprocess=False,
    browser_executable_path="/usr/bin/google-chrome",
    driver_executable_path="/tmp/chromedriver",
)

driver.get("https://nowsecure.nl")
driver.save_screenshot("nowsecure.png")
