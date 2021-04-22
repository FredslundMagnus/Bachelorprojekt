
# Parameters

    Name :                      Diamonds3_0.0_var-0
    Main :                      graphTrain
    Level :                     Levels.Causal6
    Failed actions chance :     0.0
    Hours :                     10.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.var
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
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      34041582262 function calls (31353135265 primitive calls) in 35710.37 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.372 35710.372 {built-in method builtins.exec}
                      1    0.001    0.001 35710.372 35710.372 <string>:1(<module>)
                      1  136.673  136.673 35710.371 35710.371 allGraphsTrain.py:10(graphTrain)
                 602407 5163.126    0.009 12392.251    0.021 allGraphs.py:146(transformNot)
              722893716 8067.684    0.000 8067.684    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 602407   14.381    0.000 8005.225    0.013 allGraphsTrain.py:29(<listcomp>)
               60843208 1837.862    0.000 7990.914    0.000 allGraphs.py:110(states)
                 602407  522.483    0.001 6133.183    0.010 allGraphsTrain.py:35(<listcomp>)
              662648200 5873.233    0.000 5873.233    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                9283234   15.859    0.000 5610.700    0.001 allGraphs.py:158(getInterventions)
                8625328    7.565    0.000 4617.228    0.001 allGraphs.py:129(rightIntervention)
        481082573/8625328  255.885    0.000 4574.223    0.001 {built-in method builtins.min}
               33201993   13.539    0.000 4557.791    0.000 allGraphs.py:130(<lambda>)
        953539818/33201993 1350.185    0.000 4544.252    0.000 allGraphs.py:74(expected_moves)
        1392795070/109191666  372.034    0.000 4339.701    0.000 allGraphs.py:78(<genexpr>)
                 602407    2.006    0.000 3783.208    0.006 game.py:41(step)
                 602407    2.817    0.000 3658.384    0.006 layers.py:718(step)
                 602408   81.132    0.000 2104.295    0.003 layers.py:684(update)
             7735350774 1173.088    0.000 1683.703    0.000 enum.py:646(__hash__)
                 602407  102.980    0.000 1605.053    0.003 allGraphsTrain.py:37(<listcomp>)
                 602407   41.498    0.000 1548.161    0.003 layers.py:17(step)
               60240700   90.308    0.000 1501.457    0.000 layer.py:98(move)
              481740479  252.114    0.000 1418.565    0.000 allGraphs.py:83(layers_not_in)
               14858633 1314.803    0.000 1314.803    0.000 {built-in method tensor}
                 602407    1.997    0.000 1246.204    0.002 agent.py:29(learn)
                2963509   22.592    0.000 1245.343    0.000 layers.py:740(restart)
                 602407   11.948    0.000 1242.944    0.002 agent.py:117(_learn)
               12295270    6.924    0.000 1235.054    0.000 game.py:37(board)
                 602407   35.676    0.000 1230.996    0.002 learner.py:42(Qlearn)
              481740479  556.973    0.000 1166.450    0.000 allGraphs.py:84(<listcomp>)
                2963509   10.667    0.000 1029.755    0.000 level.py:8(__init__)
               60240700  192.333    0.000  989.323    0.000 layers.py:735(check)
               63855142  135.989    0.000  969.901    0.000 tensor.py:21(wrapped)
                9283234   40.949    0.000  967.152    0.000 allGraphs.py:153(format)
                2963509   36.269    0.000  924.576    0.000 levels.py:288(generate)
                 602407   41.636    0.000  918.187    0.002 allGraphsTrain.py:44(<listcomp>)
               17781682  152.026    0.000  849.093    0.000 level.py:41(notUsed)
               63252735  664.232    0.000  664.232    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
              953539818  437.368    0.000  642.778    0.000 allGraphs.py:45(p)
               60240700  630.770    0.000  630.770    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                 602407  325.212    0.001  574.002    0.001 agent.py:67(modify)
             7735352787  510.615    0.000  510.615    0.000 {built-in method builtins.hash}
                 602407    3.410    0.000  488.812    0.001 grad_mode.py:23(decorate_context)
        13855361/1807221   49.721    0.000  480.057    0.000 module.py:715(_call_impl)
                 602407   16.256    0.000  478.883    0.001 adam.py:55(step)
                1204814    2.898    0.000  438.629    0.000 network.py:27(forward)
                1204814   11.349    0.000  428.487    0.000 container.py:115(forward)
               17781682   11.833    0.000  398.278    0.000 level.py:38(elementsIn)
                 602407   86.763    0.000  393.453    0.001 functional.py:53(adam)
               60240700   94.032    0.000  336.398    0.000 layers.py:729(isFree)
              165710686   89.683    0.000  320.356    0.000 {built-in method builtins.any}
                4819264  180.793    0.000  309.972    0.000 layer.py:167(NoRock_update)
                 602407    3.526    0.000  295.028    0.000 tensor.py:181(backward)
                 602407    1.949    0.000  291.501    0.000 __init__.py:68(backward)
                 602407  277.058    0.000  277.058    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              124095942   45.452    0.000  273.632    0.000 {built-in method builtins.all}
               17781682  130.163    0.000  259.251    0.000 level.py:39(<listcomp>)
                 602407    6.969    0.000  255.884    0.000 agent.py:112(__call__)
              471797952  188.614    0.000  242.366    0.000 layer.py:95(isFree)
               60240700  139.875    0.000  234.309    0.000 layers.py:424(check)
              278014410   73.721    0.000  213.334    0.000 layers.py:690(<genexpr>)
               62650328  195.981    0.000  195.981    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                1807221    6.614    0.000  194.359    0.000 tensor.py:576(__iter__)
               23708072   17.007    0.000  185.575    0.000 layer.py:69(restart)
                1807221  183.467    0.000  183.467    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              843443278  180.369    0.000  180.369    0.000 level.py:32(inverse)
                2409628    3.817    0.000  171.361    0.000 conv.py:422(forward)
                2409628    4.511    0.000  166.084    0.000 conv.py:414(_conv_forward)
              104818952   49.850    0.000  164.753    0.000 overrides.py:1070(has_torch_function)
              515495619  134.445    0.000  164.713    0.000 layers.py:700(<genexpr>)
              956004945  157.324    0.000  161.095    0.000 {built-in method builtins.max}
                2409628  160.753    0.000  160.753    0.000 {built-in method conv2d}
               60240700   96.636    0.000  156.532    0.000 layers.py:452(check)
               60240700   92.941    0.000  149.706    0.000 layers.py:437(check)
                2963609   71.455    0.000  142.076    0.000 layers.py:36(reset)
             1378727304  127.605    0.000  127.605    0.000 layer.py:91(positions)
               17781682   79.306    0.000  127.193    0.000 {built-in method _functools.reduce}
                2409628    5.156    0.000  126.133    0.000 linear.py:92(forward)
              746828405  124.524    0.000  124.524    0.000 enum.py:352(<genexpr>)
               33734846   74.234    0.000  123.396    0.000 tensor.py:933(grad)
                2409628    9.214    0.000  118.675    0.000 functional.py:1669(linear)
                 602407    9.938    0.000  106.705    0.000 optimizer.py:167(zero_grad)
               60240800   57.076    0.000   89.555    0.000 layers.py:457(isDone)
                 602407    4.605    0.000   88.789    0.000 agent.py:59(modify_board)
                2963509   43.666    0.000   87.396    0.000 level.py:16(<dictcomp>)
                 602407   49.240    0.000   84.556    0.000 collector.py:46(collect)
                2409628   84.553    0.000   84.553    0.000 {built-in method addmm}
              170325958   60.483    0.000   82.881    0.000 layer.py:130(add)
              347344181   79.728    0.000   79.728    0.000 layer.py:146(elements)
                9638512   78.733    0.000   78.733    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               60240700   50.612    0.000   77.880    0.000 layers.py:413(check)
               60240700   46.641    0.000   72.457    0.000 layers.py:402(check)
              275902674   55.193    0.000   65.572    0.000 overrides.py:1083(<genexpr>)
                9638512   65.381    0.000   65.381    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 602407   40.499    0.000   60.594    0.000 allGraphsTrain.py:43(<listcomp>)
               60240700   39.898    0.000   60.197    0.000 layers.py:23(check)
                 602407   58.233    0.000   58.233    0.000 {built-in method torch._C._nn.one_hot}
                3614442    3.562    0.000   57.448    0.000 activation.py:713(forward)
                3614442    5.107    0.000   53.887    0.000 functional.py:1292(leaky_relu)
                4819256   49.508    0.000   49.508    0.000 {method 'add' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532040: <Diamonds3_0.0_var_0> in cluster <dcc> Done

Job <Diamonds3_0.0_var_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:45 2021
Job was executed on host(s) <n-62-20-7>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 17:08:21 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 17:08:21 2021
Terminated at Wed Apr 21 03:03:42 2021
Results reported at Wed Apr 21 03:03:42 2021

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
#BSUB -W 720
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   35658.27 sec.
    Max Memory :                                 2060 MB
    Average Memory :                             2053.75 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14324.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35723 sec.
    Turnaround time :                            308097 sec.

The output (if any) is above this job summary.

