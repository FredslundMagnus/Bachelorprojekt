
# Parameters

    Name :                      causal1_9x9-0
    Main :                      teleport
    Level :                     Levels.Causal1
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
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.98
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
  File "main.py", line 106, in <module>
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
  File "/appl/python/3.8.4/lib/python3.8/pstats.py", line 124, in load_stats
    self.stats = marshal.load(f)
EOFError: EOF read where object expected

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-14>
Subject: Job 9434608: <causal1_9x9_0> in cluster <dcc> Exited

Job <causal1_9x9_0> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Thu Mar 18 20:16:26 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Mar 18 20:16:27 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 18 20:16:27 2021
Terminated at Fri Mar 19 08:11:42 2021
Results reported at Fri Mar 19 08:11:42 2021

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

    CPU time :                                   42793.97 sec.
    Max Memory :                                 2447 MB
    Average Memory :                             2430.84 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5745.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42959 sec.
    Turnaround time :                            42916 sec.

The output (if any) is above this job summary.

