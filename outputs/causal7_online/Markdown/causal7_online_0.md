Traceback (most recent call last):
  File "main.py", line 9, in <module>
    from allGraphsTrain import graphTrain
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphsTrain.py", line 1, in <module>
    from allGraphs import *
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/allGraphs.py", line 2, in <module>
    from paint import Paint
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/paint.py", line 8, in <module>
    import pygame
ModuleNotFoundError: No module named 'pygame'

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-10>
Subject: Job 9505730: <causal7_online_0> in cluster <dcc> Exited

Job <causal7_online_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Thu Apr  8 23:22:37 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr  8 23:22:47 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr  8 23:22:47 2021
Terminated at Thu Apr  8 23:22:54 2021
Results reported at Thu Apr  8 23:22:54 2021

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

    CPU time :                                   1.26 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   8 sec.
    Turnaround time :                            17 sec.

The output (if any) is above this job summary.

