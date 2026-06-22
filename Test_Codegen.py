import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://www.google.com/")
    page.get_by_role("combobox", name="Search").fill("Automation test")
    page.get_by_text("automation testing", exact=True).click()
    page.locator("iframe[name=\"a-cl24thevq9h0\"]").content_frame.get_by_role("checkbox", name="I'm not a robot").click()
    page.get_by_role("link", name="Automation test cases").click()
    page.goto("https://www.zoho.com/qengine/?gad_source=1&gad_campaignid=23662810523&gbraid=0AAAABCv9Px3c80CtGiSZ5nHaXuMsRAjz4&gclid=EAIaIQobChMI8v-f0NqalQMVAIZmAh26vyonEAAYAiAAEgL9E_D_BwE")
    expect(page.locator("body")).to_contain_text("")
    page.locator("span").first.click()
    page.get_by_role("textbox", name="Name *").click()
    page.get_by_role("textbox", name="Business Email *").click()
    page.get_by_role("textbox", name="Phone Number *").click()
    page.get_by_role("textbox", name="Password *").click()