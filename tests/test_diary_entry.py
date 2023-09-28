import pytest
from lib.diary_entry import DiaryEntry

def test_format_is_correct():
    diaryentry = DiaryEntry("My Title", "These are the contents")
    result = diaryentry.format()
    assert result == "My Title: These are the contents"

def test_count_words():
    diaryentry = DiaryEntry("My Title", "These are the contents")
    result = diaryentry.count_words()
    assert result == 4

def test_reading_time():
    diaryentry = DiaryEntry("My Title", "These are the contents")
    result = diaryentry.reading_time(1)
    assert result == 4

def test_reading_chunk():
    diaryentry = DiaryEntry("My Title", "These are the contents")
    result = diaryentry.reading_chunk(1, 2)
    assert result == "These are"