class NNPrediction:

    def __init__(self):
        self.predict_arr = []

    def predict_bread_sales(self, stat_dict, cond, n):
        for i in stat_dict.values():
            for j in range(len(i)):
                i[j] = (cond[j] - i[j]) ** 2

        for i in stat_dict:
            stat_dict[i] = (sum(stat_dict[i])) ** 0.5

        sorted_bread_stat = dict(sorted(stat_dict.items(), key=lambda x: x[1]))

        for i in sorted_bread_stat.keys():
            self.predict_arr.append(i)

        return sum(self.predict_arr[:3]) / n
