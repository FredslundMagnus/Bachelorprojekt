Traceback (most recent call last):
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 71, in __init__
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
  File "main.py", line 60, in teleport
    collector.collect([rewards, modified_rewards, teleport_rewards], [dones, modified_dones])
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/save.py", line 16, in __exit__
    self.save()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/save.py", line 21, in save
    self.saveObject(element, start, element.__class__.__name__)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/save.py", line 26, in saveObject
    pickle.dump(element, open(Save.path(start, _class) + name, "wb"))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/save.py", line 34, in path
    os.mkdir("/".join(path))
FileExistsError: [Errno 17] File exists: 'outputs/causal5_good/Teleporter'


# Parameters

    Name :                      causal5_good-1
    Main :                      teleport
    Level :                     Levels.Causal5
    Hours :                     20.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
    Learner2 :                  Learners.Qlearn
    Exploration2 :              Explorations.epsilonGreedy
    Gamma2 :                    0.95
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    Layer reddoors :            True
    Layer redkeys :             True
    Layer bluedoors :           True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              1197 minutes.
    Hours used :                19 hours.

# Profiling


      50341217062 function calls (50158500847 primitive calls) in 71875.05 seconds

##    Ordered by: cumulative time
   List reduced from 460 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 71875.054 71875.054 {built-in method builtins.exec}
                      1    0.000    0.000 71875.054 71875.054 <string>:1(<module>)
                      1  160.733  160.733 71875.054 71875.054 main.py:42(teleport)
                6526064   23.948    0.000 24246.924    0.004 agent.py:27(learn)
                6526064  571.335    0.000 20800.350    0.003 learner.py:42(Qlearn)
                3263032   16.603    0.000 14969.101    0.005 game.py:36(step)
                3263032  114.137    0.000 14573.547    0.004 agent.py:52(_learn)
                3263032   19.968    0.000 14130.243    0.004 layers.py:594(step)
                3263032 6777.918    0.002 12986.749    0.004 replaybuffer.py:28(teleporter_save_data)
                3263032   94.369    0.000 9636.021    0.003 agent.py:113(_learn)
        205555871/22840059  863.064    0.000 9356.597    0.000 module.py:715(_call_impl)
                3263032  265.745    0.000 8978.500    0.003 layers.py:18(step)
                6526064   40.725    0.000 8918.886    0.001 grad_mode.py:23(decorate_context)
                6526064  227.312    0.000 8798.048    0.001 adam.py:55(step)
               16313995   42.617    0.000 8767.278    0.001 network.py:24(forward)
              326303200  433.455    0.000 8681.363    0.000 layer.py:82(move)
               16313995  221.580    0.000 8623.347    0.001 container.py:115(forward)
                3263032 5539.347    0.002 8398.384    0.003 agent.py:84(interveen)
                6526064 1628.522    0.000 7585.295    0.001 functional.py:53(adam)
                6524899  157.780    0.000 5749.014    0.001 agent.py:47(__call__)
              326303200  888.160    0.000 5542.183    0.000 layers.py:611(check)
                3263033  359.842    0.000 5108.052    0.002 layers.py:565(update)
              323737166 4853.821    0.000 4853.821    0.000 {built-in method clone}
                6526064   42.061    0.000 4780.680    0.001 tensor.py:181(backward)
                6526064   24.399    0.000 4738.619    0.001 __init__.py:68(backward)
                3263032 2781.291    0.001 4568.051    0.001 replaybuffer.py:22(sample_data)
                6526064 4531.348    0.001 4531.348    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                3263032 1612.006    0.000 3290.384    0.001 agent.py:65(modify)
               32627990   58.493    0.000 3114.168    0.000 conv.py:422(forward)
               32627990   62.493    0.000 3032.881    0.000 conv.py:414(_conv_forward)
               32627990 2958.553    0.000 2958.553    0.000 {built-in method conv2d}
               42415921   98.917    0.000 2786.549    0.000 linear.py:92(forward)
               42415921  172.595    0.000 2642.125    0.000 functional.py:1669(linear)
              326303200  623.511    0.000 2259.855    0.000 layers.py:605(isFree)
               29367297 1106.056    0.000 1942.977    0.000 layer.py:143(NoRock_update)
               42415921 1886.958    0.000 1886.958    0.000 {built-in method addmm}
              411142086 1188.973    0.000 1858.641    0.000 tensor.py:933(grad)
               29366123 1847.977    0.000 1847.977    0.000 {built-in method cat}
                3263032   45.921    0.000 1813.195    0.001 agent.py:108(__call__)
                6526064  167.177    0.000 1793.536    0.000 optimizer.py:167(zero_grad)
                3915433   43.238    0.000 1762.439    0.000 layers.py:615(restart)
                9787931   72.996    0.000 1707.604    0.000 agent.py:57(modify_board)
             2839486544 1301.058    0.000 1636.343    0.000 layer.py:79(isFree)
              117469152 1587.152    0.000 1587.152    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3263032   65.686    0.000 1534.428    0.000 replaybuffer.py:18(stacker)
             5730498516 1026.880    0.000 1465.785    0.000 enum.py:646(__hash__)
              333525097 1457.000    0.000 1457.000    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                3915433   22.730    0.000 1411.623    0.000 level.py:8(__init__)
              117469152 1341.658    0.000 1341.658    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               58729916   55.282    0.000 1306.989    0.000 activation.py:713(forward)
               58729916   86.827    0.000 1251.707    0.000 functional.py:1292(leaky_relu)
                3915433   62.758    0.000 1243.376    0.000 levels.py:247(generate)
               14035546 1171.400    0.000 1171.400    0.000 {built-in method tensor}
               58729916 1156.908    0.000 1156.908    0.000 {built-in method torch._C._nn.leaky_relu}
               25450529  220.056    0.000 1115.685    0.000 level.py:41(notUsed)
                9787931 1067.781    0.000 1067.781    0.000 {built-in method torch._C._nn.one_hot}
              326303200  570.019    0.000  929.576    0.000 layers.py:415(check)
              342620360  111.846    0.000  928.008    0.000 {built-in method builtins.all}
              326303200  569.578    0.000  920.867    0.000 layers.py:371(check)
              326303200  566.386    0.000  913.681    0.000 layers.py:357(check)
              326303200  570.470    0.000  911.166    0.000 layers.py:401(check)
              528609081  305.306    0.000  895.825    0.000 overrides.py:1070(has_torch_function)
                6526064    8.696    0.000  892.538    0.000 game.py:32(board)
               58734576  859.946    0.000  859.946    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1014484129  253.951    0.000  844.754    0.000 layers.py:571(<genexpr>)
                3263032  500.142    0.000  840.175    0.000 collector.py:54(collect)
               58734576  785.925    0.000  785.925    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               58734576  715.217    0.000  715.217    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               16317060   94.659    0.000  713.980    0.000 tensor.py:21(wrapped)
             7174917850  701.099    0.000  701.099    0.000 layer.py:75(positions)
               58734576  645.548    0.000  645.548    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                6524899  222.925    0.000  621.154    0.000 exploration.py:53(softmaxer)
              584077131  228.961    0.000  561.754    0.000 {built-in method builtins.any}
              326303300  370.851    0.000  555.150    0.000 layers.py:111(isDone)
               58734576  497.652    0.000  497.652    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              984655382  491.608    0.000  491.608    0.000 layer.py:122(elements)
              326303200  311.923    0.000  471.904    0.000 layers.py:344(check)
               25450529   19.213    0.000  455.169    0.000 level.py:38(elementsIn)
             5730522083  438.910    0.000  438.910    0.000 {built-in method builtins.hash}
              326303200  275.384    0.000  419.078    0.000 layers.py:388(check)
                6526064    9.294    0.000  394.679    0.000 loss.py:445(forward)
                6526064   37.219    0.000  385.384    0.000 functional.py:2637(mse_loss)
               42415921  378.930    0.000  378.930    0.000 {method 't' of 'torch._C._TensorBase' objects}
        3446413173/3446413171  250.579    0.000  355.226    0.000 {built-in method builtins.len}
               19578192  335.971    0.000  335.971    0.000 {built-in method sum}
             1115950491  258.152    0.000  328.119    0.000 overrides.py:1083(<genexpr>)
             1200333250  299.516    0.000  299.516    0.000 level.py:32(inverse)
               35238897   31.516    0.000  295.628    0.000 layer.py:56(restart)
               25450529  141.499    0.000  283.260    0.000 level.py:39(<listcomp>)
              464895503  203.385    0.000  282.513    0.000 layer.py:106(add)
             2839486544  276.752    0.000  276.752    0.000 layer.py:183(isBlocking)
                9789096   49.540    0.000  258.149    0.000 tensor.py:506(__rsub__)
              329970434  173.092    0.000  256.884    0.000 layer.py:102(remove)
                3263032   89.631    0.000  246.288    0.000 random.py:315(sample)
                6526064  244.398    0.000  244.398    0.000 {built-in method torch._C._nn.mse_loss}
                3263086  243.732    0.000  243.733    0.000 {method 'to' of 'torch._C._TensorBase' objects}
               32627990   25.007    0.000  242.717    0.000 flatten.py:39(forward)
                9789096  230.761    0.000  230.761    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                3264336  223.078    0.000  223.078    0.000 {method 'ne' of 'torch._C._TensorBase' objects}
                6527042  219.321    0.000  219.321    0.000 {built-in method max}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 9492738: <causal5_good_1> in cluster <dcc> Done

Job <causal5_good_1> was submitted from host <n-62-27-19> by user <s183905> in cluster <dcc> at Fri Apr  2 14:23:06 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Fri Apr  2 14:23:08 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Fri Apr  2 14:23:08 2021
Terminated at Sat Apr  3 10:23:36 2021
Results reported at Sat Apr  3 10:23:36 2021

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

Successfully completed.

Resource usage summary:

    CPU time :                                   71526.04 sec.
    Max Memory :                                 2811 MB
    Average Memory :                             2794.43 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13573.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   72135 sec.
    Turnaround time :                            72030 sec.

The output (if any) is above this job summary.

