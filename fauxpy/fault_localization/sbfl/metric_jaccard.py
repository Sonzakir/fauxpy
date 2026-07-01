class MetricJaccard:
    def __init__(self, epsilon: float):
        self._metric_name = "Jaccard"
        self._epsilon = epsilon

    def get_metric_name(self):
        return self._metric_name

    def compute(self, ef, ep, nf, np):
        score = float(ef) / (ef + nf + ep + self._epsilon)
        return score
