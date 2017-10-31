josh = [74  102 65  95  67  86  113 46  106 86  54 116 68];
pube = [86  92  125 66  115 81  81  70  82  64  84 93  126];
pete = [77  63  104 56  99  82  46  106 63  93  71 103 102];
gore = [98  80  107 74  104 100 117 74  96  73  90 64  89];
burg = [99  94  80  61  76  80  103 96  91  89  59 79  77];
vand = [98  95  105 82  103 125 79  91  69  29  67 99  81];
show = [89  106 118 70  76  68  90  90  92  54  77 117 101];
dick = [111 59  85  108 71  78  105 84  86  59  73 84  96];
jbon = [62  54  74  56  90  75  92  129 106 73  54 53  71];
ease = [121 89  91  120 81  81  99  108 66  63  48 95  65];
rodg = [79  107 86  30  100 97  73  100 140 113 94 97  109];
punn = [77  83  109 80  101 102 85  83  103 96  47 73  82];

all = [josh;pube;pete;gore;burg;vand;show;dick;jbon;ease;rodg;punn];

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

true_wins = [6.5;8;4;7;5;8;8;5;3.5;5;11;7;];

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

% so we want a function that takes who has been picked 