pill = [111.00, 102.86, 82.48, 87.40, 126.90, 91.46, 94.26, 79.70, 72.74, 98.92, 93.98, 85.54, 119.66];
dick = [92.36, 122.00, 95.94, 68.14, 121.46, 97.40, 125.12, 101.22, 111.56, 85.18, 67.68, 61.86, 85.88];
rave = [100.60, 109.44, 98.44, 114.66, 86.38, 82.98, 128.42, 67.80, 76.94, 68.26, 67.08, 78.02, 82.72];
pube = [113.86, 92.66, 108.56, 116.26, 158.28, 77.00, 85.40, 107.72, 85.36, 124.10, 85.20, 121.34, 130.40];
pete = [72.74, 85.86, 52.88, 73.42, 41.40, 94.92, 35.92, 77.72, 112.54, 98.54, 66.12, 109.46, 107.80];
bone = [70.30, 115.96, 109.86, 76.48, 55.96, 86.56, 89.14, 83.28, 85.18, 86.30, 82.14, 101.84, 57.23];
anal = [105.20, 87.90, 125.70, 91.92, 114.12, 96.76, 79.54, 97.90, 77.56, 58.04, 90.82, 91.26, 73.54];
vand = [50.72, 80.86, 101.12, 127.66, 65.00, 71.90, 65.20, 95.82, 99.18, 105.82, 100.68, 68.44, 102.28];
lamb = [130.68, 104.92, 106.70, 84.62, 66.56, 83.28, 117.04, 125.28, 92.78, 123.46, 101.74, 128.20, 101.30];
tank = [99.96, 93.36, 106.24, 96.12, 85.50, 94.32, 107.64, 97.32, 75.66, 98.18, 101.00, 93.56, 64.36];
show = [108.26, 67.62, 90.90, 96.88, 78.26, 30.96, 68.74, 93.84, 84.58, 92.54, 116.54, 70.32, 58.56];
pats = [68.26, 110.62, 91.28, 86.00, 81.04, 104.18, 73.48, 92.80, 97.60, 78.64, 86.18, 83.44, 91.56];

all = [pill; dick;rave;pube;pete;bone;anal;vand;lamb;tank;show;pats];

avg_score = mean(all,2);

moment2 = std(all,0,2);

expected_wins = zeros(12,13);

for player = 1:12
    for week = 1:13
        inds = 1:12;
        inds = inds([1:(player-1) (player+1):end]);
        
        others = all(inds,week);
        target = all(player,week);
        
        wins = sum(target > others);
        ties = sum(target == others);
        
        expected_wins(player,week) = (wins + ties/2)/11;
    end
end

expected_wins = sum(expected_wins,2);

true_wins = [8;7;4;11;4;5;7;6;7;11;4;4];

diff = true_wins - expected_wins;

all_socres = all(:);
figure; qqplot(all_scores);
mu = mean(all_scores);
standdev = std(all_scores);


x65 = norminv(0.65,mu,standdev);

% So our target points per week is 94


% Her's the Plan
% Let's take last year's draft and look at number of available at each position
% after each round
% So depending on your pick you look at the dfference berween te dropoff
% of who should be available