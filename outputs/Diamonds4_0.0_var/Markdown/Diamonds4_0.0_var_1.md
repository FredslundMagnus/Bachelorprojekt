
# Parameters

    Name :                      Diamonds4_0.0_var-1
    Main :                      graphTrain
    Level :                     Levels.Causal7
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


      16041254552 function calls (15704129519 primitive calls) in 35708.24 seconds

##    Ordered by: cumulative time
   List reduced from 466 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.242 35708.242 {built-in method builtins.exec}
                      1    0.001    0.001 35708.242 35708.242 <string>:1(<module>)
                      1  151.190  151.190 35708.241 35708.241 allGraphsTrain.py:10(graphTrain)
                 606484 6501.115    0.011 14612.166    0.024 allGraphs.py:146(transformNot)
                 606484   15.765    0.000 8858.796    0.015 allGraphsTrain.py:29(<listcomp>)
               61254985 2300.647    0.000 8843.079    0.000 allGraphs.py:110(states)
              606489248 8238.421    0.000 8238.421    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              545836000 7112.836    0.000 7112.836    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 606484    2.138    0.000 3053.270    0.005 game.py:41(step)
                 606484    2.794    0.000 2918.054    0.005 layers.py:718(step)
                 606484  683.974    0.001 2251.839    0.004 allGraphsTrain.py:35(<listcomp>)
                 606484  164.687    0.000 2181.671    0.004 allGraphsTrain.py:37(<listcomp>)
                 606484    1.906    0.000 1616.025    0.003 agent.py:29(learn)
                 606484   12.587    0.000 1612.907    0.003 agent.py:117(_learn)
                 606484   46.554    0.000 1600.320    0.003 learner.py:42(Qlearn)
                8741207   15.723    0.000 1567.865    0.000 allGraphs.py:158(getInterventions)
                 606485   78.714    0.000 1527.072    0.003 layers.py:684(update)
                 606484   42.166    0.000 1384.975    0.002 layers.py:17(step)
               60648400   92.963    0.000 1337.768    0.000 layer.py:98(move)
               64287304  162.876    0.000 1324.104    0.000 tensor.py:21(wrapped)
                 606484   55.368    0.000 1267.847    0.002 allGraphsTrain.py:44(<listcomp>)
               14353819 1215.392    0.000 1215.392    0.000 {built-in method tensor}
               11773628    7.014    0.000 1124.281    0.000 game.py:37(board)
               63680820  984.496    0.000  984.496    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               60648400  900.578    0.000  900.578    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                8741207   38.330    0.000  859.559    0.000 allGraphs.py:153(format)
               60648400  174.417    0.000  833.007    0.000 layers.py:735(check)
                2317587   16.572    0.000  821.225    0.000 layers.py:740(restart)
                 606484  404.088    0.001  703.029    0.001 agent.py:67(modify)
                8179975    6.894    0.000  684.321    0.000 allGraphs.py:129(rightIntervention)
                 606484    3.457    0.000  676.829    0.001 grad_mode.py:23(decorate_context)
                 606484   17.128    0.000  666.535    0.001 adam.py:55(step)
                2317587    8.127    0.000  657.629    0.000 level.py:8(__init__)
        73890458/8179975   46.799    0.000  646.836    0.000 {built-in method builtins.min}
               20752560    8.577    0.000  633.991    0.000 allGraphs.py:130(<lambda>)
        139600941/20752560  196.391    0.000  625.414    0.000 allGraphs.py:74(expected_moves)
        13949132/1819452   55.589    0.000  585.066    0.000 module.py:715(_call_impl)
                 606484  122.060    0.000  574.519    0.001 functional.py:53(adam)
                2317587   23.897    0.000  573.255    0.000 levels.py:441(generate)
                1212968    3.197    0.000  536.190    0.000 network.py:27(forward)
                1212968   14.039    0.000  526.020    0.000 container.py:115(forward)
               11124189   95.017    0.000  523.821    0.000 level.py:41(notUsed)
             2159821283  350.023    0.000  517.971    0.000 enum.py:646(__hash__)
        184558864/44122758   51.246    0.000  513.596    0.000 allGraphs.py:78(<genexpr>)
                 606484    3.246    0.000  364.581    0.001 tensor.py:181(backward)
                 606484    2.134    0.000  361.336    0.001 __init__.py:68(backward)
                 606484  343.668    0.001  343.668    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               60648400   82.876    0.000  323.457    0.000 layers.py:729(isFree)
                 606484    7.717    0.000  309.243    0.001 agent.py:112(__call__)
               63074336  297.002    0.000  297.002    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              167498168   86.084    0.000  294.925    0.000 {built-in method builtins.any}
                4245395  156.108    0.000  268.836    0.000 layer.py:167(NoRock_update)
               11124189    7.498    0.000  246.218    0.000 level.py:38(elementsIn)
              416378911  190.716    0.000  240.580    0.000 layer.py:95(isFree)
                2425936    4.305    0.000  206.178    0.000 conv.py:422(forward)
               74451690   42.973    0.000  205.641    0.000 allGraphs.py:83(layers_not_in)
                1819452    7.358    0.000  204.511    0.000 tensor.py:576(__iter__)
                2425936    4.961    0.000  200.322    0.000 conv.py:414(_conv_forward)
                2425936  194.548    0.000  194.548    0.000 {built-in method conv2d}
              124935804   42.815    0.000  193.215    0.000 {built-in method builtins.all}
                1819452  192.238    0.000  192.238    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
             2159823296  167.948    0.000  167.948    0.000 {built-in method builtins.hash}
              105528350   51.370    0.000  167.303    0.000 overrides.py:1070(has_torch_function)
               60648400  101.363    0.000  166.301    0.000 layers.py:632(check)
               74451690   78.890    0.000  162.668    0.000 allGraphs.py:84(<listcomp>)
               11124189   77.690    0.000  160.233    0.000 level.py:39(<listcomp>)
               60648400   96.912    0.000  159.301    0.000 layers.py:602(check)
                2425936    5.822    0.000  156.161    0.000 linear.py:92(forward)
               60648400   94.318    0.000  155.443    0.000 layers.py:617(check)
                2425936    9.660    0.000  147.891    0.000 functional.py:1669(linear)
              466647304  116.878    0.000  143.569    0.000 layers.py:700(<genexpr>)
               16223109   11.770    0.000  141.635    0.000 layer.py:69(restart)
               33963158   90.073    0.000  140.636    0.000 tensor.py:933(grad)
                 606484   12.488    0.000  136.016    0.000 optimizer.py:167(zero_grad)
              226651984   57.017    0.000  134.434    0.000 layers.py:690(<genexpr>)
                9703744  120.012    0.000  120.012    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 606484   69.920    0.000  117.328    0.000 collector.py:46(collect)
                2317687   56.082    0.000  111.618    0.000 layers.py:36(reset)
             1208943746  107.999    0.000  107.999    0.000 layer.py:91(positions)
              534100548  107.528    0.000  107.528    0.000 level.py:32(inverse)
                2425936  106.521    0.000  106.521    0.000 {built-in method addmm}
                 606484    4.828    0.000  102.777    0.000 agent.py:59(modify_board)
                9703744  102.129    0.000  102.129    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
              139600941   66.044    0.000   98.398    0.000 allGraphs.py:45(p)
              483905429   82.253    0.000   82.253    0.000 enum.py:352(<genexpr>)
               11124189   49.126    0.000   78.486    0.000 {built-in method _functools.reduce}
                3638904    3.149    0.000   75.234    0.000 activation.py:713(forward)
               60648400   46.728    0.000   73.495    0.000 layers.py:588(check)
                3638904    5.142    0.000   72.085    0.000 functional.py:1292(leaky_relu)
              143218610   52.348    0.000   71.371    0.000 layer.py:130(add)
                2317587   35.923    0.000   70.816    0.000 level.py:16(<dictcomp>)
              292630311   68.744    0.000   68.744    0.000 layer.py:146(elements)
                3638904   66.491    0.000   66.491    0.000 {built-in method torch._C._nn.leaky_relu}
                4851872   66.027    0.000   66.027    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                 606484   65.371    0.000   65.371    0.000 {built-in method torch._C._nn.one_hot}
              277769940   54.617    0.000   64.901    0.000 overrides.py:1083(<genexpr>)
               60648400   42.273    0.000   62.125    0.000 layers.py:23(check)
                 606484   40.905    0.000   61.201    0.000 allGraphsTrain.py:43(<listcomp>)
                4851872   59.139    0.000   59.139    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                4851872   54.631    0.000   54.631    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532044: <Diamonds4_0.0_var_1> in cluster <dcc> Done

Job <Diamonds4_0.0_var_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:46 2021
Job was executed on host(s) <n-62-20-3>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 17:52:48 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 17:52:48 2021
Terminated at Wed Apr 21 03:48:01 2021
Results reported at Wed Apr 21 03:48:01 2021

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

    CPU time :                                   35618.02 sec.
    Max Memory :                                 2061 MB
    Average Memory :                             2060.29 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14323.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35774 sec.
    Turnaround time :                            310755 sec.

The output (if any) is above this job summary.

