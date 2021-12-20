import statistics as st
class StatsData:
    def __init__(self, num):
        self.l_data = num
        self.mean = st.mean(num)
        self.median = st.median(num)
        self.variance = st.variance(num)
