
# Parameters

    Name :                      Diamonds3_0.0_var-2
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


      30064831071 function calls (27720413452 primitive calls) in 35708.85 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.849 35708.849 {built-in method builtins.exec}
                      1    0.002    0.002 35708.849 35708.849 <string>:1(<module>)
                      1  190.157  190.157 35708.847 35708.847 allGraphsTrain.py:10(graphTrain)
                 537586 4854.102    0.009 12121.356    0.023 allGraphs.py:146(transformNot)
              645107996 8552.760    0.000 8552.760    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 537586   14.661    0.000 8022.065    0.015 allGraphsTrain.py:29(<listcomp>)
               54296287 1774.076    0.000 8007.457    0.000 allGraphs.py:110(states)
                 537586  576.625    0.001 5887.029    0.011 allGraphsTrain.py:35(<listcomp>)
              591345100 5542.002    0.000 5542.002    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                8265179   16.816    0.000 5310.404    0.001 allGraphs.py:158(getInterventions)
                7524100    7.959    0.000 4356.524    0.001 allGraphs.py:129(rightIntervention)
        419495730/7524100  233.383    0.000 4314.844    0.001 {built-in method builtins.min}
               28965352   13.186    0.000 4299.070    0.000 allGraphs.py:130(<lambda>)
        831467360/28965352 1281.014    0.000 4285.884    0.000 allGraphs.py:74(expected_moves)
        1214473638/95281760  350.707    0.000 4090.589    0.000 allGraphs.py:78(<genexpr>)
                 537586    2.855    0.000 3985.661    0.007 game.py:41(step)
                 537586    3.713    0.000 3858.372    0.007 layers.py:718(step)
                 537587   89.786    0.000 2146.520    0.004 layers.py:684(update)
                 537586   52.190    0.000 1703.388    0.003 layers.py:17(step)
               53758600   98.930    0.000 1645.944    0.000 layer.py:98(move)
                 537586  102.064    0.000 1626.346    0.003 allGraphsTrain.py:37(<listcomp>)
             6796802644 1111.456    0.000 1618.110    0.000 enum.py:646(__hash__)
              420236809  239.625    0.000 1335.491    0.000 allGraphs.py:83(layers_not_in)
                 537586    2.767    0.000 1330.870    0.002 agent.py:29(learn)
                 537586   13.761    0.000 1326.766    0.002 agent.py:117(_learn)
                 537586   41.399    0.000 1313.005    0.002 learner.py:42(Qlearn)
               13243988 1268.451    0.000 1268.451    0.000 {built-in method tensor}
                2600091   24.453    0.000 1224.571    0.000 layers.py:740(restart)
               10953110    7.995    0.000 1184.750    0.000 game.py:37(board)
              420236809  521.468    0.000 1095.866    0.000 allGraphs.py:84(<listcomp>)
               53758600  195.572    0.000 1017.575    0.000 layers.py:735(check)
                2600091   11.405    0.000 1003.982    0.000 level.py:8(__init__)
               56984116  139.070    0.000  954.599    0.000 tensor.py:21(wrapped)
                8265179   40.317    0.000  923.729    0.000 allGraphs.py:153(format)
                 537586   42.166    0.000  896.165    0.002 allGraphsTrain.py:44(<listcomp>)
                2600091   35.185    0.000  890.449    0.000 levels.py:288(generate)
               15602889  144.965    0.000  816.627    0.000 level.py:41(notUsed)
               56446530  649.211    0.000  649.211    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                 537586  335.834    0.001  618.911    0.001 agent.py:67(modify)
               53758600  612.102    0.000  612.102    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
              831467360  416.571    0.000  610.255    0.000 allGraphs.py:45(p)
        12364478/1612758   63.116    0.000  572.284    0.000 module.py:715(_call_impl)
                1075172    3.755    0.000  517.294    0.000 network.py:27(forward)
             6796804433  506.654    0.000  506.654    0.000 {built-in method builtins.hash}
                1075172   14.061    0.000  503.760    0.000 container.py:115(forward)
                 537586    4.745    0.000  488.374    0.001 grad_mode.py:23(decorate_context)
                 537586   19.541    0.000  475.058    0.001 adam.py:55(step)
               53758600   93.613    0.000  432.846    0.000 layers.py:729(isFree)
                 537586   86.802    0.000  387.394    0.001 functional.py:53(adam)
               15602889   11.588    0.000  382.631    0.000 level.py:38(elementsIn)
              418728320  283.572    0.000  339.233    0.000 layer.py:95(isFree)
                4300696  196.545    0.000  334.857    0.000 layer.py:167(NoRock_update)
                 537586    3.744    0.000  329.303    0.001 tensor.py:181(backward)
                 537586    3.055    0.000  325.558    0.001 __init__.py:68(backward)
                 537586   12.187    0.000  324.584    0.001 agent.py:112(__call__)
              147924224   87.026    0.000  315.374    0.000 {built-in method builtins.any}
                 537586  307.385    0.001  307.385    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              110742816   46.004    0.000  302.608    0.000 {built-in method builtins.all}
               15602889  120.635    0.000  248.705    0.000 level.py:39(<listcomp>)
              266213737   77.645    0.000  242.541    0.000 layers.py:690(<genexpr>)
               53758600  143.348    0.000  234.354    0.000 layers.py:424(check)
                1612758    8.508    0.000  225.041    0.000 tensor.py:576(__iter__)
                1612758  210.746    0.000  210.746    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2150344    4.826    0.000  207.854    0.000 conv.py:422(forward)
                2150344    6.412    0.000  200.789    0.000 conv.py:414(_conv_forward)
                2150344  193.478    0.000  193.478    0.000 {built-in method conv2d}
               55908944  189.825    0.000  189.825    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
               20800728   17.936    0.000  188.945    0.000 layer.py:69(restart)
              740091621  175.684    0.000  175.684    0.000 level.py:32(inverse)
               53758600  106.367    0.000  166.490    0.000 layers.py:437(check)
              460427481  136.253    0.000  164.722    0.000 layers.py:700(<genexpr>)
               93540098   49.413    0.000  159.937    0.000 overrides.py:1070(has_torch_function)
               53758600   99.901    0.000  159.409    0.000 layers.py:452(check)
              833821197  146.440    0.000  151.766    0.000 {built-in method builtins.max}
                2150344    6.750    0.000  148.579    0.000 linear.py:92(forward)
                2150344   10.615    0.000  138.886    0.000 functional.py:1669(linear)
                2600191   68.955    0.000  138.051    0.000 layers.py:36(reset)
             1259421356  133.080    0.000  133.080    0.000 layer.py:91(positions)
               15602889   77.054    0.000  122.338    0.000 {built-in method _functools.reduce}
              655308809  120.506    0.000  120.506    0.000 enum.py:352(<genexpr>)
               30104870   72.440    0.000  119.961    0.000 tensor.py:933(grad)
                 537586    5.779    0.000  106.154    0.000 agent.py:59(modify_board)
                 537586   10.701    0.000  104.381    0.000 optimizer.py:167(zero_grad)
                2150344  100.769    0.000  100.769    0.000 {built-in method addmm}
               53758700   62.202    0.000   99.151    0.000 layers.py:442(isDone)
                2600091   50.784    0.000   94.865    0.000 level.py:16(<dictcomp>)
              306616423   89.110    0.000   89.110    0.000 layer.py:146(elements)
              150299505   64.216    0.000   88.036    0.000 layer.py:130(add)
               53758600   54.419    0.000   85.346    0.000 layers.py:413(check)
                 537586   48.875    0.000   84.278    0.000 collector.py:46(collect)
                8601376   76.829    0.000   76.829    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               53758600   46.241    0.000   72.267    0.000 layers.py:402(check)
                 537586   69.828    0.000   69.828    0.000 {built-in method torch._C._nn.one_hot}
                 537586   46.815    0.000   66.472    0.000 allGraphsTrain.py:43(<listcomp>)
              246214656   53.305    0.000   63.219    0.000 overrides.py:1083(<genexpr>)
                8601376   63.124    0.000   63.124    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                3225516    4.206    0.000   63.089    0.000 activation.py:713(forward)
                 537586   15.902    0.000   60.236    0.000 allGraphs.py:137(transform)
               53758600   40.432    0.000   59.712    0.000 layers.py:23(check)
                3225516    7.360    0.000   58.883    0.000 functional.py:1292(leaky_relu)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532042: <Diamonds3_0.0_var_2> in cluster <dcc> Done

Job <Diamonds3_0.0_var_2> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:46 2021
Job was executed on host(s) <n-62-20-12>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 17:32:45 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 17:32:45 2021
Terminated at Wed Apr 21 03:28:00 2021
Results reported at Wed Apr 21 03:28:00 2021

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

    CPU time :                                   35620.86 sec.
    Max Memory :                                 2060 MB
    Average Memory :                             2058.95 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14324.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35715 sec.
    Turnaround time :                            309554 sec.

The output (if any) is above this job summary.

