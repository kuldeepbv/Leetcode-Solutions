from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        card_count = Counter(hand)
        unique_cards = sorted(card_count.keys())
        
        for card in unique_cards:
            if card_count[card] > 0:
                num_groups = card_count[card]
                for i in range(groupSize):
                    if card_count[card + i] < num_groups:
                        return False
                    card_count[card + i] -= num_groups
        
        return True