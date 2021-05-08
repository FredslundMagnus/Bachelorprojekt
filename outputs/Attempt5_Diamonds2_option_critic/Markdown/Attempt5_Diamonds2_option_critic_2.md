
------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9618600: <Attempt5_Diamonds2_option_critic_2> in cluster <dcc> Exited

Job <Attempt5_Diamonds2_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Thu May  6 02:11:24 2021
Job was executed on host(s) <n-62-11-60>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu May  6 13:26:36 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May  6 13:26:36 2021
Terminated at Sat May  8 22:30:41 2021
Results reported at Sat May  8 22:30:41 2021

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

Exited.


The output (if any) is above this job summary.

