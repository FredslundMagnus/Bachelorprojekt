
# Parameters

    Name :                      Diamonds4_0.0_var-0
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


      19390882789 function calls (18969379802 primitive calls) in 35704.44 seconds

##    Ordered by: cumulative time
   List reduced from 467 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35704.441 35704.441 {built-in method builtins.exec}
                      1    0.001    0.001 35704.441 35704.441 <string>:1(<module>)
                      1  175.628  175.628 35704.440 35704.440 allGraphsTrain.py:10(graphTrain)
                 720455 5610.387    0.008 13424.297    0.019 allGraphs.py:146(transformNot)
              720461160 8732.634    0.000 8732.634    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 720455   17.486    0.000 8551.193    0.012 allGraphsTrain.py:29(<listcomp>)
               72766056 2016.205    0.000 8533.726    0.000 allGraphs.py:110(states)
              648409900 6320.765    0.000 6320.765    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 720455    2.433    0.000 4055.662    0.006 game.py:41(step)
                 720455    3.339    0.000 3907.275    0.005 layers.py:718(step)
                 720455  674.760    0.001 2676.217    0.004 allGraphsTrain.py:35(<listcomp>)
                 720455  142.264    0.000 2119.664    0.003 allGraphsTrain.py:37(<listcomp>)
                 720456  103.919    0.000 2093.571    0.003 layers.py:684(update)
               10958098   18.486    0.000 2001.458    0.000 allGraphs.py:158(getInterventions)
                 720455   56.203    0.000 1806.278    0.003 layers.py:17(step)
               72045500  118.035    0.000 1743.177    0.000 layer.py:98(move)
                 720455    2.281    0.000 1619.059    0.002 agent.py:29(learn)
                 720455   15.497    0.000 1615.241    0.002 agent.py:117(_learn)
                 720455   46.281    0.000 1599.744    0.002 learner.py:42(Qlearn)
               17619065 1424.310    0.000 1424.310    0.000 {built-in method tensor}
               14560374    8.593    0.000 1324.048    0.000 game.py:37(board)
               76368230  182.471    0.000 1278.403    0.000 tensor.py:21(wrapped)
                 720455   54.036    0.000 1211.843    0.002 allGraphsTrain.py:44(<listcomp>)
                2878600   22.180    0.000 1145.571    0.000 layers.py:740(restart)
               72045500  228.560    0.000 1091.002    0.000 layers.py:735(check)
               10958098   46.709    0.000 1028.389    0.000 allGraphs.py:153(format)
               10253166    9.648    0.000  944.142    0.000 allGraphs.py:129(rightIntervention)
                2878600   11.026    0.000  920.531    0.000 level.py:8(__init__)
        92574397/10253166   64.393    0.000  894.378    0.000 {built-in method builtins.min}
               26015695   12.284    0.000  877.660    0.000 allGraphs.py:130(<lambda>)
               75647775  869.781    0.000  869.781    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
        174895628/26015695  268.360    0.000  865.376    0.000 allGraphs.py:74(expected_moves)
               72045500  835.167    0.000  835.167    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2878600   32.824    0.000  803.164    0.000 levels.py:441(generate)
               13816671  133.355    0.000  735.024    0.000 level.py:41(notUsed)
                 720455  410.250    0.001  731.164    0.001 agent.py:67(modify)
        231201164/55308824   72.333    0.000  712.901    0.000 allGraphs.py:78(<genexpr>)
             2646600392  473.387    0.000  691.754    0.000 enum.py:646(__hash__)
                 720455    4.646    0.000  636.614    0.001 grad_mode.py:23(decorate_context)
        16570465/2161365   68.313    0.000  632.066    0.000 module.py:715(_call_impl)
                 720455   21.119    0.000  623.538    0.001 adam.py:55(step)
                1440910    4.369    0.000  577.867    0.000 network.py:27(forward)
                1440910   15.461    0.000  564.399    0.000 container.py:115(forward)
                 720455  113.760    0.000  510.524    0.001 functional.py:53(adam)
               72045500  109.702    0.000  419.020    0.000 layers.py:729(isFree)
              198849035  113.782    0.000  387.801    0.000 {built-in method builtins.any}
                 720455    4.011    0.000  373.434    0.001 tensor.py:181(backward)
                5043192  221.537    0.000  370.356    0.000 layer.py:167(NoRock_update)
                 720455    2.533    0.000  369.423    0.001 __init__.py:68(backward)
                 720455  350.490    0.000  350.490    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
               13816671   10.630    0.000  343.873    0.000 level.py:38(elementsIn)
                 720455    8.621    0.000  335.094    0.000 agent.py:112(__call__)
              488642708  243.102    0.000  309.318    0.000 layer.py:95(isFree)
               93279329   58.906    0.000  283.935    0.000 allGraphs.py:83(layers_not_in)
               74927320  261.526    0.000  261.526    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2161365    8.578    0.000  258.883    0.000 tensor.py:576(__iter__)
              148413830   56.095    0.000  255.278    0.000 {built-in method builtins.all}
                2161365  244.767    0.000  244.767    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
               93279329  109.402    0.000  225.029    0.000 allGraphs.py:84(<listcomp>)
               13816671  109.995    0.000  224.571    0.000 level.py:39(<listcomp>)
                2881820    5.232    0.000  223.321    0.000 conv.py:422(forward)
               72045500  133.075    0.000  219.677    0.000 layers.py:632(check)
              125359304   67.873    0.000  218.954    0.000 overrides.py:1070(has_torch_function)
             2646602789  218.367    0.000  218.367    0.000 {built-in method builtins.hash}
                2881820    5.630    0.000  216.089    0.000 conv.py:414(_conv_forward)
                2881820  209.374    0.000  209.374    0.000 {built-in method conv2d}
               72045500  126.030    0.000  207.260    0.000 layers.py:617(check)
               72045500  123.394    0.000  203.726    0.000 layers.py:602(check)
               20150200   15.564    0.000  195.586    0.000 layer.py:69(restart)
              553336000  153.232    0.000  187.623    0.000 layers.py:700(<genexpr>)
              282855191   80.797    0.000  178.402    0.000 layers.py:690(<genexpr>)
               40345534   98.837    0.000  164.457    0.000 tensor.py:933(grad)
                2881820    6.810    0.000  164.423    0.000 linear.py:92(forward)
                2878700   78.225    0.000  156.678    0.000 layers.py:36(reset)
                2881820   11.961    0.000  154.470    0.000 functional.py:1669(linear)
              663375242  151.041    0.000  151.041    0.000 level.py:32(inverse)
             1407597408  146.258    0.000  146.258    0.000 layer.py:91(positions)
                 720455   13.015    0.000  142.205    0.000 optimizer.py:167(zero_grad)
              174895628   91.012    0.000  134.980    0.000 allGraphs.py:45(p)
              601031249  116.526    0.000  116.526    0.000 enum.py:352(<genexpr>)
                 720455    5.375    0.000  113.603    0.000 agent.py:59(modify_board)
                 720455   64.191    0.000  110.207    0.000 collector.py:46(collect)
                2881820  109.420    0.000  109.420    0.000 {built-in method addmm}
               13816671   68.028    0.000  108.672    0.000 {built-in method _functools.reduce}
               11527280  102.511    0.000  102.511    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                2878600   50.631    0.000   99.014    0.000 level.py:16(<dictcomp>)
              175367939   70.999    0.000   97.156    0.000 layer.py:130(add)
               72045500   59.796    0.000   95.075    0.000 layers.py:588(check)
              357959822   91.626    0.000   91.626    0.000 layer.py:146(elements)
              329968658   72.566    0.000   85.873    0.000 overrides.py:1083(<genexpr>)
               11527280   85.865    0.000   85.865    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                 720455   54.290    0.000   81.745    0.000 allGraphsTrain.py:43(<listcomp>)
               72045500   55.456    0.000   81.233    0.000 layers.py:23(check)
                4322730    4.034    0.000   75.604    0.000 activation.py:713(forward)
                 720455   74.425    0.000   74.425    0.000 {built-in method torch._C._nn.one_hot}
                4322730    6.597    0.000   71.570    0.000 functional.py:1292(leaky_relu)
                4322730   64.342    0.000   64.342    0.000 {built-in method torch._C._nn.leaky_relu}
                 720455   17.028    0.000   62.261    0.000 allGraphs.py:137(transform)
        685940786/685940784   48.384    0.000   60.882    0.000 {built-in method builtins.len}
                5763640   59.701    0.000   59.701    0.000 {method 'add' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532043: <Diamonds4_0.0_var_0> in cluster <dcc> Done

Job <Diamonds4_0.0_var_0> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:46 2021
Job was executed on host(s) <n-62-20-16>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Tue Apr 20 17:46:03 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Tue Apr 20 17:46:03 2021
Terminated at Wed Apr 21 03:41:11 2021
Results reported at Wed Apr 21 03:41:11 2021

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

    CPU time :                                   35614.73 sec.
    Max Memory :                                 2059 MB
    Average Memory :                             2058.44 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14325.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35708 sec.
    Turnaround time :                            310345 sec.

The output (if any) is above this job summary.

