class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize:
            return False

        count_dic = collections.Counter(hand)
        hand.sort()
        for n in hand:
            if count_dic[n] > 0:
                for n_check in range(n, n + groupSize):
                    if count_dic[n_check] < 1:
                        return False
                    else:
                        count_dic[n_check] -= 1
        
        return True
