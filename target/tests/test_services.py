import datetime

import pytest

from book.tests.factories import BookFactory
from target.services import ProgressService
from target.tests.factories import TargetFactory


@pytest.mark.django_db
class TestProgressService(object):
    def test_get_goal_per_day_should_return_fifty(self):
        today_date = datetime.datetime.today()
        end_date = today_date + datetime.timedelta(days=5)
        book = BookFactory(page_count=500)
        book.save()
        target = TargetFactory(
            end_date=end_date, start_date=today_date, current_page_progress=250, book=book
        )
        target.save()

        goal_value = ProgressService(target).get_pages_daily_target()
        expected_result = 50

        assert goal_value == expected_result

    def test_get_goal_per_day_should_return_none_if_end_day_less_then_today(self):
        today_date = datetime.datetime.today()
        end_date = today_date - datetime.timedelta(days=5)
        book = BookFactory(page_count=500)
        book.save()
        target = TargetFactory(
            end_date=end_date, start_date=today_date, current_page_progress=250, book=book
        )
        target.save()

        goal_value = ProgressService(target).get_pages_daily_target()

        assert goal_value is None

    def test_get_goal_per_day_should_return_fifty_if_date_object_passed(self):
        today_date = datetime.datetime.today()
        end_date = today_date + datetime.timedelta(days=5)
        book = BookFactory(page_count=500)
        book.save()
        target = TargetFactory(
            end_date=end_date.date(), start_date=today_date, current_page_progress=250, book=book
        )
        target.save()

        goal_value = ProgressService(target).get_pages_daily_target()
        expected_result = 50

        assert goal_value == expected_result
