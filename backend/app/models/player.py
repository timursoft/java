class Player:
    def __init__(self, player_id: int, skill_level: int):
        self.id = player_id
        self.skill_level = skill_level

    def __repr__(self):
        return f'<Player id={self.id} skill_level={self.skill_level}>'