
# Parameters

    Name :                      causal6_online_var_0.5_full_UCB1-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
    Failed actions chance :     0.5
    Hours :                     12.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        200000.0
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        100000.0
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
    Layer reddoor :             True
    Layer redkeys :             True
    Layer bluedoor :            True
    Layer bluekeys :            True
    Layer pink1 :               True
    Layer pink2 :               True
    Layer pink3 :               True
    Layer brown1 :              True
    Layer brown2 :              True
    Layer brown3 :              True
    Layer greendown :           True
    Layer greenup :             True
    Layer greenstar :           True
    Layer yellowstar :          True
    Layer bluestar :            True
    Layer coconut :             True
    Layer monster :             True
    Layer greencross :          True
    Layer bluecross :           True
    Layer redcross :            True
    Layer purplecross :         True
    Epsilon cap :               0.2
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.001
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      35016903975 function calls (31716449198 primitive calls) in 42906.75 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42906.755 42906.755 {built-in method builtins.exec}
                      1    0.001    0.001 42906.755 42906.755 <string>:1(<module>)
                      1  130.524  130.524 42906.754 42906.754 allGraphsTrain.py:10(graphTrain)
                 486568 6813.136    0.014 15221.370    0.031 allGraphs.py:146(transformNot)
                 486568   15.189    0.000 9556.126    0.020 allGraphsTrain.py:29(<listcomp>)
               49143469 2481.527    0.000 9540.987    0.000 allGraphs.py:110(states)
                 486568  624.231    0.001 9273.384    0.019 allGraphsTrain.py:35(<listcomp>)
               10432586   17.363    0.000 8649.153    0.001 allGraphs.py:158(getInterventions)
              583885988 8529.098    0.000 8529.098    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              535225300 7522.804    0.000 7522.804    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
               10432586   10.261    0.000 7448.956    0.001 allGraphs.py:133(UCB1)
        591234539/10432586  365.304    0.000 7389.665    0.001 {built-in method builtins.min}
               40513797   20.698    0.000 7366.165    0.000 allGraphs.py:134(<lambda>)
        1172036492/40513797 1934.747    0.000 7345.468    0.000 allGraphs.py:68(expected_moves_UCB1)
        1712324648/133926262  575.783    0.000 7018.800    0.000 allGraphs.py:72(<genexpr>)
                 486568    1.865    0.000 2827.969    0.006 game.py:41(step)
                 486568    2.555    0.000 2710.679    0.006 layers.py:718(step)
             8212920863 1389.827    0.000 2023.530    0.000 enum.py:646(__hash__)
              591234539  349.678    0.000 1999.546    0.000 allGraphs.py:83(layers_not_in)
                 486568  144.966    0.000 1879.652    0.004 allGraphsTrain.py:37(<listcomp>)
             1172036492 1069.859    0.000 1738.366    0.000 allGraphs.py:60(UCB1)
                 486569   73.056    0.000 1687.299    0.003 layers.py:684(update)
              591234539  798.423    0.000 1649.868    0.000 allGraphs.py:84(<listcomp>)
               14941796 1468.302    0.000 1468.302    0.000 {built-in method tensor}
                 486568    1.830    0.000 1406.837    0.003 agent.py:29(learn)
                 486568   10.856    0.000 1403.953    0.003 agent.py:117(_learn)
                 486568   40.468    0.000 1393.097    0.003 learner.py:42(Qlearn)
               12865427    8.071    0.000 1387.973    0.000 game.py:37(board)
               10432586   56.905    0.000 1182.835    0.000 allGraphs.py:153(format)
               51576208  148.694    0.000 1169.415    0.000 tensor.py:21(wrapped)
                 486568   51.110    0.000 1123.903    0.002 allGraphsTrain.py:44(<listcomp>)
                 486568   38.519    0.000 1018.024    0.002 layers.py:17(step)
               48656800   84.192    0.000  974.642    0.000 layer.py:98(move)
                1804674   15.957    0.000  868.500    0.000 layers.py:740(restart)
               51089640  861.697    0.000  861.697    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               48656800  770.202    0.000  770.202    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1804674    7.278    0.000  709.386    0.000 level.py:8(__init__)
                1804674   25.232    0.000  634.669    0.000 levels.py:293(generate)
             8212922492  633.703    0.000  633.703    0.000 {built-in method builtins.hash}
                 486568  341.660    0.001  598.170    0.001 agent.py:67(modify)
                 486568    3.262    0.000  590.116    0.001 grad_mode.py:23(decorate_context)
               10829062  103.853    0.000  582.411    0.000 level.py:41(notUsed)
                 486568   15.400    0.000  581.323    0.001 adam.py:55(step)
               48656800  127.359    0.000  517.908    0.000 layers.py:735(check)
        11191064/1459704   48.660    0.000  506.499    0.000 module.py:715(_call_impl)
                 486568  106.046    0.000  499.126    0.001 functional.py:53(adam)
                 973136    2.636    0.000  464.380    0.000 network.py:24(forward)
                 973136   11.935    0.000  455.491    0.000 container.py:115(forward)
                 486568    2.973    0.000  315.621    0.001 tensor.py:181(backward)
                 486568    1.751    0.000  312.648    0.001 __init__.py:68(backward)
              100233108   48.599    0.000  302.242    0.000 {built-in method builtins.all}
              134434601   82.204    0.000  298.896    0.000 {built-in method builtins.any}
                 486568  297.686    0.001  297.686    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               48656800   81.467    0.000  295.742    0.000 layers.py:729(isFree)
               10829062    8.111    0.000  271.730    0.000 level.py:38(elementsIn)
                 486568    6.744    0.000  268.412    0.001 agent.py:112(__call__)
               50603072  263.833    0.000  263.833    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3892552  151.221    0.000  260.665    0.000 layer.py:167(NoRock_update)
             1171978167  251.264    0.000  251.264    0.000 {built-in method math.log}
              298292157   89.273    0.000  238.641    0.000 layers.py:690(<genexpr>)
             1173496196  235.387    0.000  235.387    0.000 {built-in method builtins.max}
              361764314  163.162    0.000  214.274    0.000 layer.py:95(isFree)
                1459704    6.489    0.000  180.790    0.000 tensor.py:576(__iter__)
                1946272    3.662    0.000  178.020    0.000 conv.py:422(forward)
               10829062   86.107    0.000  174.724    0.000 level.py:39(<listcomp>)
                1946272    3.985    0.000  172.993    0.000 conv.py:414(_conv_forward)
                1459704  170.071    0.000  170.071    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                1946272  168.274    0.000  168.274    0.000 {built-in method conv2d}
              421670034  130.000    0.000  156.972    0.000 layers.py:700(<genexpr>)
               84662966   46.506    0.000  150.906    0.000 overrides.py:1070(has_torch_function)
               14437392   11.643    0.000  138.103    0.000 layer.py:69(restart)
                1946272    4.996    0.000  135.855    0.000 linear.py:92(forward)
                1946272    8.709    0.000  128.554    0.000 functional.py:1669(linear)
             1175870846  127.847    0.000  127.847    0.000 {built-in method math.sqrt}
               27247862   79.890    0.000  125.769    0.000 tensor.py:933(grad)
              513656657  123.282    0.000  123.282    0.000 level.py:32(inverse)
                 486568   11.555    0.000  120.780    0.000 optimizer.py:167(zero_grad)
               24324048   67.736    0.000  112.596    0.000 layers.py:424(check)
                1804774   58.674    0.000  108.780    0.000 layers.py:36(reset)
                7785088  104.291    0.000  104.291    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 486568   61.033    0.000  102.322    0.000 collector.py:46(collect)
                1946272   91.760    0.000   91.760    0.000 {built-in method addmm}
                7785088   89.095    0.000   89.095    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10829062   55.001    0.000   88.895    0.000 {built-in method _functools.reduce}
              454816025   88.220    0.000   88.220    0.000 enum.py:352(<genexpr>)
                 486568    3.947    0.000   87.567    0.000 agent.py:59(modify_board)
               48656900   54.725    0.000   87.218    0.000 layers.py:442(isDone)
              742024933   76.840    0.000   76.840    0.000 layer.py:91(positions)
               24326448   44.900    0.000   72.676    0.000 layers.py:437(check)
               24324273   44.464    0.000   71.864    0.000 layers.py:452(check)
              231672060   64.992    0.000   64.992    0.000 layer.py:146(elements)
                2919408    2.761    0.000   64.623    0.000 activation.py:713(forward)
              112656949   46.553    0.000   63.407    0.000 layer.py:130(add)
                1804674   32.327    0.000   62.629    0.000 level.py:16(<dictcomp>)
                2919408    4.597    0.000   61.862    0.000 functional.py:1292(leaky_relu)
              222848412   50.049    0.000   59.374    0.000 overrides.py:1083(<genexpr>)
                2919408   56.829    0.000   56.829    0.000 {built-in method torch._C._nn.leaky_relu}
                3892544   56.429    0.000   56.429    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 486568   55.280    0.000   55.280    0.000 {built-in method torch._C._nn.one_hot}
                 486568   36.490    0.000   54.606    0.000 allGraphsTrain.py:43(<listcomp>)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-16>
Subject: Job 9512223: <causal6_online_var_0.5_full_UCB1_0> in cluster <dcc> Done

Job <causal6_online_var_0.5_full_UCB1_0> was submitted from host <n-62-30-2> by user <s183905> in cluster <dcc> at Tue Apr 13 11:09:10 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 13 22:32:22 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 13 22:32:22 2021
Terminated at Wed Apr 14 10:27:32 2021
Results reported at Wed Apr 14 10:27:32 2021

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

    CPU time :                                   42800.47 sec.
    Max Memory :                                 2082 MB
    Average Memory :                             2081.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14302.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42910 sec.
    Turnaround time :                            83902 sec.

The output (if any) is above this job summary.

