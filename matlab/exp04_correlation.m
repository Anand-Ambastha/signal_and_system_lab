% Experiment 4: Autocorrelation and cross-correlation of sequences
clc; clear; close all;
x = [1 2 3 4 5 6];
y = [2 1 0 3 1 4];
% Using conv with the time-reversed sequence (no toolbox needed)
rxx = conv(x, fliplr(x));
rxy = conv(x, fliplr(y));       % lag convention: sum x[n+l] y[n]
lags = -(length(x)-1):(length(x)-1);
disp('Autocorrelation Rxx ='); disp(rxx)
disp('Cross-correlation Rxy ='); disp(rxy)
fprintf('Rxx peak at lag %d (value = energy = %d)\n', lags(rxx == max(rxx)), sum(x.^2));

f = figure('Position', [100 100 900 650]);
subplot(2,2,1); stem(x); grid on; title('x[n]');
subplot(2,2,2); stem(y); grid on; title('y[n]');
subplot(2,2,3); stem(lags, rxx); grid on; title('Autocorrelation R_{xx}[l]'); xlabel('lag l');
subplot(2,2,4); stem(lags, rxy); grid on; title('Cross-correlation R_{xy}[l]'); xlabel('lag l');
save_fig(f, 'exp04_correlation.png');
