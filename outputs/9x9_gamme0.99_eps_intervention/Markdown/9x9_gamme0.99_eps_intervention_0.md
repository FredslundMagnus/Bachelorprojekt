
# Parameters

    Name :                      9x9_gamme0.99_eps_intervention-0
    Main :                      teleport
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.epsilonGreedy
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              True
    Layer putter :              True
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
    Gamma :                     0.99
    Update :                    10000
    Reset chance :              0.005
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      24911944576 function calls (24767662897 primitive calls) in 35699.63 seconds

##    Ordered by: cumulative time
   List reduced from 442 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35719.338 35719.338 {built-in method builtins.exec}
                      1    1.295    1.295 35719.338 35719.338 <string>:1(<module>)
                      1  142.757  142.757 35718.043 35718.043 main.py:10(teleport)
                5153790   20.493    0.000 12158.729    0.002 agent.py:26(learn)
                5153790  334.326    0.000 10218.990    0.002 learner.py:42(Qlearn)
                2576895   10.704    0.000 8588.334    0.003 game.py:21(step)
                2576895   14.783    0.000 8026.823    0.003 layers.py:212(step)
                2576895  108.886    0.000 7262.455    0.003 agent.py:50(_learn)
        162316812/18036144  683.591    0.000 5497.971    0.000 module.py:866(_call_impl)
                2576895  202.900    0.000 5146.510    0.002 layers.py:17(step)
               12882354   36.628    0.000 5109.407    0.000 network.py:24(forward)
                2576895 3143.891    0.001 5103.687    0.002 replaybuffer.py:27(teleporter_save_data)
               12882354  163.304    0.000 4982.019    0.000 container.py:117(forward)
              257689500  245.570    0.000 4920.811    0.000 layer.py:66(move)
                2576895   94.997    0.000 4865.599    0.002 agent.py:101(_learn)
                2576895 2457.041    0.001 4074.669    0.002 agent.py:77(interveen)
                5153790   44.161    0.000 3921.532    0.001 optimizer.py:84(wrapper)
                5153790   24.039    0.000 3724.424    0.001 grad_mode.py:24(decorate_context)
                5153790  152.006    0.000 3645.408    0.001 adam.py:55(step)
                5153790  772.477    0.000 3321.649    0.001 _functional.py:53(adam)
                5151669  146.146    0.000 3308.398    0.001 agent.py:45(__call__)
              257689500  601.840    0.000 2865.070    0.000 layers.py:229(check)
                2576896  246.784    0.000 2843.997    0.001 layers.py:192(update)
                5153790   23.093    0.000 2635.077    0.001 tensor.py:195(backward)
                5153790   20.745    0.000 2611.367    0.001 __init__.py:68(backward)
                5153790 2486.298    0.000 2486.298    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2576895 1242.521    0.000 2219.054    0.001 replaybuffer.py:23(sample_data)
               25764708   60.542    0.000 1866.056    0.000 conv.py:398(forward)
               25764708   37.232    0.000 1779.482    0.000 conv.py:390(_conv_forward)
               25764708 1742.250    0.000 1742.250    0.000 {built-in method conv2d}
                2576895  965.649    0.000 1655.473    0.001 agent.py:59(modify)
              175951645 1646.010    0.000 1646.010    0.000 {built-in method clone}
              257689500  337.548    0.000 1595.975    0.000 layers.py:223(isFree)
               33493272   71.701    0.000 1387.133    0.000 linear.py:93(forward)
               33493272   28.886    0.000 1282.903    0.000 functional.py:1737(linear)
             1356330165 1060.796    0.000 1258.427    0.000 layer.py:63(isFree)
               33493272 1247.924    0.000 1247.924    0.000 {built-in method torch._C._nn.linear}
                2576895   40.557    0.000 1066.088    0.000 agent.py:96(__call__)
                7728564   45.666    0.000 1032.622    0.000 agent.py:54(modify_board)
              257689500  612.763    0.000  983.254    0.000 layers.py:124(check)
               20615168  356.087    0.000  963.989    0.000 layer.py:90(update)
               20613039  943.443    0.000  943.443    0.000 {built-in method cat}
                1292517   14.303    0.000  874.808    0.001 layers.py:233(restart)
               11990416  831.057    0.000  831.057    0.000 {built-in method tensor}
                2576895   48.202    0.000  786.505    0.000 replaybuffer.py:19(stacker)
               46375626   41.380    0.000  748.255    0.000 activation.py:713(forward)
                1292517    3.105    0.000  742.181    0.001 levels.py:8(__init__)
                1292517   11.497    0.000  739.077    0.001 level.py:8(__init__)
               46375626   38.715    0.000  706.875    0.000 functional.py:1364(leaky_relu)
                1763342  111.566    0.000  706.525    0.000 levels.py:11(generate)
              257689600   70.894    0.000  687.781    0.000 {built-in method builtins.all}
                7728564  684.480    0.000  684.480    0.000 {built-in method torch._C._nn.one_hot}
               46375626  660.670    0.000  660.670    0.000 {built-in method torch._C._nn.leaky_relu}
              780714963  190.691    0.000  646.243    0.000 layers.py:197(<genexpr>)
               92768220  637.462    0.000  637.462    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                5153790    5.774    0.000  632.656    0.000 game.py:17(board)
             2190998320  412.477    0.000  579.957    0.000 enum.py:646(__hash__)
               92768220  570.041    0.000  570.041    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                5153790  101.431    0.000  569.946    0.000 optimizer.py:189(zero_grad)
              257689500  310.921    0.000  476.115    0.000 layers.py:95(check)
              621793471  469.204    0.000  469.204    0.000 layer.py:85(elements)
              257689600  289.611    0.000  431.501    0.000 layers.py:65(isDone)
                2576895  228.872    0.000  390.574    0.000 collector.py:37(collect)
               46384110  383.933    0.000  383.933    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              257689500  255.623    0.000  368.963    0.000 layers.py:50(check)
              183680209  367.865    0.000  367.865    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
             3934161782  352.441    0.000  352.441    0.000 layer.py:59(positions)
              257689500  233.193    0.000  351.504    0.000 layers.py:77(check)
               46384110  340.147    0.000  340.147    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                7728564   29.191    0.000  331.369    0.000 exploration.py:47(epsilonGreedy)
               46384110  304.870    0.000  304.870    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               46384110  301.796    0.000  301.796    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              324688824  207.515    0.000  264.118    0.000 tensor.py:906(grad)
                1763342  126.407    0.000  238.444    0.000 levels.py:76(RFS)
                5153790    7.654    0.000  231.750    0.000 loss.py:527(forward)
               46384110  225.374    0.000  225.374    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                5153790   22.148    0.000  224.095    0.000 functional.py:2898(mse_loss)
                7396096   86.565    0.000  221.589    0.000 random.py:315(sample)
              290821022  126.275    0.000  170.454    0.000 layer.py:76(add)
               15461370  170.051    0.000  170.051    0.000 {built-in method sum}
                3877551   23.562    0.000  168.831    0.000 level.py:41(notUsed)
             2191017223  167.484    0.000  167.484    0.000 {built-in method builtins.hash}
              215993514  112.075    0.000  162.011    0.000 layer.py:72(remove)
                5153790  138.771    0.000  138.771    0.000 {built-in method torch._C._nn.mse_loss}
        771275633/771275631   94.604    0.000  130.169    0.000 {built-in method builtins.len}
                5154562  129.608    0.000  129.608    0.000 {built-in method max}
             1196894355  126.128    0.000  126.128    0.000 layer.py:125(isBlocking)
               25764708   18.127    0.000  122.303    0.000 flatten.py:39(forward)
                7730685   11.941    0.000  120.854    0.000 tensor.py:525(__rsub__)
              129149756  117.620    0.000  117.620    0.000 level.py:32(inverse)
               10340136   16.630    0.000  114.640    0.000 layer.py:40(restart)
              171147688   75.289    0.000  110.183    0.000 random.py:250(_randbelow_with_getrandbits)
                6054980  108.020    0.000  108.020    0.000 {built-in method argmax}
                7730685  107.197    0.000  107.197    0.000 {built-in method rsub}
                1673584   45.219    0.000  105.742    0.000 {method 'choice' of 'numpy.random.mtrand.RandomState' objects}
               25764708  104.177    0.000  104.177    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                5153790   22.000    0.000   99.673    0.000 __init__.py:28(_make_grads)
                5153790   97.063    0.000   97.063    0.000 {built-in method gather}
              164893707   95.916    0.000   95.916    0.000 {built-in method torch._C._get_tracing_state}
               10307580   20.939    0.000   94.452    0.000 profiler.py:615(__enter__)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9395481: <9x9_gamme0.99_eps_intervention_0> in cluster <dcc> Done

Job <9x9_gamme0.99_eps_intervention_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Tue Mar  9 01:14:58 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Tue Mar  9 01:15:29 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Mar  9 01:15:29 2021
Terminated at Tue Mar  9 11:11:22 2021
Results reported at Tue Mar  9 11:11:22 2021

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

Successfully completed.

Resource usage summary:

    CPU time :                                   35625.29 sec.
    Max Memory :                                 5938 MB
    Average Memory :                             4187.12 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2254.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35743 sec.
    Turnaround time :                            35784 sec.

The output (if any) is above this job summary.

