from streamlit.testing.v1 import AppTest
import datetime


"""def test_saledate_is_datetime():
    at= AppTest.from_file("app.py", default_timeout=10).run()
    select_date= datetime.date(2014, 12, 16)
    date = at.dataframe[0].value.loc[0, "saledate"]
    assert select_date == date """

def test_sort_column_with_type():
    at= AppTest.from_file("app.py", default_timeout=10).run()
    at.sidebar.selectbox[0].set_value("year").run()
    at.sidebar.selectbox[1].set_value("Croissant").run()
    index = at.dataframe[0].value.loc[0, "year"]
    assert index == 1984
