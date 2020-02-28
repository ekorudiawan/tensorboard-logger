import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time 
import os

class Logger(object):
    def __init__(self, log_dir):
        super(Logger, self).__init__()
        self.log_dir = log_dir
        self.writer = tf.summary.FileWriter(self.log_dir)
    
    def add_scalar(self, tag_name, value, step):
        summary = tf.Summary(value=[tf.Summary.Value(tag=tag_name, simple_value=value)])
        self.writer.add_summary(summary, step)

class Plotter(object):
    def __init__(self, log_dir):
        super(Plotter, self).__init__()
        event_file = os.listdir(log_dir)
        self.event_file = os.path.join(LOG_DIR, event_file[0])
        sns.set()
    
    def plot(self, tag_name, title=None):
        list_values = []
        for e in tf.train.summary_iterator(self.event_file):
            for v in e.summary.value:
                if v.tag == tag_name:
                    list_values.append(v.simple_value)
        fig, ax = plt.subplots()
        n = np.arange(len(list_values))
        ax.plot(n, list_values)
        ax.set_xlabel("n-data")
        ax.set_ylabel(tag_name)
        if title != None:
            ax.set_title(title)

if __name__ == "__main__":
    LOG_DIR = "log/record_1"
    TAG_NAME = "sensor_1"
    # logger = Logger(LOG_DIR)
    # for i in range(1000):
    #     random_value = np.random.randn()
    #     logger.add_scalar(TAG_NAME, random_value, i)
    #     time.sleep(0.01)
    plotter = Plotter(LOG_DIR)
    plotter.plot(TAG_NAME, title="Sensor Data")
    plt.show()