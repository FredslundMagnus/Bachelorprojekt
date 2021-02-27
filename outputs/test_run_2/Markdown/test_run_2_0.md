Traceback (most recent call last):
  File "main.py", line 30, in <module>
    run(Defaults, main)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 74, in run
    (serverRun if isServer else main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 28, in serverRun
    showParams(params)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 90, in showParams
    timer = Timer()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 68, in __init__
    cProfile.run(
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 16, in run
    return _pyprofile._Utils(Profile).run(statement, filename, sort)
  File "/appl/python/3.8.4/lib/python3.8/profile.py", line 53, in run
    prof.run(statement)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 95, in run
    return self.runctx(cmd, dict, dict)
  File "/appl/python/3.8.4/lib/python3.8/cProfile.py", line 100, in runctx
    exec(cmd, globals, locals)
  File "<string>", line 2, in <module>
  File "main.py", line 26, in main
    agent.learn(observations, actions, rewards, dones)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/agent.py", line 20, in learn
    self.learner.learn(self.values, state_after, action, reward, done)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/learner.py", line 32, in DoubleQlearn
    value_next = torch.gather(vals_target_next, 2, torch.argmax(vals_next, 2).unsqueeze(2))
IndexError: Dimension out of range (expected to be in range of [-2, 1], but got 2)

------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-2>
Subject: Job 9334306: <test_run_2_0> in cluster <dcc> Exited

Job <test_run_2_0> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Sat Feb 27 13:16:48 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sat Feb 27 13:16:48 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Feb 27 13:16:48 2021
Terminated at Sat Feb 27 13:17:16 2021
Results reported at Sat Feb 27 13:17:16 2021

Your job looked like:

------------------------------------------------------------
# LSBATCH: User input
#!/bin/sh
#BSUB -q hpc
#BSUB -q gpuv100
#BSUB -gpu "num=1:mode=exclusive_process"
#BSUB -n 1
#BSUB -R "rusage[mem=60G]"
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

    CPU time :                                   5.62 sec.
    Max Memory :                                 639 MB
    Average Memory :                             639.00 MB
    Total Requested Memory :                     61440.00 MB
    Delta Memory :                               60801.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                7
    Run time :                                   82 sec.
    Turnaround time :                            28 sec.

The output (if any) is above this job summary.

