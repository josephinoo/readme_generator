from badges import *
from generator import *
badge=Badge("eljoseph","x")
badge.badge_followers()
badge.badge_forks()
print(badge.get_badge())
create_readme(badge.get_badge())