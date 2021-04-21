
# Parameters

    Name :                      Diamonds3_0.5_var-1
    Main :                      graphTrain
    Level :                     Levels.Causal6
    Failed actions chance :     0.5
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
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      28399875143 function calls (25643540324 primitive calls) in 35708.94 seconds

##    Ordered by: cumulative time
   List reduced from 465 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35708.944 35708.944 {built-in method builtins.exec}
                      1    0.002    0.002 35708.943 35708.943 <string>:1(<module>)
                      1  115.154  115.154 35708.942 35708.942 allGraphsTrain.py:10(graphTrain)
                 461161 5859.651    0.013 13253.447    0.029 allGraphs.py:146(transformNot)
                 461161   12.898    0.000 8310.768    0.018 allGraphsTrain.py:29(<listcomp>)
               46577362 2132.524    0.000 8297.888    0.000 allGraphs.py:110(states)
              553397388 7522.140    0.000 7522.140    0.000 {method 'item' of 'torch._C._TensorBase' objects}
              507277600 6554.892    0.000 6554.892    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 461161  554.005    0.001 6476.370    0.014 allGraphsTrain.py:35(<listcomp>)
                9757409   17.982    0.000 5922.365    0.001 allGraphs.py:158(getInterventions)
                8796027    7.714    0.000 4822.131    0.001 allGraphs.py:129(rightIntervention)
        493673485/8796027  253.971    0.000 4777.804    0.001 {built-in method builtins.min}
               33939487   14.123    0.000 4760.556    0.000 allGraphs.py:130(<lambda>)
        978550943/33939487 1405.842    0.000 4746.433    0.000 allGraphs.py:74(expected_moves)
        1429488914/111866612  393.604    0.000 4534.249    0.000 allGraphs.py:78(<genexpr>)
                 461161    1.736    0.000 2376.881    0.005 game.py:41(step)
                 461161    2.225    0.000 2269.196    0.005 layers.py:718(step)
                 461161  125.152    0.000 1653.716    0.004 allGraphsTrain.py:37(<listcomp>)
             6975534944 1070.455    0.000 1568.906    0.000 enum.py:646(__hash__)
              494634867  259.644    0.000 1471.295    0.000 allGraphs.py:83(layers_not_in)
                 461162   61.710    0.000 1380.072    0.003 layers.py:684(update)
               14032582 1337.909    0.000 1337.909    0.000 {built-in method tensor}
               12063215    7.090    0.000 1267.607    0.000 game.py:37(board)
                 461161    1.473    0.000 1232.307    0.003 agent.py:29(learn)
                 461161    9.459    0.000 1229.769    0.003 agent.py:117(_learn)
                 461161   35.778    0.000 1220.310    0.003 learner.py:42(Qlearn)
              494634867  573.844    0.000 1211.651    0.000 allGraphs.py:84(<listcomp>)
                9757409   46.728    0.000 1067.306    0.000 allGraphs.py:153(format)
               48883066  124.360    0.000 1012.420    0.000 tensor.py:21(wrapped)
                 461161   43.419    0.000  971.190    0.002 allGraphsTrain.py:44(<listcomp>)
                 461161   32.372    0.000  884.153    0.002 layers.py:17(step)
               46116100   68.644    0.000  847.529    0.000 layer.py:98(move)
               48421905  748.743    0.000  748.743    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1670385   13.417    0.000  724.174    0.000 layers.py:740(restart)
              978550943  459.448    0.000  684.284    0.000 allGraphs.py:45(p)
               46116100  680.943    0.000  680.943    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1670385    6.285    0.000  597.922    0.000 level.py:8(__init__)
                1670385   21.105    0.000  533.307    0.000 levels.py:288(generate)
                 461161  302.849    0.001  529.523    0.001 agent.py:67(modify)
                 461161    2.606    0.000  516.922    0.001 grad_mode.py:23(decorate_context)
                 461161   13.525    0.000  509.209    0.001 adam.py:55(step)
             6975536509  498.452    0.000  498.452    0.000 {built-in method builtins.hash}
               10022412   89.970    0.000  489.220    0.000 level.py:41(notUsed)
               46116100  104.763    0.000  447.292    0.000 layers.py:735(check)
        10606703/1383483   41.869    0.000  442.155    0.000 module.py:715(_call_impl)
                 461161   92.457    0.000  437.620    0.001 functional.py:53(adam)
                 922322    2.536    0.000  405.518    0.000 network.py:27(forward)
                 922322   10.246    0.000  397.301    0.000 container.py:115(forward)
                 461161    2.551    0.000  278.225    0.001 tensor.py:181(backward)
                 461161    1.624    0.000  275.674    0.001 __init__.py:68(backward)
                 461161  262.350    0.001  262.350    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
               46116100   72.404    0.000  262.054    0.000 layers.py:729(isFree)
              127454930   69.908    0.000  248.253    0.000 {built-in method builtins.any}
                 461161    5.729    0.000  234.156    0.001 agent.py:112(__call__)
               10022412    6.768    0.000  228.721    0.000 level.py:38(elementsIn)
               47960744  227.741    0.000  227.741    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3689296  126.921    0.000  227.003    0.000 layer.py:167(NoRock_update)
               94999266   36.298    0.000  221.571    0.000 {built-in method builtins.all}
              348865585  146.859    0.000  189.650    0.000 layer.py:95(isFree)
              980895808  169.573    0.000  174.993    0.000 {built-in method builtins.max}
              215812230   55.477    0.000  172.135    0.000 layers.py:690(<genexpr>)
                1844644    3.078    0.000  155.937    0.000 conv.py:422(forward)
                1383483    5.354    0.000  154.595    0.000 tensor.py:576(__iter__)
                1844644    3.434    0.000  151.660    0.000 conv.py:414(_conv_forward)
               10022412   71.256    0.000  150.499    0.000 level.py:39(<listcomp>)
                1844644  147.575    0.000  147.575    0.000 {built-in method conv2d}
                1383483  145.395    0.000  145.395    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               80242148   39.746    0.000  132.390    0.000 overrides.py:1070(has_torch_function)
              400012335  101.113    0.000  124.693    0.000 layers.py:700(<genexpr>)
                1844644    4.386    0.000  118.348    0.000 linear.py:92(forward)
                1844644    7.389    0.000  112.132    0.000 functional.py:1669(linear)
               25825070   68.470    0.000  108.546    0.000 tensor.py:933(grad)
               13363080    9.416    0.000  108.397    0.000 layer.py:69(restart)
                 461161    9.787    0.000  104.763    0.000 optimizer.py:167(zero_grad)
              475395772  103.264    0.000  103.264    0.000 level.py:32(inverse)
               23059957   56.509    0.000   96.404    0.000 layers.py:424(check)
                7378576   91.449    0.000   91.449    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                 461161   52.812    0.000   88.922    0.000 collector.py:46(collect)
                1670485   40.319    0.000   83.016    0.000 layers.py:36(reset)
                1844644   80.927    0.000   80.927    0.000 {built-in method addmm}
                 461161    3.629    0.000   77.994    0.000 agent.py:59(modify_board)
                7378576   77.747    0.000   77.747    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               46116200   47.637    0.000   76.685    0.000 layers.py:442(isDone)
               10022412   44.697    0.000   71.454    0.000 {built-in method _functools.reduce}
              420942221   70.527    0.000   70.527    0.000 enum.py:352(<genexpr>)
              688678762   67.009    0.000   67.009    0.000 layer.py:91(positions)
               23062132   39.669    0.000   65.235    0.000 layers.py:437(check)
               23056047   38.203    0.000   63.797    0.000 layers.py:452(check)
              105581389   42.888    0.000   58.047    0.000 layer.py:130(add)
              217195359   57.836    0.000   57.836    0.000 layer.py:146(elements)
                2766966    2.367    0.000   56.372    0.000 activation.py:713(forward)
                1670385   28.695    0.000   54.103    0.000 level.py:16(<dictcomp>)
                2766966    3.907    0.000   54.005    0.000 functional.py:1292(leaky_relu)
              211212006   44.579    0.000   53.369    0.000 overrides.py:1083(<genexpr>)
                3689288   49.901    0.000   49.901    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2766966   49.734    0.000   49.734    0.000 {built-in method torch._C._nn.leaky_relu}
                 461161   49.629    0.000   49.629    0.000 {built-in method torch._C._nn.one_hot}
                 461161   31.998    0.000   47.919    0.000 allGraphsTrain.py:43(<listcomp>)
                3689288   45.518    0.000   45.518    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
                3689288   41.923    0.000   41.923    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}


Traceback (most recent call last):
  File "main.py", line 227, in <module>
    run(Defaults)
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/auxillaries.py", line 132, in run
    (serverRun if isServer else Defaults.main).__call__(getvals(Defaults))
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/server.py", line 37, in serverRun
    profilingStats()
  File "/zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils/debug.py", line 62, in profilingStats
    os.remove('stats')
FileNotFoundError: [Errno 2] No such file or directory: 'stats'

------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532016: <Diamonds3_0.5_var_1> in cluster <dcc> Exited

Job <Diamonds3_0.5_var_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:42 2021
Job was executed on host(s) <n-62-20-2>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Sun Apr 18 19:10:10 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sun Apr 18 19:10:10 2021
Terminated at Mon Apr 19 05:05:28 2021
Results reported at Mon Apr 19 05:05:28 2021

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

Exited with exit code 1.

Resource usage summary:

    CPU time :                                   35619.40 sec.
    Max Memory :                                 2078 MB
    Average Memory :                             2058.30 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14306.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35748 sec.
    Turnaround time :                            142606 sec.

The output (if any) is above this job summary.

