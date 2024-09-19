import time
from appium import webdriver
from appium.options.common import AppiumOptions

APPIUM = "http://localhost:4723"
CAPS = {
    "platformName": "iOS",
    "appium:options": {
        "platformVersion": "17.7",
        "deviceName": "iPhone 15 Plus",
        "automationName": "XCUITest",
        "bundleId": "<com.companyname.appid>", # or "app": "path/to/testapp.ipa", eg.: "https://github.com/saucelabs/sample-app-mobile/releases/download/2.7.1/iOS.RealDevice.SauceLabs.Mobile.Sample.app.2.7.1.ipa"
        "udid": "<device_udid>",  # or "auto" for a single device
        "xcodeOrgId": "<org_unit_number>",
        "xcodeSigningId": "iPhone Developer",
        "updatedWDABundleId": "<com.companyname.wda>",
        "showXcodeLog": True, # optional - shows xcodebuild's log details
        "noReset": True # optional
    }
}
OPTIONS = AppiumOptions().load_capabilities(CAPS)
driver = webdriver.Remote(
    command_executor=APPIUM,
    options=OPTIONS
)

time.sleep(3) # for demo only

# test code

driver.quit()
