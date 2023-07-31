from selene.support.shared import browser
from selene import be, have


def test_positive(browser_window_config):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in ...'))


def test_negative (browser_window_config):
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('_1%tyudf;ffsd  dsf').press_enter()
    browser.element('[class="card-section"]').should(have.text('По запросу _1%tyudf;ffsd dsf ничего не найдено. '))



