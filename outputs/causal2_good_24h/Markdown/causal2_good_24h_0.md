
# Parameters

    Name :                      causal2_good_24h-0
    Main :                      teleport
    Level :                     Levels.Causal2
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling

Traceback (most recent call last):
  File "main.py", line 147, in <module>
    run(Defaults)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 36, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 59, in profilingStats
    p = Stats('stats')
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 96, in __init__
    self.init(arg)
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 110, in init
    self.load_stats(arg)
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 123, in load_stats
    with open(arg, 'rb') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9474547: <causal2_good_24h_0> in cluster <dcc> Exited

Job <causal2_good_24h_0> was submitted from host <n-62-27-21> by user <s183905> in cluster <dcc> at Sun Mar 28 11:07:13 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Mar 28 11:07:13 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Mar 28 11:07:13 2021
Terminated at Mon Mar 29 11:02:39 2021
Results reported at Mon Mar 29 11:02:39 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
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

    CPU time :                                   85901.38 sec.
    Max Memory :                                 2822 MB
    Average Memory :                             2816.49 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13562.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86151 sec.
    Turnaround time :                            86126 sec.

The output (if any) is above this job summary.

