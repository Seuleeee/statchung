from stats.models.models import Stats


class StatsService:
    def get_dashboard_stats(self, stat: str, user_id: str) -> str:
        statistics = Stats.objects.filter(create_user=user_id).values_list(stat, flat=True)
        return statistics
