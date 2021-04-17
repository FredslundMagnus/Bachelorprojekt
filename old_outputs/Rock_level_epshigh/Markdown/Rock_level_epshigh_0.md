
# Parameters

    Name :                      Rock_level_epshigh-0
    Main :                      teleport
    Level :                     Levels.Rocks
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Network1 :                  Networks.Teleporter
    Network2 :                  Networks.Mini
    Learner1 :                  Learners.Qlearn
    Learner2 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Exploration2 :              Explorations.epsilonGreedy
    Layer blocks :              True
    Layer goal :                True
    Layer gold :                False
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            True
    Layer diamond2 :            True
    Layer diamond3 :            True
    Layer diamond4 :            True
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.2
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      35880001942 function calls (35758776843 primitive calls) in 42916.56 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42916.563 42916.563 {built-in method builtins.exec}
                      1    0.973    0.973 42916.563 42916.563 <string>:1(<module>)
                      1  156.443  156.443 42915.590 42915.590 main.py:13(teleport)
                2164769   13.664    0.000 17535.374    0.008 game.py:27(step)
                2164769   16.663    0.000 16946.178    0.008 layers.py:373(step)
                2164769  224.457    0.000 11246.355    0.005 layers.py:18(step)
                4329538   26.901    0.000 11135.487    0.003 agent.py:26(learn)
              216476900  540.522    0.000 11001.460    0.000 layer.py:74(move)
                4329538  307.441    0.000 9287.782    0.002 learner.py:42(Qlearn)
              216476900  721.573    0.000 7907.119    0.000 layers.py:390(check)
                2164769   93.869    0.000 6555.212    0.003 agent.py:50(_learn)
                2164770  273.802    0.000 5657.836    0.003 layers.py:344(update)
        136377223/15153135  636.862    0.000 4953.783    0.000 module.py:866(_call_impl)
                2164769 2808.214    0.001 4675.139    0.002 replaybuffer.py:27(teleporter_save_data)
               10823597   36.602    0.000 4553.294    0.000 network.py:24(forward)
                2164769   80.228    0.000 4542.518    0.002 agent.py:101(_learn)
               10823597  150.285    0.000 4433.090    0.000 container.py:117(forward)
              216476900 3756.115    0.000 4347.027    0.000 layers.py:76(check)
                2164769 1997.779    0.001 3471.062    0.002 agent.py:77(interveen)
                4329538   54.013    0.000 3421.317    0.001 optimizer.py:84(wrapper)
                4329538   26.459    0.000 3211.013    0.001 grad_mode.py:24(decorate_context)
                4329538  150.203    0.000 3124.518    0.001 adam.py:55(step)
                4329290  144.988    0.000 3096.296    0.001 agent.py:45(__call__)
                4329538  651.579    0.000 2817.738    0.001 _functional.py:53(adam)
                2164769 1803.145    0.001 2606.688    0.001 replaybuffer.py:23(sample_data)
                4329538   23.877    0.000 2520.201    0.001 tensor.py:195(backward)
                4329538   24.660    0.000 2495.698    0.001 __init__.py:68(backward)
               19482930 1656.895    0.000 2485.731    0.000 layer.py:119(update)
                4329538 2366.414    0.001 2366.414    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              216476900  382.770    0.000 2267.693    0.000 layers.py:384(isFree)
                6848058   74.763    0.000 2152.380    0.000 layers.py:394(restart)
             1795978462 1647.711    0.000 1884.922    0.000 layer.py:71(isFree)
                2164769 1020.707    0.000 1706.815    0.001 agent.py:59(modify)
               21647194   55.280    0.000 1698.759    0.000 conv.py:398(forward)
               21647194   39.557    0.000 1617.186    0.000 conv.py:390(_conv_forward)
               21647194 1577.629    0.000 1577.629    0.000 {built-in method conv2d}
              170508124 1540.355    0.000 1540.355    0.000 {built-in method clone}
                6848058   33.969    0.000 1337.206    0.000 level.py:8(__init__)
               28141253   64.752    0.000 1218.229    0.000 linear.py:93(forward)
                6848058  195.384    0.000 1188.130    0.000 levels.py:95(generate)
               28141253   25.970    0.000 1118.764    0.000 functional.py:1737(linear)
               28141253 1086.949    0.000 1086.949    0.000 {built-in method torch._C._nn.linear}
                6494059   52.497    0.000  966.474    0.000 agent.py:54(modify_board)
                2164769   43.677    0.000  962.094    0.000 agent.py:96(__call__)
             3705486057  660.832    0.000  940.642    0.000 enum.py:646(__hash__)
                9164729  826.293    0.000  826.293    0.000 {built-in method tensor}
               19482673  762.202    0.000  762.202    0.000 {built-in method cat}
               61632522   99.544    0.000  719.828    0.000 layer.py:48(restart)
                4329538    7.566    0.000  684.118    0.000 game.py:23(board)
               13696116   96.299    0.000  661.732    0.000 level.py:41(notUsed)
              216476900  460.087    0.000  658.562    0.000 layers.py:63(check)
              216477000   66.718    0.000  646.248    0.000 {built-in method builtins.all}
                6494059  633.796    0.000  633.796    0.000 {built-in method torch._C._nn.one_hot}
               38964850   38.895    0.000  633.080    0.000 activation.py:713(forward)
                2164769   45.834    0.000  617.497    0.000 replaybuffer.py:19(stacker)
              216476900  390.027    0.000  614.730    0.000 layers.py:216(check)
             1855561542  606.349    0.000  606.349    0.000 layer.py:114(elements)
              683495933  171.349    0.000  605.773    0.000 layers.py:350(<genexpr>)
              216476900  371.539    0.000  594.856    0.000 layers.py:230(check)
               38964850   35.179    0.000  594.185    0.000 functional.py:1364(leaky_relu)
              216476900  369.621    0.000  594.113    0.000 layers.py:244(check)
               38964850  552.173    0.000  552.173    0.000 {built-in method torch._C._nn.leaky_relu}
               77931684  539.772    0.000  539.772    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
             5068710060  501.671    0.000  501.671    0.000 layer.py:67(positions)
              912416293  368.485    0.000  498.798    0.000 layer.py:98(add)
                4329538   91.552    0.000  491.378    0.000 optimizer.py:189(zero_grad)
               77931684  478.220    0.000  478.220    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              431929540  230.653    0.000  453.720    0.000 layer.py:94(remove)
              216477000  289.039    0.000  409.581    0.000 layers.py:110(isDone)
                9012827  146.250    0.000  401.639    0.000 random.py:315(sample)
                6848158  182.065    0.000  373.105    0.000 layers.py:33(reset)
              177002183  372.179    0.000  372.179    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                2164769  200.324    0.000  342.382    0.000 collector.py:54(collect)
              376643190  342.212    0.000  342.212    0.000 level.py:32(inverse)
                4329290  115.825    0.000  332.649    0.000 exploration.py:53(softmaxer)
               38965842  323.305    0.000  323.305    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              216476900  215.026    0.000  318.656    0.000 layers.py:203(check)
               38965842  287.544    0.000  287.544    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             3705502008  279.813    0.000  279.813    0.000 {built-in method builtins.hash}
               38965842  264.105    0.000  264.105    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
               38965842  261.371    0.000  261.371    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                4329538   11.046    0.000  240.558    0.000 loss.py:527(forward)
              272760948  192.013    0.000  236.011    0.000 tensor.py:906(grad)
                4329538   28.390    0.000  229.512    0.000 functional.py:2898(mse_loss)
              216476900   91.330    0.000  216.450    0.000 layers.py:99(<listcomp>)
             2791521140  215.956    0.000  215.956    0.000 {method 'append' of 'list' objects}
        2220433007/2220433005  161.727    0.000  196.115    0.000 {built-in method builtins.len}
               38965842  188.000    0.000  188.000    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1795978462  182.328    0.000  182.328    0.000 layer.py:175(isBlocking)
              431929540  181.636    0.000  181.636    0.000 {method 'remove' of 'list' objects}
              279494104  122.847    0.000  181.043    0.000 random.py:250(_randbelow_with_getrandbits)
               13696116   13.436    0.000  171.793    0.000 level.py:38(elementsIn)
               12988614  153.334    0.000  153.334    0.000 {built-in method sum}
                4329538  131.976    0.000  131.976    0.000 {built-in method torch._C._nn.mse_loss}
                2164769   12.576    0.000  123.660    0.000 exploration.py:47(epsilonGreedy)
                6494307   14.811    0.000  120.869    0.000 tensor.py:525(__rsub__)
                4330186  116.562    0.000  116.562    0.000 {built-in method max}
                4329290  109.182    0.000  109.182    0.000 {built-in method multinomial}
               21647194   17.743    0.000  108.415    0.000 flatten.py:39(forward)
                6494307  104.336    0.000  104.336    0.000 {built-in method rsub}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-11>
Subject: Job 9441983: <Rock_level_epshigh_0> in cluster <dcc> Done

Job <Rock_level_epshigh_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:11 2021
Job was executed on host(s) <n-62-20-11>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 01:13:13 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 01:13:13 2021
Terminated at Sat Mar 20 13:08:40 2021
Results reported at Sat Mar 20 13:08:40 2021

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

    CPU time :                                   42801.30 sec.
    Max Memory :                                 5368 MB
    Average Memory :                             3983.16 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2824.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42965 sec.
    Turnaround time :                            42929 sec.

The output (if any) is above this job summary.

