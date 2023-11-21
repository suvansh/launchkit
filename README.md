# Launcher Util
This repo aims to isolate the launching / hyperparameter sweep capabilities of [https://github.com/rail-berkeley/rlkit/blob/master/rlkit/launchers/launcher_util.py](RLKit's Launcher). Consult this repository for further documentation and explanation of settings, some of which may not be used in this repo.

## Dependencies
Install and check out [https://github.com/justinjfu/doodad](Doodad), used for launching experiments on EC2 and GCP instances. Otherwise, launchkit runs experiments locally (mode `here_no_doodad`) by default.

## See also
Check out [https://github.com/vitchyr/viskit](Viskit) for inspecting and visualizing results of hyperparameter sweeps. This launchkit saves experiment outputs in a way that is compatible with viskit.