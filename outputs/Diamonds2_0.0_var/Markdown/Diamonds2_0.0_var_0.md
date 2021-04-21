
# Parameters

    Name :                      Diamonds2_0.0_var-0
    Main :                      graphTrain
    Level :                     Levels.Causal5
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
    Counterfacts :              2
    Topn :                      5
    Random counterfacts :       False
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      35042670123 function calls (31413199768 primitive calls) in 35710.94 seconds

##    Ordered by: cumulative time
   List reduced from 467 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35710.938 35710.938 {built-in method builtins.exec}
                      1    0.001    0.001 35710.938 35710.938 <string>:1(<module>)
                      1   98.715   98.715 35710.937 35710.937 allGraphsTrain.py:10(graphTrain)
                 388522 5821.041    0.015 13089.213    0.034 allGraphs.py:146(transformNot)
                 388522    9.994    0.000 8427.693    0.022 allGraphsTrain.py:29(<listcomp>)
               39240823 2179.884    0.000 8417.753    0.000 allGraphs.py:110(states)
                 388522  440.296    0.001 7561.939    0.019 allGraphsTrain.py:35(<listcomp>)
              543934504 7388.711    0.000 7388.711    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                5400474   10.573    0.000 7121.643    0.001 allGraphs.py:158(getInterventions)
              505079200 6548.049    0.000 6548.049    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                4779607    4.651    0.000 6450.354    0.001 allGraphs.py:129(rightIntervention)
        622725426/4779607  374.166    0.000 6423.689    0.001 {built-in method builtins.min}
               17631280    7.222    0.000 6413.622    0.000 allGraphs.py:130(<lambda>)
        1240671245/17631280 1844.982    0.000 6406.399    0.000 allGraphs.py:74(expected_moves)
        1840985784/60272036  490.056    0.000 6286.071    0.000 allGraphs.py:78(<genexpr>)
                 388522    1.325    0.000 2186.400    0.006 game.py:41(step)
                 388522    1.829    0.000 2093.339    0.005 layers.py:718(step)
             9833914598 1437.057    0.000 2072.899    0.000 enum.py:646(__hash__)
              623346293  320.338    0.000 2011.408    0.000 allGraphs.py:83(layers_not_in)
              623346293  803.338    0.000 1691.070    0.000 allGraphs.py:84(<listcomp>)
                 388522  103.907    0.000 1390.573    0.004 allGraphsTrain.py:37(<listcomp>)
                 388522   27.023    0.000 1078.266    0.003 layers.py:17(step)
               38852200   59.601    0.000 1047.986    0.000 layer.py:98(move)
                 388522    1.233    0.000 1027.686    0.003 agent.py:29(learn)
                 388522    8.016    0.000 1025.682    0.003 agent.py:117(_learn)
                 388522   29.931    0.000 1017.667    0.003 learner.py:42(Qlearn)
                 388523   51.068    0.000 1011.235    0.003 layers.py:684(update)
                9007451  915.157    0.000  915.157    0.000 {built-in method tensor}
             1240671245  583.809    0.000  851.759    0.000 allGraphs.py:45(p)
                7343085    4.757    0.000  849.550    0.000 game.py:37(board)
               41183332  102.124    0.000  838.375    0.000 tensor.py:21(wrapped)
                 388522   35.929    0.000  803.838    0.002 allGraphsTrain.py:44(<listcomp>)
               38852200  144.786    0.000  705.294    0.000 layers.py:735(check)
                5400474   27.943    0.000  650.655    0.000 allGraphs.py:153(format)
             9833915907  635.842    0.000  635.842    0.000 {built-in method builtins.hash}
               40794810  623.890    0.000  623.890    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               38852200  573.505    0.000  573.505    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                1157419    9.542    0.000  520.795    0.000 layers.py:740(restart)
                 388522  246.535    0.001  435.996    0.001 agent.py:67(modify)
                1157419    4.457    0.000  433.939    0.000 level.py:8(__init__)
                 388522    2.188    0.000  431.850    0.001 grad_mode.py:23(decorate_context)
                 388522   10.942    0.000  425.307    0.001 adam.py:55(step)
                1157419   16.046    0.000  393.756    0.000 levels.py:249(generate)
        8936006/1165566   35.665    0.000  371.895    0.000 module.py:715(_call_impl)
                 388522   77.769    0.000  366.946    0.001 functional.py:53(adam)
                7520975   64.317    0.000  360.737    0.000 level.py:41(notUsed)
                 777044    2.080    0.000  340.959    0.000 network.py:27(forward)
                 777044    8.555    0.000  334.310    0.000 container.py:115(forward)
                 388522    2.118    0.000  231.583    0.001 tensor.py:181(backward)
                 388522    1.396    0.000  229.465    0.001 __init__.py:68(backward)
               38852200   64.010    0.000  227.728    0.000 layers.py:729(isFree)
             1242457678  222.603    0.000  226.227    0.000 {built-in method builtins.max}
                 388522  218.231    0.001  218.231    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              107628976   60.822    0.000  215.741    0.000 {built-in method builtins.any}
                 388522    4.996    0.000  197.651    0.001 agent.py:112(__call__)
                3496707  109.333    0.000  192.962    0.000 layer.py:167(NoRock_update)
               40406288  191.570    0.000  191.570    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7520975    5.096    0.000  168.156    0.000 level.py:38(elementsIn)
              334247386  127.448    0.000  163.718    0.000 layer.py:95(isFree)
                1554088    2.603    0.000  131.431    0.000 conv.py:422(forward)
                1165566    4.644    0.000  130.349    0.000 tensor.py:576(__iter__)
                1554088    3.161    0.000  127.898    0.000 conv.py:414(_conv_forward)
                1554088  124.227    0.000  124.227    0.000 {built-in method conv2d}
                1165566  122.605    0.000  122.605    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
              376948810   93.771    0.000  113.663    0.000 layers.py:700(<genexpr>)
               80035632   24.585    0.000  111.315    0.000 {built-in method builtins.all}
                7520975   53.720    0.000  108.685    0.000 level.py:39(<listcomp>)
               67602962   32.910    0.000  106.978    0.000 overrides.py:1070(has_torch_function)
               38852200   64.524    0.000  104.439    0.000 layers.py:349(check)
                1554088    3.549    0.000   99.465    0.000 linear.py:92(forward)
               38852200   60.929    0.000   98.700    0.000 layers.py:387(check)
               38852200   58.769    0.000   97.438    0.000 layers.py:337(check)
               38852200   58.624    0.000   96.204    0.000 layers.py:375(check)
                1554088    6.376    0.000   94.422    0.000 functional.py:1669(linear)
               21757286   55.704    0.000   88.139    0.000 tensor.py:933(grad)
              948351400   85.471    0.000   85.471    0.000 layer.py:91(positions)
                 388522    7.883    0.000   85.306    0.000 optimizer.py:167(zero_grad)
              354722204   78.000    0.000   78.000    0.000 level.py:32(inverse)
                6216352   77.067    0.000   77.067    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              122254888   29.536    0.000   76.569    0.000 layers.py:690(<genexpr>)
                 388522   44.605    0.000   74.792    0.000 collector.py:46(collect)
               10416771    7.324    0.000   74.173    0.000 layer.py:69(restart)
                1554088   67.869    0.000   67.869    0.000 {built-in method addmm}
                6216352   65.545    0.000   65.545    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 388522    2.926    0.000   64.936    0.000 agent.py:59(modify_board)
                1157519   27.712    0.000   55.927    0.000 layers.py:36(reset)
                7520975   33.900    0.000   54.375    0.000 {built-in method _functools.reduce}
              312423749   52.257    0.000   52.257    0.000 enum.py:352(<genexpr>)
              168269380   48.149    0.000   48.149    0.000 layer.py:146(elements)
               38852200   30.275    0.000   47.410    0.000 layers.py:364(check)
                2331132    2.012    0.000   47.376    0.000 activation.py:713(forward)
                2331132    3.248    0.000   45.364    0.000 functional.py:1292(leaky_relu)
               38852200   28.850    0.000   45.311    0.000 layers.py:326(check)
                3108176   41.947    0.000   41.947    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2331132   41.819    0.000   41.819    0.000 {built-in method torch._C._nn.leaky_relu}
                 388522   41.180    0.000   41.180    0.000 {built-in method torch._C._nn.one_hot}
              177943344   34.438    0.000   41.023    0.000 overrides.py:1083(<genexpr>)
               81210581   29.801    0.000   40.513    0.000 layer.py:130(add)
                 388522   26.072    0.000   38.939    0.000 allGraphsTrain.py:43(<listcomp>)
               38852200   26.256    0.000   38.598    0.000 layers.py:23(check)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532037: <Diamonds2_0.0_var_0> in cluster <dcc> Done

Job <Diamonds2_0.0_var_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:45 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 04:48:43 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 04:48:43 2021
Terminated at Tue Apr 20 14:44:03 2021
Results reported at Tue Apr 20 14:44:03 2021

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

    CPU time :                                   35618.34 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2058.58 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35823 sec.
    Turnaround time :                            263718 sec.

The output (if any) is above this job summary.

