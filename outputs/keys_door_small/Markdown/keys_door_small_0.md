
# Parameters

    Name :                      keys_door_small-0
    Main :                      teleport
    Hours :                     10.0
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
    Layer keys :                True
    Layer door :                True
    Layer holder :              False
    Layer putter :              False
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
    Minutes used :              595 minutes.
    Hours used :                9 hours.

# Profiling


      20456531615 function calls (20339853624 primitive calls) in 35659.08 seconds

##    Ordered by: cumulative time
   List reduced from 451 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 35716.700 35716.700 {built-in method builtins.exec}
                      1    0.704    0.704 35716.700 35716.700 <string>:1(<module>)
                      1   90.882   90.882 35715.996 35715.996 main.py:10(teleport)
                4167248   15.794    0.000 14619.225    0.004 agent.py:26(learn)
                4167248  347.681    0.000 12686.159    0.003 learner.py:42(Qlearn)
                2083624   67.506    0.000 8709.926    0.004 agent.py:50(_learn)
                2083624    8.402    0.000 6103.200    0.003 game.py:21(step)
                2083624   58.577    0.000 5885.244    0.003 agent.py:101(_learn)
        131261851/14584871  532.870    0.000 5754.785    0.000 module.py:715(_call_impl)
                2083624    9.673    0.000 5658.132    0.003 layers.py:212(step)
                4167248   27.942    0.000 5457.518    0.001 grad_mode.py:23(decorate_context)
               10417623   28.594    0.000 5388.788    0.001 network.py:24(forward)
                4167248  146.052    0.000 5382.664    0.001 adam.py:55(step)
               10417623  144.068    0.000 5295.739    0.001 container.py:115(forward)
                2083624 2602.657    0.001 5036.946    0.002 replaybuffer.py:27(teleporter_save_data)
                4167248  987.690    0.000 4639.647    0.001 functional.py:53(adam)
                2083624 2586.346    0.001 4343.762    0.002 agent.py:77(interveen)
                4166751   94.014    0.000 3515.949    0.001 agent.py:45(__call__)
                2083625  197.182    0.000 3134.014    0.002 layers.py:192(update)
                4167248   27.178    0.000 2855.269    0.001 tensor.py:181(backward)
                4167248   14.952    0.000 2828.091    0.001 __init__.py:68(backward)
                4167248 2702.486    0.001 2702.486    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
                2083624  148.116    0.000 2501.229    0.001 layers.py:17(step)
              208362400  212.326    0.000 2335.281    0.000 layer.py:66(move)
                2083624 1028.880    0.000 2045.175    0.001 agent.py:59(modify)
              132609873 1915.940    0.000 1915.940    0.000 {built-in method clone}
               20835246   37.671    0.000 1894.604    0.000 conv.py:422(forward)
               20835246   41.299    0.000 1843.822    0.000 conv.py:414(_conv_forward)
               20835246 1795.474    0.000 1795.474    0.000 {built-in method conv2d}
                3925321   28.042    0.000 1793.939    0.000 layers.py:233(restart)
               27085621   62.679    0.000 1723.616    0.000 linear.py:92(forward)
                2083624  682.901    0.000 1654.355    0.001 replaybuffer.py:23(sample_data)
               27085621  109.963    0.000 1634.691    0.000 functional.py:1669(linear)
                3925321    5.750    0.000 1472.819    0.000 levels.py:8(__init__)
                3925321   23.896    0.000 1467.069    0.000 level.py:8(__init__)
                5354997  281.718    0.000 1392.766    0.000 levels.py:11(generate)
               27085621 1172.925    0.000 1172.925    0.000 {built-in method addmm}
              262536678  706.534    0.000 1115.967    0.000 tensor.py:933(grad)
                4167248  113.116    0.000 1110.070    0.000 optimizer.py:167(zero_grad)
                2083624   27.771    0.000 1099.056    0.001 agent.py:96(__call__)
                6250375   44.991    0.000 1054.537    0.000 agent.py:54(modify_board)
               16668495 1025.207    0.000 1025.207    0.000 {built-in method cat}
              208362400  280.104    0.000  973.142    0.000 layers.py:229(check)
               75010464  962.031    0.000  962.031    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              208362400  196.127    0.000  961.520    0.000 layers.py:223(isFree)
                2083624   36.165    0.000  825.762    0.000 replaybuffer.py:19(stacker)
               75010464  822.766    0.000  822.766    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               37503244   34.420    0.000  802.060    0.000 activation.py:713(forward)
               37503244   53.316    0.000  767.639    0.000 functional.py:1292(leaky_relu)
              823659534  632.853    0.000  765.393    0.000 layer.py:63(isFree)
               37503244  709.329    0.000  709.329    0.000 {built-in method torch._C._nn.leaky_relu}
                5354997  356.673    0.000  683.654    0.000 levels.py:76(RFS)
                6250375  659.139    0.000  659.139    0.000 {built-in method torch._C._nn.one_hot}
              138860248  595.344    0.000  595.344    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                8823357  576.142    0.000  576.142    0.000 {built-in method tensor}
              216697902   73.908    0.000  554.708    0.000 {built-in method builtins.all}
               10418125  258.808    0.000  541.498    0.000 layer.py:90(update)
               37505232  540.152    0.000  540.152    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              335462607  183.367    0.000  538.519    0.000 overrides.py:1070(has_torch_function)
                2083624  307.357    0.000  514.883    0.000 collector.py:37(collect)
              635633835  153.353    0.000  499.837    0.000 layers.py:197(<genexpr>)
               37505232  481.412    0.000  481.412    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               37505232  441.668    0.000  441.668    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                4167248    4.606    0.000  415.458    0.000 game.py:17(board)
               37505232  391.981    0.000  391.981    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                4166751  134.781    0.000  377.665    0.000 exploration.py:53(softmaxer)
              208362400  230.008    0.000  362.526    0.000 layers.py:95(check)
              370882725  138.184    0.000  338.680    0.000 {built-in method builtins.any}
              208362500  217.893    0.000  329.070    0.000 layers.py:65(isDone)
               37505232  321.879    0.000  321.879    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
             1084043443  204.305    0.000  294.407    0.000 enum.py:646(__hash__)
               19626605   30.305    0.000  285.874    0.000 layer.py:40(restart)
              208362400  182.916    0.000  280.548    0.000 layers.py:77(check)
                8335402   40.419    0.000  264.988    0.000 tensor.py:21(wrapped)
                4167248    6.107    0.000  243.692    0.000 loss.py:445(forward)
                4167248   23.437    0.000  237.584    0.000 functional.py:2637(mse_loss)
               27085621  228.262    0.000  228.262    0.000 {method 't' of 'torch._C._TensorBase' objects}
               12793618   84.825    0.000  213.902    0.000 random.py:315(sample)
              747740178  213.854    0.000  213.854    0.000 layer.py:85(elements)
               12501744  204.320    0.000  204.320    0.000 {built-in method sum}
              706345821  160.267    0.000  197.838    0.000 overrides.py:1083(<genexpr>)
                3925421   98.632    0.000  195.031    0.000 layers.py:37(reset)
              365359978  138.381    0.000  187.163    0.000 layer.py:76(add)
             1940013215  170.862    0.000  170.862    0.000 layer.py:59(positions)
              321299820  109.808    0.000  164.595    0.000 levels.py:33(<genexpr>)
                6250872   31.436    0.000  157.521    0.000 tensor.py:506(__rsub__)
                4167248  150.265    0.000  150.265    0.000 {built-in method torch._C._nn.mse_loss}
               20835246   15.331    0.000  147.450    0.000 flatten.py:39(forward)
              212399011  101.340    0.000  145.500    0.000 random.py:250(_randbelow_with_getrandbits)
                6250872  139.646    0.000  139.646    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                4167872  133.958    0.000  133.958    0.000 {built-in method max}
               20835246  132.119    0.000  132.119    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
        425701099/425701097   66.731    0.000  131.057    0.000 {built-in method builtins.len}
              133346307  126.109    0.000  126.109    0.000 {built-in method torch._C._get_tracing_state}
                6250872  126.086    0.000  126.086    0.000 {built-in method rsub}
                4166751  120.377    0.000  120.377    0.000 {built-in method multinomial}
               85679952   41.282    0.000  113.719    0.000 random.py:285(choice)
                4167248  110.606    0.000  110.606    0.000 {built-in method gather}
                4167248   18.167    0.000  107.034    0.000 __init__.py:28(_make_grads)
              153328854   72.114    0.000  106.375    0.000 layer.py:72(remove)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 9395012: <keys_door_small_0> in cluster <dcc> Done

Job <keys_door_small_0> was submitted from host <n-62-27-20> by user <s183905> in cluster <dcc> at Mon Mar  8 13:46:24 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Mon Mar  8 13:46:26 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Mon Mar  8 13:46:26 2021
Terminated at Mon Mar  8 23:42:06 2021
Results reported at Mon Mar  8 23:42:06 2021

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

    CPU time :                                   35617.59 sec.
    Max Memory :                                 2387 MB
    Average Memory :                             2375.85 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5805.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   35740 sec.
    Turnaround time :                            35742 sec.

The output (if any) is above this job summary.

