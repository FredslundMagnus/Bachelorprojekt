
# Parameters

    Name :                      Diamonds4_0.0_UCB1-1
    Main :                      graphTrain
    Level :                     Levels.Causal7
    Failed actions chance :     0.0
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


      19128868981 function calls (18706673542 primitive calls) in 35709.45 seconds

##    Ordered by: cumulative time
   List reduced from 464 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35709.447 35709.447 {built-in method builtins.exec}
                      1    0.001    0.001 35709.447 35709.447 <string>:1(<module>)
                      1  231.623  231.623 35709.445 35709.445 allGraphsTrain.py:10(graphTrain)
                 691183 5279.377    0.008 13173.944    0.019 allGraphs.py:146(transformNot)
              691188928 9188.926    0.000 9188.926    0.000 {method 'item' of 'torch._C._TensorBase' objects}
                 691183   17.289    0.000 8368.372    0.012 allGraphsTrain.py:29(<listcomp>)
               69809584 1851.949    0.000 8351.128    0.000 allGraphs.py:110(states)
              622065100 5962.025    0.000 5962.025    0.000 {method 'sum' of 'torch._C._TensorBase' objects}
                 691183    3.437    0.000 4067.083    0.006 game.py:41(step)
                 691183    4.994    0.000 3911.143    0.006 layers.py:718(step)
                 691183  729.563    0.001 2854.325    0.004 allGraphsTrain.py:35(<listcomp>)
               10339857   15.573    0.000 2124.762    0.000 allGraphs.py:158(getInterventions)
                 691183  132.413    0.000 2085.792    0.003 allGraphsTrain.py:37(<listcomp>)
                 691184  110.179    0.000 2042.592    0.003 layers.py:684(update)
                 691183   65.664    0.000 1857.698    0.003 layers.py:17(step)
               69118300  118.592    0.000 1785.507    0.000 layer.py:98(move)
                 691183    3.293    0.000 1705.715    0.002 agent.py:29(learn)
                 691183   18.159    0.000 1700.227    0.002 agent.py:117(_learn)
                 691183   52.402    0.000 1682.069    0.002 learner.py:42(Qlearn)
               16731819 1440.287    0.000 1440.287    0.000 {built-in method tensor}
               13795773    8.829    0.000 1335.332    0.000 game.py:37(board)
               73265398  176.340    0.000 1236.401    0.000 tensor.py:21(wrapped)
                 691183   54.690    0.000 1160.223    0.002 allGraphsTrain.py:44(<listcomp>)
                2792726   23.756    0.000 1100.695    0.000 layers.py:740(restart)
               10339857   10.592    0.000 1083.217    0.000 allGraphs.py:133(UCB1)
               69118300  218.273    0.000 1045.973    0.000 layers.py:735(check)
        92929708/10339857   64.545    0.000 1031.614    0.000 {built-in method builtins.min}
               10339857   46.167    0.000 1025.972    0.000 allGraphs.py:153(format)
               26159852   12.573    0.000 1014.437    0.000 allGraphs.py:134(<lambda>)
        175519559/26159852  272.591    0.000 1001.864    0.000 allGraphs.py:68(expected_moves_UCB1)
                2792726   12.161    0.000  878.286    0.000 level.py:8(__init__)
               72574215  842.185    0.000  842.185    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
        231949558/55527720   71.564    0.000  819.736    0.000 allGraphs.py:72(<genexpr>)
                 691183  420.481    0.001  784.957    0.001 agent.py:67(modify)
               69118300  781.407    0.000  781.407    0.000 {method 'argmax' of 'torch._C._TensorBase' objects}
                2792726   31.789    0.000  756.296    0.000 levels.py:441(generate)
        15897209/2073549   78.930    0.000  726.193    0.000 module.py:715(_call_impl)
               13403135  126.729    0.000  690.856    0.000 level.py:41(notUsed)
             2591982933  455.626    0.000  659.353    0.000 enum.py:646(__hash__)
                1382366    4.969    0.000  657.475    0.000 network.py:27(forward)
                1382366   18.450    0.000  640.864    0.000 container.py:115(forward)
                 691183    5.833    0.000  628.456    0.001 grad_mode.py:23(decorate_context)
                 691183   25.062    0.000  611.367    0.001 adam.py:55(step)
               69118300  105.988    0.000  500.369    0.000 layers.py:729(isFree)
                 691183  111.180    0.000  499.566    0.001 functional.py:53(adam)
                 691183    4.788    0.000  421.113    0.001 tensor.py:181(backward)
                 691183    3.985    0.000  416.325    0.001 __init__.py:68(backward)
                 691183   14.684    0.000  409.427    0.001 agent.py:112(__call__)
              481336269  333.085    0.000  394.381    0.000 layer.py:95(isFree)
                 691183  392.588    0.001  392.588    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                4838288  219.032    0.000  374.355    0.000 layer.py:167(NoRock_update)
              190738749  105.749    0.000  365.180    0.000 {built-in method builtins.any}
               13403135   10.254    0.000  322.731    0.000 level.py:38(elementsIn)
                2073549   10.019    0.000  284.961    0.000 tensor.py:576(__iter__)
               92929708   59.382    0.000  280.831    0.000 allGraphs.py:83(layers_not_in)
              175519559  171.353    0.000  272.073    0.000 allGraphs.py:60(UCB1)
                2073549  268.096    0.000  268.096    0.000 {method 'unbind' of 'torch._C._TensorBase' objects}
                2764732    6.078    0.000  262.034    0.000 conv.py:422(forward)
                2764732    8.923    0.000  253.408    0.000 conv.py:414(_conv_forward)
              142383798   49.590    0.000  248.350    0.000 {built-in method builtins.all}
               71883032  247.706    0.000  247.706    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                2764732  243.396    0.000  243.396    0.000 {built-in method conv2d}
               92929708  108.638    0.000  221.449    0.000 allGraphs.py:84(<listcomp>)
               13403135  102.046    0.000  209.163    0.000 level.py:39(<listcomp>)
              120265976   63.729    0.000  204.443    0.000 overrides.py:1070(has_torch_function)
               69118300  129.496    0.000  204.359    0.000 layers.py:617(check)
             2591985234  203.727    0.000  203.727    0.000 {built-in method builtins.hash}
               69118300  124.767    0.000  202.709    0.000 layers.py:632(check)
               69118300  118.372    0.000  192.265    0.000 layers.py:602(check)
               19549082   16.516    0.000  191.856    0.000 layer.py:69(restart)
                2764732    7.995    0.000  189.402    0.000 linear.py:92(forward)
              237732330   64.325    0.000  179.629    0.000 layers.py:690(<genexpr>)
              530605392  145.011    0.000  178.742    0.000 layers.py:700(<genexpr>)
                2764732   13.328    0.000  177.589    0.000 functional.py:1669(linear)
               38706302   92.021    0.000  152.495    0.000 tensor.py:933(grad)
                2792826   73.126    0.000  146.034    0.000 layers.py:36(reset)
              643521891  144.009    0.000  144.009    0.000 level.py:32(inverse)
             1404384848  136.430    0.000  136.430    0.000 layer.py:91(positions)
                 691183    7.720    0.000  135.456    0.000 agent.py:59(modify_board)
                 691183   13.376    0.000  132.628    0.000 optimizer.py:167(zero_grad)
                2764732  128.783    0.000  128.783    0.000 {built-in method addmm}
                 691183   63.117    0.000  109.513    0.000 collector.py:46(collect)
              583052489  107.654    0.000  107.654    0.000 enum.py:352(<genexpr>)
               13403135   64.611    0.000  103.314    0.000 {built-in method _functools.reduce}
                2792726   54.674    0.000  102.098    0.000 level.py:16(<dictcomp>)
               69118300   66.301    0.000  100.514    0.000 layers.py:588(check)
               11058928   99.750    0.000   99.750    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              345697149   99.218    0.000   99.218    0.000 layer.py:146(elements)
              169400036   71.317    0.000   98.832    0.000 layer.py:130(add)
                 691183   88.736    0.000   88.736    0.000 {built-in method torch._C._nn.one_hot}
                 691183   58.808    0.000   83.692    0.000 allGraphsTrain.py:43(<listcomp>)
               11058928   81.750    0.000   81.750    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                4147098    5.345    0.000   81.028    0.000 activation.py:713(forward)
              316562082   67.593    0.000   80.123    0.000 overrides.py:1083(<genexpr>)
                 691183   20.057    0.000   75.692    0.000 allGraphs.py:137(transform)
                4147098    8.982    0.000   75.683    0.000 functional.py:1292(leaky_relu)
               69118300   50.517    0.000   75.295    0.000 layers.py:23(check)
                4147098   66.002    0.000   66.002    0.000 {built-in method torch._C._nn.leaky_relu}
               34346259   43.077    0.000   63.011    0.000 layers.py:113(isDone)
                2073549   61.993    0.000   61.993    0.000 {method 'tolist' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9532031: <Diamonds4_0.0_UCB1_1> in cluster <dcc> Done

Job <Diamonds4_0.0_UCB1_1> was submitted from host <n-62-30-7> by user <s183905> in cluster <dcc> at Sat Apr 17 13:28:44 2021
Job was executed on host(s) <n-62-20-10>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Apr 19 20:05:18 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Apr 19 20:05:18 2021
Terminated at Tue Apr 20 06:00:34 2021
Results reported at Tue Apr 20 06:00:34 2021

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

    CPU time :                                   35619.82 sec.
    Max Memory :                                 2064 MB
    Average Memory :                             2060.80 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               14320.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35718 sec.
    Turnaround time :                            232310 sec.

The output (if any) is above this job summary.

