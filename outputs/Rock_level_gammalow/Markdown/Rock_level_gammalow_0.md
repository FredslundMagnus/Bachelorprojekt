
# Parameters

    Name :                      Rock_level_gammalow-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.02
    Gamma :                     0.95
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling

Traceback (most recent call last):
  File "main.py", line 111, in <module>
    run(Defaults)
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 36, in serverRun
    profilingStats()
  File "/zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 59, in profilingStats
    p = Stats('stats')
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 96, in __init__
    self.init(arg)
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 110, in init
    self.load_stats(arg)
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 123, in load_stats
    with open(arg, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9441987: <Rock_level_gammalow_0> in cluster <dcc> Exited

Job <Rock_level_gammalow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:12 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 13:08:38 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 13:08:38 2021
Terminated at Sun Mar 21 01:04:12 2021
Results reported at Sun Mar 21 01:04:12 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=8G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   42802.72 sec.
    Max Memory :                                 6001 MB
    Average Memory :                             4289.00 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2191.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42943 sec.
    Turnaround time :                            85860 sec.

The output (if any) is above this job summary.

