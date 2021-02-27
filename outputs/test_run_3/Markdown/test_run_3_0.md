/zhome/ee/d/137643/.lsbatch/1614443058.9335751.shell: line 14: 11577 Killed                  python main.py $LSB_PROJECT_NAME

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-3>
Subject: Job 9335751: <test_run_3_0> in cluster <dcc> Exited

Job <test_run_3_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Sat Feb 27 17:24:18 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Feb 27 17:24:23 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Feb 27 17:24:23 2021
Terminated at Sat Feb 27 17:24:52 2021
Results reported at Sat Feb 27 17:24:52 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=2G]"
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

    CPU time :                                   4.55 sec.
    Max Memory :                                 2048 MB
    Average Memory :                             1562.00 MB
    Total Requested Memory :                     2048.00 MB
    Delta Memory :                               0.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   33 sec.
    Turnaround time :                            34 sec.

The output (if any) is above this job summary.

