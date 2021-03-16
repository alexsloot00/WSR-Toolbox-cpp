# '''
# (c) REACT LAB, Harvard University
# Author: Ninad Jadhav
# '''

#!/usr/bin/env python3

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import json
import glob, os
import seaborn as sns
import numpy as np

SMALL_SIZE = 8
MEDIUM_SIZE = 10
BIGGER_SIZE = 12

plt.rc('font', size=MEDIUM_SIZE)         # controls default text sizes
plt.rc('axes', titlesize=BIGGER_SIZE)    # fontsize of the axes title
plt.rc('axes', labelsize=BIGGER_SIZE)    # fontsize of the x and y labels
plt.rc('xtick', labelsize=MEDIUM_SIZE)   # fontsize of the tick labels
plt.rc('ytick', labelsize=MEDIUM_SIZE)   # fontsize of the tick labels
plt.rc('legend', fontsize=MEDIUM_SIZE)   # legend fontsize
plt.rc('figure', titlesize=BIGGER_SIZE)  # fontsize of the figure title

def main():

    os.chdir("../debug")
    for traj_file in glob.glob("*.json"):

        if(traj_file.split("_")[2] == "interpl"): 
            continue
        
        f = open("../debug/"+traj_file,"r") 
        data_json = json.loads(f.read())

        #Sort the keys numerically to preserve order.
        d = data_json["channel_packets"]
        data_json_sorted = json.dumps({int(x):d[x] for x in d.keys()}, sort_keys=True)
        data_json = json.loads(data_json_sorted)
        
        print("Channel data for TX Neighbor robot : ", traj_file.split("_")[1], 
              "channel phase data = ", traj_file.split("_")[2])

        traj = pd.DataFrame.from_dict(data_json, orient="index")


        sns.scatterplot(y=traj["center_subcarrier_phase"],
                        x=np.arange(0,len(data_json),1),
                        s=8,
                        marker='x')
        plt.title('RX Robot Channel Phase: ' + traj_file.split("_")[2])
        plt.show()

        sns.scatterplot(y=traj["timestamp"],
                x=np.arange(0,len(data_json),1),
                s=8,
                marker='x')

        plt.title('RX Robot Channel Timestamp: ' + traj_file.split("_")[2])
        plt.show()

        # sns.scatterplot(y=traj["numcpp_center_subcarrier"],
        #         x=np.arange(0,len(data_json["channel_packets"]),1),
        #         s=10,
        #         marker='x')

        # plt.show()

if __name__ == "__main__":
    main()