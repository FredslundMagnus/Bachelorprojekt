/zhome/ea/9/137501/.lsbatch/1616682285.9464471.shell: line 14:  4694 Killed                  python main.py $LSB_PROJECT_NAME

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9464471: <causal3_9x9_20hours_0> in cluster <dcc> Exited

Job <causal3_9x9_20hours_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu Mar 25 15:24:45 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Thu Mar 25 15:24:46 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 25 15:24:46 2021
Terminated at Fri Mar 26 11:27:23 2021
Results reported at Fri Mar 26 11:27:23 2021

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

    CPU time :                                   52972.63 sec.
    Max Memory :                                 8192 MB
    Average Memory :                             6322.91 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               0.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   72219 sec.
    Turnaround time :                            72158 sec.

The output (if any) is above this job summary.

