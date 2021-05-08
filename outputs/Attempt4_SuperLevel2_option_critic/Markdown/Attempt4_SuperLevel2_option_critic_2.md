
------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9608047: <Attempt4_SuperLevel2_option_critic_2> in cluster <dcc> Exited

Job <Attempt4_SuperLevel2_option_critic_2> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Mon May  3 14:47:45 2021
Job was executed on host(s) <n-62-11-66>, in queue <hpc>, as user <s183914> in cluster <dcc> at Thu May  6 01:28:37 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu May  6 01:28:37 2021
Terminated at Sat May  8 22:30:42 2021
Results reported at Sat May  8 22:30:42 2021

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

