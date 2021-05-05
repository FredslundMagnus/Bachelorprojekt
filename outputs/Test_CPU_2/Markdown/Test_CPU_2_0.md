User defined signal 2

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9603659: <Test_CPU_2_0> in cluster <dcc> Exited

Job <Test_CPU_2_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Sat May  1 14:25:44 2021
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat May  1 14:25:46 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  1 14:25:46 2021
Terminated at Tue May  4 14:26:53 2021
Results reported at Tue May  4 14:26:53 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -n 1
#BSUB -R "rusage[mem=16G]"
#BSUB -R "span[hosts=1]"
#BSUB -W 4320
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $MYARGS
------------------------------------------------------------

TERM_RUNLIMIT: job killed after reaching LSF run time limit.
Exited with exit code 140.

Resource usage summary:

    CPU time :                                   258651.00 sec.
    Max Memory :                                 115 MB
    Average Memory :                             114.98 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               16269.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                6
    Run time :                                   259302 sec.
    Turnaround time :                            259269 sec.

The output (if any) is above this job summary.

