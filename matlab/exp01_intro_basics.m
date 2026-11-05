% Experiment 1: Introduction to MATLAB and its basic commands
clc; clear; close all;
a = 5; b = 3;
disp([a+b, a-b, a*b, a/b, a^b])
v = [1 2 3 4 5]
vcol = v'
linspace(0, 1, 5)
0:2:10
A = [1 2; 3 4]; B = [5 6; 7 8];
A*B            % matrix product
A.*B           % element-wise product
A'             % transpose
inv(A)
det(A)
zeros(2,3)
ones(2,3)
eye(3)
z = 3 + 4i;
abs(z), angle(z)
sum(v), mean(v), max(v)
v(2:4)

x = linspace(0, 2*pi, 200);
f = figure;
plot(x, sin(x), x, cos(x), '--'); grid on
title('Basic plotting'); xlabel('x'); ylabel('y'); legend('sin(x)', 'cos(x)');
save_fig(f, 'exp01_basic_plot.png');
