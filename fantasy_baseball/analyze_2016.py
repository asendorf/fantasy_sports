import numpy as np
import matplotlib.pyplot as plt;

if __name__ == "__main__":

    data=np.genfromtxt('/home/asendorf/Dropbox/MATLAB/fantasy/league_stats_2017.csv',delimiter=',');

    runs = data[1:,2];
    hrs = data[1:,3];
    rbis = data[1:,4];
    sbs = data[1:,5];
    obp = data[1:,6];
    slg = data[1:,7];
    ip = data[1:,9];
    ks = data[1:,10];
    ws = data[1:,11];
    era = data[1:,12];
    whip = data[1:,13];
    svhd = data[1:,14];

    wins = np.zeros((10,19));
    ties = np.zeros((10,19));
    losses = np.zeros((10,19));

    for week in range(19):
        
        ind = week*11;

        curr_runs = list(runs[ind:ind+10]);
        curr_hrs = list(hrs[ind:ind+10]);
        curr_rbis = list(rbis[ind:ind+10]);
        curr_sbs = list(sbs[ind:ind+10]);
        curr_obp = list(obp[ind:ind+10]);
        curr_slg = list(slg[ind:ind+10]);
        curr_ip = list(ip[ind:ind+10]);
        curr_ks = list(ks[ind:ind+10]);
        curr_ws = list(ws[ind:ind+10]);
        curr_era = list(era[ind:ind+10]);
        curr_whip = list(whip[ind:ind+10]);
        curr_svhd = list(svhd[ind:ind+10]);

        curr_stats = [curr_runs,curr_hrs,curr_rbis,curr_sbs,curr_obp,curr_slg,curr_ip,curr_ks,curr_ws,curr_era,curr_whip,curr_svhd];

        for team in range(10):
            for stat in range(12):
                
                curr_stat = curr_stats[stat]
                if stat in [0,1,2,3,4,5,6,7,8,11]:
                    wins[team,week] = wins[team,week] + sum(curr_stat[team] > curr_stat[:team] + curr_stat[team+1:]);
                    losses[team,week] = losses[team,week] + sum(curr_stat[team] < curr_stat[:team] + curr_stat[team+1:]);
                    ties[team,week] = ties[team,week] + sum(curr_stat[team] == curr_stat[:team] + curr_stat[team+1:]);
                else:
                    wins[team,week] = wins[team,week] + sum(curr_stat[team] < curr_stat[:team] + curr_stat[team+1:]);
                    losses[team,week] = losses[team,week] + sum(curr_stat[team] > curr_stat[:team] + curr_stat[team+1:]);
                    ties[team,week] = ties[team,week] + sum(curr_stat[team] == curr_stat[:team] + curr_stat[team+1:]);

#    plt.figure();
#    plt.plot(sum(wins,1))
#    plt.show();
#    plt.figure();
#    plt.plot(sum(losses,1))
#    plt.show()
#    plt.figure();
#    plt.plot(sum(ties,1))
#    plt.show()

    full_win_perc = np.zeros((10,1));
    #2016: true_win_perc = [0.561,0.461,0.417,0.421,0.592,0.441,0.544,0.513,0.487,0.564];
    true_win_perc = [0.561,0.557,0.377,0.338,0.607,0.428,0.583,0.469,0.537,0.542];

    for team in range(10):
        full_win_perc[team] = (sum(wins[team,:])+0.5*sum(ties[team,:]))/(2052);
        print "{0}-{1}-{2}: {3}".format(sum(wins[team,:]),sum(losses[team,:]),sum(ties[team,:]),full_win_perc[team,0])

    width = 0.35;    
    ind = np.arange(10);
    plt.figure()
    plt.hold(True)
    rects1=plt.bar(ind,true_win_perc,width,color='b')
    rects2=plt.bar(ind+width,full_win_perc,width,color='r');
    plt.ylabel('Win Percentage',fontsize=16);
    plt.xlabel('Team',fontsize=16)
    plt.title('Actual vs. Full Win Percentage',fontsize=20)
    plt.xticks(ind+width)
    plt.ylim([0.3,0.65])
    plt.xticks(ind+width,['HW','Yelich','Big Unit','Flip','Rafay','BWT','Dead','Manny','Stanton','Trout'])
    plt.legend((rects1[0],rects2[0]),('Head-to-head','Vs. All'),loc='upper right')
    plt.show()

    # Cumulative
    cum_wins = np.cumsum(wins,axis=1)
    cum_ties = np.cumsum(ties,axis=1)
    cumlosses = np.cumsum(losses,axis=1)

    cum_win_perc = np.zeros((10,19));
    for team in range(10):
        for week in range(19):
            cum_win_perc[team,week] = (cum_wins[team,week]+0.5*cum_ties[team,week])/((week+1)*108);


    cm = plt.get_cmap('gist_rainbow')

    plt.figure();
#    plt.gca().set_color_cycle(['red', 'green', 'blue','cyan','magenta','black','yellow'])
#plt.gca().set_color_cycle([cm(1.*i/10) for i in range(10)])
    plt.hold(True)
    my_lines = ['r','orange','y','gold','g','c','b','m','grey','k']

    for ind in range(10):
        plt.plot(range(1,20), cum_win_perc[ind,:],my_lines[ind],linewidth=3)
#    plt.plot(range(1,20),cum_win_perc.T,linewidth=3);
    plt.xlabel('Week',fontsize=16)
    plt.ylabel('Win Percentage',fontsize=16)
    plt.title('Yearly Trend',fontsize=20);
    plt.legend(['HW','Yelich','Big Unit','Flip','Rafay','BWT','Dead','Manny','Stanton','Trout'])
    plt.xlim([1,19])
    plt.ylim([0.15,0.85])
    plt.show()

