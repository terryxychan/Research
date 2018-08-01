filename = 'ft_data.csv';
M = csvread(filename);
Fx = M(:,1);
Fy = M(:,2);
Fz = M(:,3);
Mx = M(:,4);
My = M(:,5);
Mz = M(:,6);
[t,y]=size(Fx);
time = 1:1:t;
plot(time,Fx)
hold on
plot(time,Fy);
hold on
plot(time,Fz);
hold on
plot(time,Mx);
hold on
plot(time,My);
hold on
plot(time,Mz);
%plot(time,Fz);
legend('Fx','Fy','Fz','Mx','My','Mz');
title('Force Torque Sensor Response');
