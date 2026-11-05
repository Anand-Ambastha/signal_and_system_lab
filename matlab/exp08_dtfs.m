% Experiment 8: DTFS coefficients of a periodic discrete-time signal
clc; clear; close all;
N = 8; n = 0:N-1;
x = [1 2 3 4 4 3 2 1];
k = 0:N-1;
a = zeros(1, N);
for kk = k
    a(kk+1) = sum(x .* exp(-1j*2*pi*kk*n/N)) / N;
end
disp('DTFS coefficients a_k:'); disp(a.')
fprintf('Check against fft/N: %d\n', all(abs(a - fft(x)/N) < 1e-12));
x_rec = zeros(1, N);
for nn = n
    x_rec(nn+1) = real(sum(a .* exp(1j*2*pi*k*nn/N)));
end
disp('Reconstruction x[n] ='); disp(x_rec)

f = figure('Position', [100 100 700 800]);
subplot(3,1,1); stem(-N:2*N-1, repmat(x, 1, 3)); grid on; title('Periodic signal x[n] (3 periods)'); xlabel('n');
subplot(3,1,2); stem(k, abs(a)); grid on; title('Magnitude |a_k|'); xlabel('k');
ph = angle(a); ph(abs(a) < 1e-9) = 0;
subplot(3,1,3); stem(k, ph); grid on; title('Phase \angle a_k'); xlabel('k'); ylabel('rad');
save_fig(f, 'exp08_dtfs.png');
