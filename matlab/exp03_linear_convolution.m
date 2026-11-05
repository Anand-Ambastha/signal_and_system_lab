% Experiment 3: Linear convolution of two sequences
clc; clear; close all;
x = [1 2 3 4];  nx = 0:length(x)-1;
h = [1 1 1];    nh = 0:length(h)-1;

y = zeros(1, length(x) + length(h) - 1);
for n = 1:length(y)
    for k = 1:length(x)
        if (n-k+1 >= 1) && (n-k+1 <= length(h))
            y(n) = y(n) + x(k) * h(n-k+1);
        end
    end
end
ny = 0:length(y)-1;
y_builtin = conv(x, h);
disp('y[n] manual  ='); disp(y)
disp('y[n] conv()  ='); disp(y_builtin)
disp(['Match: ' num2str(isequal(y, y_builtin))])

f = figure('Position', [100 100 600 750]);
subplot(3,1,1); stem(nx, x); grid on; title('x[n]'); xlabel('n');
subplot(3,1,2); stem(nh, h); grid on; title('h[n]'); xlabel('n');
subplot(3,1,3); stem(ny, y); grid on; title('y[n] = x[n] * h[n]'); xlabel('n');
save_fig(f, 'exp03_linear_convolution.png');
