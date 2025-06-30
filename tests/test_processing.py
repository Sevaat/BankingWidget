import src.processing as processing


def test_filter_by_state_executed(datas, datas_state_executed):
    assert processing.filter_by_state(datas, state="EXECUTED") == datas_state_executed


def test_filter_by_state_canceled(datas, datas_state_canceled):
    assert processing.filter_by_state(datas, state="CANCELED") == datas_state_canceled


def test_sort_by_date_down(datas, datas_date_down):
    assert processing.sort_by_date(datas, order=True) == datas_date_down


def test_sort_by_date_up(datas, datas_date_down):
    datas_date_down.reverse()
    assert processing.sort_by_date(datas, order=False) == datas_date_down
