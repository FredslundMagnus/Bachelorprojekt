
# Parameters

    Name :                      causal1_9x9-2
    Main :                      teleport
    Level :                     Levels.Causal1
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
    Layer gold :                True
    Layer keys :                True
    Layer door :                True
    Layer holder :              False
    Layer putter :              False
    Layer rock :                False
    Layer dirt :                False
    K :                         200000
    Epsilon cap :               0.2
    Softmax cap :               0.03
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


      28246332296 function calls (28113879841 primitive calls) in 42907.40 seconds

##    Ordered by: cumulative time
   List reduced from 459 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42907.403 42907.403 {built-in method builtins.exec}
                      1    0.927    0.927 42907.403 42907.403 <string>:1(<module>)
                      1   98.034   98.034 42906.476 42906.476 main.py:13(teleport)
                4730476   18.431    0.000 13181.996    0.003 agent.py:26(learn)
                4730476  313.961    0.000 11285.880    0.002 learner.py:42(Qlearn)
                2365238 5512.057    0.002 9845.199    0.004 replaybuffer.py:27(teleporter_save_data)
                2365238    8.261    0.000 8096.246    0.003 game.py:27(step)
                2365238   71.431    0.000 7881.063    0.003 agent.py:50(_learn)
                2365238   11.473    0.000 7624.092    0.003 layers.py:295(step)
                2365238 4196.683    0.002 5911.632    0.002 agent.py:77(interveen)
        149007953/16556509  578.371    0.000 5586.624    0.000 module.py:715(_call_impl)
                2365238   61.889    0.000 5273.266    0.002 agent.py:101(_learn)
               11826033   30.201    0.000 5218.134    0.000 network.py:24(forward)
               11826033  141.053    0.000 5116.408    0.000 container.py:115(forward)
                4730476   27.561    0.000 4542.835    0.001 grad_mode.py:23(decorate_context)
                4730476  149.895    0.000 4463.371    0.001 adam.py:55(step)
                2365239  255.727    0.000 3960.171    0.002 layers.py:266(update)
                4730476  819.256    0.000 3643.515    0.001 functional.py:53(adam)
                2365238  178.277    0.000 3637.560    0.002 layers.py:18(step)
              236523800  300.804    0.000 3436.394    0.000 layer.py:70(move)
                4730319   94.220    0.000 3423.692    0.001 agent.py:45(__call__)
              335888074 3392.234    0.000 3392.234    0.000 {built-in method clone}
                4730476   27.471    0.000 2597.251    0.001 tensor.py:181(backward)
                4730476   16.021    0.000 2569.780    0.001 __init__.py:68(backward)
                4730476 2444.647    0.001 2444.647    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2365238  872.897    0.000 2041.995    0.001 replaybuffer.py:23(sample_data)
                2365238 1022.105    0.000 1993.458    0.001 agent.py:59(modify)
               23652066   40.749    0.000 1878.333    0.000 conv.py:422(forward)
                7591651   55.846    0.000 1840.204    0.000 layers.py:316(restart)
               23652066   44.796    0.000 1821.908    0.000 conv.py:414(_conv_forward)
               23652066 1768.899    0.000 1768.899    0.000 {built-in method conv2d}
               30747623   72.124    0.000 1645.587    0.000 linear.py:92(forward)
               30747623  119.797    0.000 1542.457    0.000 functional.py:1669(linear)
              236523800  406.687    0.000 1539.019    0.000 layers.py:312(check)
              236523800  301.866    0.000 1297.855    0.000 layers.py:306(isFree)
                7591651   28.662    0.000 1231.210    0.000 level.py:8(__init__)
              298020042  727.620    0.000 1204.460    0.000 tensor.py:933(grad)
               21286985 1177.454    0.000 1177.454    0.000 {built-in method cat}
                7591651   87.627    0.000 1115.821    0.000 levels.py:122(generate)
               14191434  659.497    0.000 1108.903    0.000 layer.py:132(NoRock_update)
               30747623 1084.012    0.000 1084.012    0.000 {built-in method addmm}
                2365238   27.539    0.000 1076.148    0.000 agent.py:96(__call__)
                4730476   97.514    0.000 1039.948    0.000 optimizer.py:167(zero_grad)
                7095557   45.974    0.000 1036.339    0.000 agent.py:54(modify_board)
                2365238   42.089    0.000  997.188    0.000 replaybuffer.py:19(stacker)
             1364957169  779.644    0.000  995.989    0.000 layer.py:67(isFree)
              342983631  968.718    0.000  968.718    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               29607837  219.228    0.000  948.804    0.000 level.py:41(notUsed)
               85148568  727.206    0.000  727.206    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
               42573656   36.503    0.000  712.067    0.000 activation.py:713(forward)
               42573656   53.589    0.000  675.563    0.000 functional.py:1292(leaky_relu)
              245985854   81.480    0.000  668.641    0.000 {built-in method builtins.all}
                7095557  663.373    0.000  663.373    0.000 {built-in method torch._C._nn.one_hot}
               10006380  638.486    0.000  638.486    0.000 {built-in method tensor}
              380803520  209.867    0.000  628.489    0.000 overrides.py:1070(has_torch_function)
               42573656  616.198    0.000  616.198    0.000 {built-in method torch._C._nn.leaky_relu}
              742773882  190.662    0.000  611.080    0.000 layers.py:272(<genexpr>)
               85148568  610.612    0.000  610.612    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               45549906   43.148    0.000  535.597    0.000 layer.py:44(restart)
                4730476    5.214    0.000  487.419    0.000 game.py:23(board)
             1727703944  330.391    0.000  474.197    0.000 enum.py:646(__hash__)
              236523800  274.036    0.000  434.101    0.000 layers.py:142(check)
               42574284  429.111    0.000  429.111    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                2365238  247.434    0.000  426.061    0.000 collector.py:54(collect)
                7591751  206.284    0.000  416.834    0.000 layers.py:33(reset)
              421012096  164.041    0.000  397.494    0.000 {built-in method builtins.any}
              236523900  259.274    0.000  394.866    0.000 layers.py:110(isDone)
               42574284  392.702    0.000  392.702    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
             1365713613  376.952    0.000  376.952    0.000 level.py:32(inverse)
               42574284  351.032    0.000  351.032    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                4730319  129.287    0.000  350.049    0.000 exploration.py:53(softmaxer)
              236523800  206.637    0.000  321.714    0.000 layers.py:123(check)
              236523800  204.200    0.000  316.183    0.000 layers.py:47(check)
               42574284  301.744    0.000  301.744    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              520237734  215.079    0.000  298.585    0.000 layer.py:94(add)
             1061567370  281.544    0.000  281.544    0.000 layer.py:110(elements)
                9461954   43.205    0.000  264.314    0.000 tensor.py:21(wrapped)
               29607837   22.985    0.000  263.897    0.000 level.py:38(elementsIn)
             2674730612  258.186    0.000  258.186    0.000 layer.py:63(positions)
               42574284  239.082    0.000  239.082    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
                4730476    6.863    0.000  235.498    0.000 loss.py:445(forward)
              801816144  184.892    0.000  230.083    0.000 overrides.py:1083(<genexpr>)
                4730476   25.381    0.000  228.635    0.000 functional.py:2637(mse_loss)
        1809557132/1809557130  137.723    0.000  204.889    0.000 {built-in method builtins.len}
               30747623  197.334    0.000  197.334    0.000 {method 't' of 'torch._C._TensorBase' objects}
               14191428  171.827    0.000  171.827    0.000 {built-in method sum}
              235673874  114.169    0.000  169.511    0.000 layer.py:90(remove)
                2365238   60.944    0.000  167.509    0.000 random.py:315(sample)
               29607837   77.788    0.000  151.950    0.000 level.py:39(<listcomp>)
                7095714   34.905    0.000  147.297    0.000 tensor.py:506(__rsub__)
             1727721335  143.809    0.000  143.809    0.000 {built-in method builtins.hash}
                4730476  133.177    0.000  133.177    0.000 {built-in method torch._C._nn.mse_loss}
             1548030445  131.757    0.000  131.757    0.000 {method 'append' of 'list' objects}
               23652066   17.356    0.000  131.724    0.000 flatten.py:39(forward)
                7095714  129.568    0.000  129.568    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
             1135348663  129.160    0.000  129.160    0.000 layer.py:172(isBlocking)
                4731185  123.508    0.000  123.508    0.000 {built-in method max}
               42574374   52.655    0.000  119.985    0.000 tensor.py:596(__hash__)
               23652066  114.369    0.000  114.369    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                7095714  112.392    0.000  112.392    0.000 {built-in method rsub}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-13>
Subject: Job 9434610: <causal1_9x9_2> in cluster <dcc> Done

Job <causal1_9x9_2> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Thu Mar 18 20:16:27 2021
Job was executed on host(s) <n-62-20-13>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Mar 18 20:16:27 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 18 20:16:27 2021
Terminated at Fri Mar 19 08:11:42 2021
Results reported at Fri Mar 19 08:11:42 2021

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

    CPU time :                                   42802.61 sec.
    Max Memory :                                 2445 MB
    Average Memory :                             2443.16 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5747.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42959 sec.
    Turnaround time :                            42915 sec.

The output (if any) is above this job summary.

