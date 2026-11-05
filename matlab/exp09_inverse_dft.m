% Experiment 9 (also CBS 2): Synthesis of a signal using the inverse DFT
clc; clear; close all;
N = 64; fs = 64; n = 0:N-1; t = n/fs;
X = zeros(1, N);
X(5+1)  = N/2 * 1.0;                      X(N-5+1)  = conj(X(5+1));
X(12+1) = N/2 * 0.5 * exp(1j*pi/2);       X(N-12+1) = conj(X(12+1));

x_manual = zeros(1, N);
for nn = n
    x_manual(nn+1) = real(sum(X .* exp(1j*2*pi*(0:N-1)*nn/N)) / N);
end
x_ifft = real(ifft(X));
expected = cos(2*pi*5*t) + 0.5*cos(2*pi*12*t + pi/2);
fprintf('Manual IDFT == ifft : %d\n', all(abs(x_manual - x_ifft) < 1e-10));
fprintf('Synthesised == expected : %d\n', all(abs(x_ifft - expected) < 1e-10));

f = figure('Position', [100 100 800 800]);
subplot(3,1,1); stem(n, abs(X)); grid on; title('Designed spectrum |X[k]|'); xlabel('k');
ph = angle(X); ph(abs(X) < 1e-9) = 0;
subplot(3,1,2); stem(n, ph); grid on; title('Designed phase \angle X[k]'); xlabel('k'); ylabel('rad');
subplot(3,1,3); plot(t, x_ifft, 'o-', t, expected, '--'); grid on;
title('Synthesised time signal'); xlabel('t (s)'); legend('IDFT synthesis', 'expected');
save_fig(f, 'exp09_inverse_dft.png');
