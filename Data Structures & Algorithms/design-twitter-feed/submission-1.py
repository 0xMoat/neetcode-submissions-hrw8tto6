class Twitter:

    def __init__(self):
        self.time = 0
        self.tweet_map = defaultdict(list) # user_id -> [time, tweet_id]
        self.follow_map = defaultdict(set) # user_id -> follow_ids set

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append([self.time, tweetId])
        self.time -= 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        res = []
        min_heap = []

        self.follow_map[userId].add(userId)
        for followee_id in self.follow_map[userId]:
            if followee_id in self.tweet_map:
                latest_tweet_idx = len(self.tweet_map[followee_id]) - 1
                time, tweet_id = self.tweet_map[followee_id][latest_tweet_idx]
                heapq.heappush(min_heap, [time, tweet_id, followee_id, latest_tweet_idx - 1])

        while min_heap and len(res) < 10:
            time, tweet_id, followee_id, next_latest_tweet_idx = heapq.heappop(min_heap)
            res.append(tweet_id)
            if next_latest_tweet_idx >= 0:
                time, tweet_id = self.tweet_map[followee_id][next_latest_tweet_idx]
                heapq.heappush(min_heap, [time, tweet_id, followee_id, next_latest_tweet_idx - 1])
        
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        
