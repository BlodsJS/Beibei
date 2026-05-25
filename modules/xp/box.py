class BOXHandler:
    async def check_box(self, box, data):
        if box["target"] >= 300:
            # executa a caixa
            print("box cheia")
            return "ready"
        box["target"] += 1
        box["xp"] += data["xp"]["level"]
        return None
