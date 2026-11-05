% Run every MATLAB experiment; figures are written to ../outputs/matlab/
here = fileparts(mfilename('fullpath'));
cd(here);
files = dir('exp*.m');
for i = 1:numel(files)
    fprintf('\n=== %s ===\n', files(i).name);
    run(files(i).name);
end
