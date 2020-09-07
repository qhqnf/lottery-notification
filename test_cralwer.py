from lottery_crawler import winning_price_cralwer


def test_url():
    winning_price = winning_price_cralwer()
    assert type(winning_price) is int