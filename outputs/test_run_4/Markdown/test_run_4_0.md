Traceback (most recent call last):
  File "main.py", line 30, in <module>
    run(Defaults, main)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 74, in run
    (serverRun if isServer else main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 28, in serverRun
    showParams(params)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 96, in showParams
    if timer.error:
AttributeError: 'Timer' object has no attribute 'error'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9335752: <test_run_4_0> in cluster <dcc> Exited

Job <test_run_4_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Sat Feb 27 17:29:28 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Feb 27 17:29:29 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Feb 27 17:29:29 2021
Terminated at Sat Feb 27 17:36:58 2021
Results reported at Sat Feb 27 17:36:58 2021

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

    CPU time :                                   422.80 sec.
    Max Memory :                                 2059 MB
    Average Memory :                             1844.80 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               6133.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   494 sec.
    Turnaround time :                            450 sec.

The output (if any) is above this job summary.

