/zhome/ee/d/137643/Desktop/Bachelor/project-env/lib/python3.8/site-packages/torch/cuda/__init__.py:52: UserWarning: CUDA initialization: Found no NVIDIA driver on your system. Please check that you have an NVIDIA GPU and installed a driver from http://www.nvidia.com/Download/index.aspx (Triggered internally at  /pytorch/c10/cuda/CUDAFunctions.cpp:100.)
  return torch._C._cuda_getDeviceCount() > 0
Start
True
True
['main.py', '-name', 'Test_CPU_3-0', '-hours', '0.1', '-level', 'Levels.Causal3', '-main', 'option_critic_run', '-batch', '25']

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9603666: <Test_CPU_3_0> in cluster <dcc> Done

Job <Test_CPU_3_0> was submitted from host <n-62-30-3> by user <s183905> in cluster <dcc> at Sat May  1 14:41:06 2021
Job was executed on host(s) <n-62-31-3>, in queue <hpc>, as user <s183905> in cluster <dcc> at Sat May  1 14:41:08 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat May  1 14:41:08 2021
Terminated at Sat May  1 14:41:10 2021
Results reported at Sat May  1 14:41:10 2021

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

Successfully completed.

Resource usage summary:

    CPU time :                                   1.26 sec.
    Max Memory :                                 -
    Average Memory :                             -
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               -
    Max Swap :                                   -
    Max Processes :                              -
    Max Threads :                                -
    Run time :                                   53 sec.
    Turnaround time :                            4 sec.

The output (if any) is above this job summary.

