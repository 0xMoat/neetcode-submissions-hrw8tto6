class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        count_dic = {}
        for i, n in enumerate(hand):
            count_dic[n] = 1 + count_dic.get(n, 0)
        
        hand.sort()
        for n in hand:
            if count_dic[n] > 0:
                for n_check in range(n, n + groupSize):
                    if n_check not in count_dic or count_dic[n_check] < 1:
                        return False
                    else:
                        count_dic[n_check] -= 1
        
        return True
