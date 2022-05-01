# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 17:44:04 2022

@author: Christophe
"""
from tensorflow.python.summary.summary_iterator import summary_iterator
import matplotlib.pyplot as plt
import sys
import argparse



TAG_NAME = "Eval_AverageReturn"

# print(sys.argv)
files = []
labels = []
if len(sys.argv) > 1:
  n_file  = int(sys.argv[1])
  for i in range(0, n_file):
    files.append(sys.argv[i+2])
  for i in range(0, n_file):
    labels.append(sys.argv[i+2+n_file])

else:
  tf_event_file = "/content/cs285_f2021/homework_fall2021/hw2/data/q1_sb_no_rtg_dsa_CartPole-v0_07-02-2022_18-33-59/events.out.tfevents.1644258876.93f54620eca3"
  tf_event_file2 = "/content/cs285_f2021/homework_fall2021/hw2/data/q1_sb_rtg_dsa_CartPole-v0_07-02-2022_18-36-53/events.out.tfevents.1644259017.93f54620eca3"
  tf_event_file3 = "/content/cs285_f2021/homework_fall2021/hw2/data/q1_sb_rtg_na_CartPole-v0_07-02-2022_18-39-53/events.out.tfevents.1644259196.93f54620eca3"
  files = [tf_event_file, tf_event_file2, tf_event_file3]
  labels = ["sb_no_rtg_dsa", "sb_rtg_dsa", 'sb_rtg_na']
#Add your file paths here

#Add the labels for the plot of each file


value_list = []
plt.figure(figsize=(8,6))

for i in range(len(files)):
  for e in summary_iterator(files[i]):
    for v in e.summary.value:
        if v.tag == TAG_NAME:
            value = v.simple_value
            value_list.append(value)
  plt.plot(value_list, label=labels[i])
  value_list = []

plt.legend()
plt.xlabel("Epochs")
plt.ylabel("Eval_AverageReturn")
plt.title("Learning Curves Comparison for small batch sizes on HalfCheetah-v2 env with b50000_r0.02")
plt.grid()
plt.show()

# how to you? python plot_tf_ev...py nbfile file1 file2 ... filen label1 lable2 ... labeln
# ex: python plot_tf_ev.py 2 path/log1/event.out path/log2/event.out hopper1_b300_lr0.02 hopper1_b500_lr0.05