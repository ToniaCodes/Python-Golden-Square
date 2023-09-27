from lib.gratitudes import *

def test_add_gratitude():
    gratitude_list = Gratitudes()
    gratitude_list.add("Family")
    gratitude_list.add("Health")
    assert gratitude_list.gratitudes == ["Family", "Health"]

def test_format_gratitudes():
    gratitude_list = Gratitudes()
    gratitude_list.add("Family")
    gratitude_list.add("Health")
    formatted = gratitude_list.format()
    assert formatted == "Be grateful for: Family, Health"