/zhome/ea/9/137501/.lsbatch/1616691068.9465582.shell: line 14: 14268 Killed                  python main.py $LSB_PROJECT_NAME

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-12>
Subject: Job 9465582: <causal3_9x9_20hoursONLYMOVERsoftmaxgam0995_0> in cluster <dcc> Exited

Job <causal3_9x9_20hoursONLYMOVERsoftmaxgam0995_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 17:51:08 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 18:36:59 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 18:36:59 2021
Terminated at Fri Mar 26 11:09:56 2021
Results reported at Fri Mar 26 11:09:56 2021

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

TERM_MEMLIMIT: job killed after reaching LSF memory usage limit.
Exited with exit code 137.

Resource usage summary:

    CPU time :                                   59423.50 sec.
    Max Memory :                                 8192 MB
    Average Memory :                             5102.49 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               0.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   59577 sec.
    Turnaround time :                            62328 sec.

The output (if any) is above this job summary.

