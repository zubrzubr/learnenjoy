import datetime


class ProgressService(object):
    """
    Logic to calculate common operation for target's progress
    """
    def __init__(self, target_instance):
        self.target_instance = target_instance

    def get_pages_daily_target(self):
        """
        Calculates pages which user should read every day to achieve the goal
        :return: int count of pages per day
        """
        end_date = self.target_instance.end_date
        today_date = datetime.datetime.today().date()
        if isinstance(end_date, datetime.datetime):
            end_date = end_date.date()
        if end_date < today_date:
            return
        date_diff = end_date - datetime.datetime.today().date()
        pages_diff = (self.target_instance.book.page_count - self.target_instance.current_page_progress)
        daily_target = pages_diff / date_diff.days

        return round(daily_target, 1)
