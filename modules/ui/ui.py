from .badges_card import BADGESCard
from .economy_card import ECONOMYCard
from .profile_card import PROFILECard
from .stats_card import STATSCard
from .xp_card import XPCard


class UIManager:
    def __init__(self):

        self.card = XPCard()
        self.profile = PROFILECard()
        self.stats = STATSCard()
        self.badges = BADGESCard()
        self.economy = ECONOMYCard()
        # self.leaderboard = LeaderboardCard()
