import datetime

import pytest

from book.tests.factories import BookFactory
from target.services import ProgressService
from target.tests.factories import TargetFactory


@pytest.mark.django_db
class TestProgressService(object):
    def test_get_goal_per_day_should_return_fifty(self):
        today_date = datetime.datetime.now()
        end_date = today_date + datetime.timedelta(days=5)
        book = BookFactory(page_count=500)
        book.save()
        target = TargetFactory(
            end_date=end_date, start_date=today_date, current_page_progress=250, book=book
        )
        target.save()

        date_diff = end_date.date() - today_date.date()
        pages_per_day = (book.page_count - target.current_page_progress) / date_diff.days

        goal_value = ProgressService(target).get_pages_daily_target()

        assert goal_value == pages_per_day
