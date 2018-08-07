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
        date_diff = self.target_instance.end_date.date() - datetime.datetime.now().date()
        return (self.target_instance.book.page_count - self.target_instance.current_page_progress) / date_diff.days
