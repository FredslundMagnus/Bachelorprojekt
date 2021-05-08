
------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9621666: <Maze_Conver4_3counterfacts_1> in cluster <dcc> Exited

Job <Maze_Conver4_3counterfacts_1> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Fri May  7 14:35:36 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat May  8 14:45:28 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  8 14:45:28 2021
Terminated at Sat May  8 21:32:58 2021
Results reported at Sat May  8 21:32:58 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
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

python main.py $MYARGS


------------------------------------------------------------

Exited.


The output (if any) is above this job summary.

