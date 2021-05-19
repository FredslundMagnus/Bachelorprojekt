
# Parameters

    Name :                      Diamonds2_0.0_NN-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
    Failed actions chance :     0.0
    Use model :                 True
    Depth :                     3
    Model explore :             100000
    Samples :                   5
    Hours :                     10.0
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
    Layer super1 :              True
    Layer super2 :              True
    Layer super3 :              True
    Layer super4 :              True
    Layer super5 :              True
    Layer super6 :              True
    Layer super7 :              True
    Epsilon cap :               0.2
    Softmax cap :               0.0
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Cf convert :                3
    Counterfacts :              1
    Topn :                      6
    Random counterfacts :       False
    Num :                       0
    Load name :                 Causal4_Conver4_3counterfacts
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      14150870121 function calls (13529794099 primitive calls) in 35710.24 seconds

##    Ordered by: cumulative time
   List reduced from 476 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.236 35710.236 {built-in method builtins.exec}
                      1    0.001    0.001 35710.236 35710.236 <string>:1(<module>)
                      1   26.086   26.086 35710.236 35710.236 allGraphsTrain.py:13(graphTrain)
                 105074  109.841    0.001 27252.390    0.259 allGraphsTrain.py:40(<listcomp>)
                 613310    3.044    0.000 27137.690    0.044 allGraphs.py:179(getInterventionsmodel)
        52618182/445966 3660.562    0.000 25230.986    0.057 allGraphs.py:186(recursiveBEST)
               50415250 2112.012    0.000 18586.664    0.000 BayesianNN.py:65(predict_no_convert)
               56616224  121.782    0.000 18395.237    0.000 BayesianNN.py:18(forward)
        626440819/58177099 2028.204    0.000 18353.598    0.000 module.py:715(_call_impl)
               56826372  652.098    0.000 17958.043    0.000 container.py:115(forward)
              170268968  310.449    0.000 8065.471    0.000 linear.py:92(forward)
              170268968  581.416    0.000 7618.289    0.000 functional.py:1669(linear)
              170268968 5157.360    0.000 5157.360    0.000 {built-in method addmm}
                 105074 1159.563    0.011 4283.574    0.041 allGraphs.py:156(transformNot)
              169848672  134.846    0.000 4132.499    0.000 dropout.py:57(forward)
              169848672  536.198    0.000 3997.652    0.000 functional.py:960(dropout)
              169848672 3333.168    0.000 3333.168    0.000 {built-in method dropout}
                4955321   64.525    0.000 2566.074    0.001 BayesianNN.py:61(predict)
              170479116  104.303    0.000 2437.966    0.000 activation.py:713(forward)
              170479116  176.689    0.000 2333.663    0.000 functional.py:1292(leaky_relu)
                1245653   14.054    0.000 2260.925    0.002 BayesianNN.py:57(learn)
              170479116 2137.679    0.000 2137.679    0.000 {built-in method torch._C._nn.leaky_relu}
                1245653   13.165    0.000 2030.017    0.002 BayesianNN.py:21(learn)
                 105074    2.538    0.000 1849.358    0.018 allGraphsTrain.py:33(<listcomp>)
               10612575  428.060    0.000 1846.846    0.000 allGraphs.py:114(states)
          807015/167344   69.535    0.000 1826.112    0.011 allGraphs.py:202(recursiveExplore)
              148350693 1819.416    0.000 1819.416    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              136596800 1339.851    0.000 1339.851    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
              170268968 1198.147    0.000 1198.147    0.000 {method 't' of 'torch._C._TensorBase' objects}
               63949731  211.987    0.000 1190.049    0.000 tensor.py:21(wrapped)
               52916961  159.800    0.000 1076.026    0.000 tensor.py:506(__rsub__)
                6200974  876.714    0.000 1060.043    0.000 BayesianNN.py:43(convert_data)
                1350727    7.219    0.000  925.240    0.001 grad_mode.py:23(decorate_context)
               52916961  916.225    0.000  916.225    0.000 {built-in method rsub}
                1350727   32.484    0.000  904.088    0.001 adam.py:55(step)
                 105074    4.069    0.000  762.115    0.007 allGraphs.py:141(transform)
                1350727  165.334    0.000  740.010    0.001 functional.py:53(adam)
               52811887  702.484    0.000  702.484    0.000 {method 'gt' of 'torch._C._TensorBase' objects}
              258488564  185.300    0.000  602.371    0.000 overrides.py:1070(has_torch_function)
                 105074    0.372    0.000  534.536    0.005 game.py:42(step)
                 105074    0.551    0.000  511.350    0.005 layers.py:827(step)
                1350727    7.569    0.000  506.073    0.000 tensor.py:181(backward)
                1350727    4.245    0.000  498.504    0.000 __init__.py:68(backward)
              441860804  200.789    0.000  471.713    0.000 {built-in method builtins.any}
                1350727  463.911    0.000  463.911    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              626756041  370.416    0.000  370.416    0.000 {built-in method torch._C._get_tracing_state}
                 105074    7.865    0.000  316.777    0.003 layers.py:17(step)
                 105074   21.154    0.000  310.931    0.003 allGraphsTrain.py:44(<listcomp>)
               10507400   17.714    0.000  307.986    0.000 layer.py:106(move)
              708949442  197.070    0.000  236.648    0.000 overrides.py:1083(<genexpr>)
               58201630  140.593    0.000  234.655    0.000 tensor.py:933(grad)
                 105074    0.371    0.000  234.086    0.002 agent.py:29(learn)
                 105074    2.206    0.000  233.470    0.002 agent.py:117(_learn)
                 105074    6.831    0.000  231.263    0.002 learner.py:42(Qlearn)
             2562589648  217.868    0.000  217.868    0.000 {method 'values' of 'collections.OrderedDict' objects}
              399451058  215.130    0.000  215.131    0.000 module.py:765(__getattr__)
               10507400   42.332    0.000  206.499    0.000 layers.py:844(check)
                1350727   19.062    0.000  203.427    0.000 optimizer.py:167(zero_grad)
                 105075   14.632    0.000  193.499    0.002 layers.py:793(update)
                 105074    8.075    0.000  179.808    0.002 allGraphsTrain.py:51(<listcomp>)
               57036520   39.256    0.000  169.602    0.000 flatten.py:39(forward)
               67543920  167.112    0.000  167.112    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
        1552984051/1552984049  164.276    0.000  166.060    0.000 {built-in method builtins.len}
                1611958  152.581    0.000  152.581    0.000 {built-in method tensor}
               16629020  150.465    0.000  150.465    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               12401949  147.695    0.000  147.695    0.000 {built-in method zeros}
                1138681    1.114    0.000  133.188    0.000 game.py:38(board)
               11032770  129.156    0.000  129.156    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               16629020  123.708    0.000  123.708    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               10507400  122.641    0.000  122.641    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              171199399   76.694    0.000  108.675    0.000 _VF.py:25(__getattr__)
               74457231   47.285    0.000  106.526    0.000 {built-in method builtins.all}
                 105074   50.730    0.000   97.616    0.001 agent.py:67(modify)
              170268968   96.505    0.000   96.505    0.000 functional.py:1686(<listcomp>)
               92823555   71.712    0.000   89.149    0.000 types.py:171(__get__)
                8314510   86.344    0.000   86.344    0.000 {method 'add' of 'torch._C._TensorBase' objects}
               55580719   86.044    0.000   86.044    0.000 {method 'detach' of 'torch._C._TensorBase' objects}
                 210148    0.552    0.000   82.538    0.000 network.py:28(forward)
                8314510   79.992    0.000   79.992    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                 613310    4.796    0.000   77.323    0.000 allGraphs.py:167(format)
              429794646   71.619    0.000   71.619    0.000 {built-in method builtins.getattr}
                8314510   69.803    0.000   69.803    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               10507400   19.571    0.000   68.553    0.000 layers.py:838(isFree)
              171319828   66.952    0.000   66.952    0.000 {method 'dim' of 'torch._C._TensorBase' objects}
              249631824   46.562    0.000   66.432    0.000 enum.py:646(__hash__)
                1350727    1.715    0.000   65.352    0.000 loss.py:445(forward)
                1350727    6.388    0.000   63.637    0.000 functional.py:2637(mse_loss)
                8314510   62.111    0.000   62.111    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                2768832   59.254    0.000   59.254    0.000 {built-in method cat}
              514649057   58.967    0.000   58.967    0.000 _jit_internal.py:750(is_scripting)
                 105683    1.043    0.000   58.180    0.001 layers.py:849(restart)
               56826372   39.782    0.000   56.524    0.000 container.py:107(__iter__)
                 945675   27.904    0.000   51.731    0.000 layer.py:175(NoRock_update)
              191849193   51.197    0.000   51.197    0.000 tensor.py:24(<genexpr>)
                 105074    1.248    0.000   50.092    0.000 agent.py:112(__call__)
                 105683    0.500    0.000   49.113    0.000 level.py:8(__init__)
               92949120   37.421    0.000   48.982    0.000 layer.py:103(isFree)
                8314510   48.422    0.000   48.422    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                 105683    1.640    0.000   44.193    0.000 levels.py:249(generate)
                9041191   42.366    0.000   42.366    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9651546: <Diamonds2_0.0_NN_0> in cluster <dcc> Done

Job <Diamonds2_0.0_NN_0> was submitted from host <n-62-27-18> by user <s183905> in cluster <dcc> at Tue May 18 21:12:59 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue May 18 21:13:00 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue May 18 21:13:00 2021
Terminated at Wed May 19 07:08:30 2021
Results reported at Wed May 19 07:08:30 2021

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

Successfully completed.

Resource usage summary:

    CPU time :                                   35607.92 sec.
    Max Memory :                                 2060 MB
    Average Memory :                             2051.97 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14324.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35756 sec.
    Turnaround time :                            35731 sec.

The output (if any) is above this job summary.

