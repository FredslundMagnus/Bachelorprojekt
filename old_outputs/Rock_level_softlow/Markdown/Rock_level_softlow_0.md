
# Parameters

    Name :                      Rock_level_softlow-0
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
    Epsilon cap :               0.1
    Softmax cap :               0.01
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


      36122897532 function calls (36004270021 primitive calls) in 42914.45 seconds

##    Ordered by: cumulative time
   List reduced from 472 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42914.446 42914.446 {built-in method builtins.exec}
                      1    0.959    0.959 42914.446 42914.446 <string>:1(<module>)
                      1   97.821   97.821 42913.487 42913.487 main.py:13(teleport)
                2118379    9.446    0.000 15630.254    0.007 game.py:27(step)
                2118379   11.607    0.000 15113.901    0.007 layers.py:373(step)
                4236758   16.358    0.000 12882.820    0.003 agent.py:26(learn)
                4236758  338.354    0.000 11069.337    0.003 learner.py:42(Qlearn)
                2118379  182.185    0.000 9850.456    0.005 layers.py:18(step)
              211837900  492.917    0.000 9649.052    0.000 layer.py:74(move)
                2118379   74.762    0.000 7670.599    0.004 agent.py:50(_learn)
              211837900  706.118    0.000 7215.213    0.000 layers.py:390(check)
                2118379 2911.647    0.001 5308.017    0.003 replaybuffer.py:27(teleporter_save_data)
        133454926/14828426  600.025    0.000 5285.885    0.000 module.py:866(_call_impl)
                2118380  240.772    0.000 5237.801    0.002 layers.py:344(update)
                2118379   65.531    0.000 5187.250    0.002 agent.py:101(_learn)
               10591668   33.382    0.000 4921.690    0.000 network.py:24(forward)
               10591668  156.122    0.000 4817.179    0.000 container.py:117(forward)
                4236758   38.497    0.000 4670.192    0.001 optimizer.py:84(wrapper)
                4236758   18.605    0.000 4488.992    0.001 grad_mode.py:24(decorate_context)
                4236758  130.241    0.000 4428.492    0.001 adam.py:55(step)
                4236758  920.047    0.000 4145.828    0.001 _functional.py:53(adam)
              211837900 3261.398    0.000 3858.559    0.000 layers.py:76(check)
                2118379 2216.261    0.001 3826.032    0.002 agent.py:77(interveen)
                4236531  103.866    0.000 3244.645    0.001 agent.py:45(__call__)
                4236758   19.382    0.000 2718.389    0.001 tensor.py:195(backward)
                4236758   17.502    0.000 2698.316    0.001 __init__.py:68(backward)
                4236758 2579.775    0.001 2579.775    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                7494031   70.037    0.000 2260.419    0.000 layers.py:394(restart)
               19065420 1383.584    0.000 2037.350    0.000 layer.py:119(update)
              150016226 1937.695    0.000 1937.695    0.000 {built-in method clone}
                2118379 1169.597    0.001 1854.103    0.001 agent.py:59(modify)
               21183336   51.402    0.000 1747.727    0.000 conv.py:398(forward)
              211837900  390.581    0.000 1689.326    0.000 layers.py:384(isFree)
               21183336   33.397    0.000 1675.155    0.000 conv.py:390(_conv_forward)
               21183336 1641.758    0.000 1641.758    0.000 {built-in method conv2d}
                2118379  766.838    0.000 1561.057    0.001 replaybuffer.py:23(sample_data)
                7494031   32.039    0.000 1428.102    0.000 level.py:8(__init__)
               27538246   63.957    0.000 1364.573    0.000 linear.py:93(forward)
             1780791737 1057.523    0.000 1298.745    0.000 layer.py:71(isFree)
                7494031  203.350    0.000 1275.804    0.000 levels.py:95(generate)
               27538246   25.312    0.000 1273.592    0.000 functional.py:1737(linear)
               27538246 1242.103    0.000 1242.103    0.000 {built-in method torch._C._nn.linear}
                2118379   31.014    0.000 1007.101    0.000 agent.py:96(__call__)
             3712904508  690.111    0.000 1002.171    0.000 enum.py:646(__hash__)
                6354910   44.953    0.000  978.228    0.000 agent.py:54(modify_board)
               76261644  837.817    0.000  837.817    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               19065184  808.840    0.000  808.840    0.000 {built-in method cat}
               38129914   32.318    0.000  774.493    0.000 activation.py:713(forward)
               76261644  745.334    0.000  745.334    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               38129914   34.415    0.000  742.176    0.000 functional.py:1364(leaky_relu)
               67446279  102.469    0.000  739.068    0.000 layer.py:48(restart)
               14988062   98.887    0.000  715.462    0.000 level.py:41(notUsed)
                8773305  714.078    0.000  714.078    0.000 {built-in method tensor}
               38129914  700.673    0.000  700.673    0.000 {built-in method torch._C._nn.leaky_relu}
                4236758  109.126    0.000  666.773    0.000 optimizer.py:189(zero_grad)
                2118379   40.357    0.000  639.386    0.000 replaybuffer.py:19(stacker)
                6354910  621.281    0.000  621.281    0.000 {built-in method torch._C._nn.one_hot}
              211837900  377.935    0.000  614.499    0.000 layers.py:216(check)
              211838000   68.821    0.000  609.466    0.000 {built-in method builtins.all}
              211837900  360.209    0.000  593.367    0.000 layers.py:230(check)
              211837900  359.259    0.000  589.625    0.000 layers.py:244(check)
                4236758    5.352    0.000  568.149    0.000 game.py:23(board)
              674554680  176.867    0.000  567.425    0.000 layers.py:350(<genexpr>)
              156371136  531.380    0.000  531.380    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              976605592  376.753    0.000  509.475    0.000 layer.py:98(add)
              211837900  324.076    0.000  500.607    0.000 layers.py:63(check)
             4962473622  481.886    0.000  481.886    0.000 layer.py:67(positions)
                2118379  280.023    0.000  465.316    0.000 collector.py:54(collect)
               38130822  460.117    0.000  460.117    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             1981118272  447.504    0.000  447.504    0.000 layer.py:114(elements)
              449272821  214.477    0.000  433.740    0.000 layer.py:94(remove)
                7494131  201.242    0.000  404.289    0.000 layers.py:33(reset)
               38130822  404.226    0.000  404.226    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               38130822  384.212    0.000  384.212    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               38130822  381.834    0.000  381.834    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                9612410  137.441    0.000  380.710    0.000 random.py:315(sample)
              412171705  372.678    0.000  372.678    0.000 level.py:32(inverse)
              211838000  241.416    0.000  365.129    0.000 layers.py:110(isDone)
                4236531  122.809    0.000  339.809    0.000 exploration.py:53(softmaxer)
             3712920099  312.063    0.000  312.063    0.000 {built-in method builtins.hash}
               38130822  296.348    0.000  296.348    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              211837900  189.108    0.000  292.782    0.000 layers.py:203(check)
              266915808  209.955    0.000  257.259    0.000 tensor.py:906(grad)
                4236758    5.988    0.000  222.535    0.000 loss.py:527(forward)
                4236758   17.295    0.000  216.547    0.000 functional.py:2898(mse_loss)
             2964626793  216.415    0.000  216.415    0.000 {method 'append' of 'list' objects}
              211837900   93.556    0.000  215.197    0.000 layers.py:99(<listcomp>)
        2160657683/2160657681  169.507    0.000  204.557    0.000 {built-in method builtins.len}
               12710274  196.116    0.000  196.116    0.000 {built-in method sum}
               14988062   13.410    0.000  186.592    0.000 level.py:38(elementsIn)
             1780791737  186.310    0.000  186.310    0.000 layer.py:175(isBlocking)
              293322042  129.173    0.000  185.497    0.000 random.py:250(_randbelow_with_getrandbits)
              449272821  180.635    0.000  180.635    0.000 {method 'remove' of 'list' objects}
                4236758  143.552    0.000  143.552    0.000 {built-in method torch._C._nn.mse_loss}
               21183336   16.224    0.000  134.587    0.000 flatten.py:39(forward)
                6355137   10.253    0.000  125.129    0.000 tensor.py:525(__rsub__)
                4237392  124.857    0.000  124.857    0.000 {built-in method max}
               21183336  118.364    0.000  118.364    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                6355137  113.073    0.000  113.073    0.000 {built-in method rsub}
                4236531  108.209    0.000  108.209    0.000 {built-in method multinomial}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9441986: <Rock_level_softlow_0> in cluster <dcc> Done

Job <Rock_level_softlow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:12 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 01:13:14 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 01:13:14 2021
Terminated at Sat Mar 20 13:08:37 2021
Results reported at Sat Mar 20 13:08:37 2021

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

    CPU time :                                   42802.02 sec.
    Max Memory :                                 5335 MB
    Average Memory :                             3993.64 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2857.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42925 sec.
    Turnaround time :                            42925 sec.

The output (if any) is above this job summary.

