
# Parameters

    Name :                      Rocks_9x9_META_attempt2-0
    Main :                      metateleport
    Level :                     Levels.Rocks
    Hours :                     11.0
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
    Layer keys :                False
    Layer door :                False
    Layer holder :              False
    Layer putter :              False
    Layer rock :                True
    Layer dirt :                True
    Layer diamond1 :            False
    Layer diamond2 :            False
    Layer diamond3 :            False
    Layer diamond4 :            False
    Layer reddoors :            False
    Layer redkeys :             False
    Layer bluedoors :           False
    Layer bluekeys :            False
    K :                         200000
    Epsilon cap :               0.1
    Softmax cap :               0.025
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.03
    Miss intervention cost :    -0.15
    Intervention cost :         -0.05
    Replay size :               100000
    Sample size :               50
    Minutes used :              655 minutes.
    Hours used :                10 hours.

# Profiling


      20419542067 function calls (20258469140 primitive calls) in 39315.57 seconds

##    Ordered by: cumulative time
   List reduced from 467 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 39315.567 39315.567 {built-in method builtins.exec}
                      1    5.044    5.044 39315.567 39315.567 <string>:1(<module>)
                      1  130.408  130.408 39310.523 39310.523 main.py:14(metateleport)
                5258139   19.592    0.000 12786.111    0.002 agent.py:27(learn)
                5258139  322.176    0.000 10325.827    0.002 learner.py:42(Qlearn)
                3505426  122.441    0.000 9558.698    0.003 agent.py:51(_learn)
                1752713    8.137    0.000 9139.879    0.005 game.py:27(step)
                1752713    9.875    0.000 8808.835    0.005 layers.py:475(step)
                1752713  160.376    0.000 6232.476    0.004 layers.py:18(step)
              175271300  462.551    0.000 6056.708    0.000 layer.py:76(move)
                3505426 4822.265    0.001 5954.158    0.002 replaybuffer.py:23(sample_data)
        180336207/19264979  724.164    0.000 5793.664    0.000 module.py:866(_call_impl)
               14006840   39.394    0.000 5411.916    0.000 network.py:24(forward)
               14006840  186.476    0.000 5280.569    0.000 container.py:117(forward)
                6995988  167.317    0.000 4387.478    0.001 agent.py:46(__call__)
                5258139   43.219    0.000 4028.563    0.001 optimizer.py:84(wrapper)
              175271300  400.589    0.000 4028.319    0.000 layers.py:492(check)
                5258139   22.438    0.000 3834.683    0.001 grad_mode.py:24(decorate_context)
                3505426 1589.268    0.000 3764.768    0.001 agent.py:81(interveen)
                5258139  150.467    0.000 3763.668    0.001 adam.py:55(step)
                3505426 2123.826    0.001 3747.667    0.001 replaybuffer.py:27(teleporter_save_data)
                5258139  795.397    0.000 3434.212    0.001 _functional.py:53(adam)
                1752713   53.431    0.000 3196.868    0.002 agent.py:146(_learn)
              175271300 2694.186    0.000 2924.901    0.000 layers.py:76(check)
                5258139   20.758    0.000 2658.234    0.001 tensor.py:195(backward)
                5258139   20.288    0.000 2636.722    0.001 __init__.py:68(backward)
                1752714  195.733    0.000 2552.914    0.001 layers.py:446(update)
                5258139 2516.251    0.000 2516.251    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                1752713 1552.265    0.001 2398.383    0.001 agent.py:101(metamodify)
               28013680   63.820    0.000 1926.428    0.000 conv.py:398(forward)
               28013680   35.794    0.000 1833.613    0.000 conv.py:390(_conv_forward)
               28013680 1797.820    0.000 1797.820    0.000 {built-in method conv2d}
               38515094   80.494    0.000 1493.846    0.000 linear.py:93(forward)
              148832546 1389.860    0.000 1389.860    0.000 {built-in method clone}
               38515094   32.319    0.000 1374.343    0.000 functional.py:1737(linear)
               38515094 1334.266    0.000 1334.266    0.000 {built-in method torch._C._nn.linear}
              175271300  235.893    0.000 1331.939    0.000 layers.py:486(isFree)
               10501414   90.052    0.000 1320.186    0.000 agent.py:55(modify_board)
              928470104  964.329    0.000 1096.046    0.000 layer.py:73(isFree)
               31533970 1084.881    0.000 1084.881    0.000 {built-in method cat}
               10516284  658.960    0.000 1027.944    0.000 layer.py:121(update)
                3505426   65.008    0.000  885.415    0.000 replaybuffer.py:19(stacker)
               10501414  842.538    0.000  842.538    0.000 {built-in method torch._C._nn.one_hot}
               52521934   43.405    0.000  795.526    0.000 activation.py:713(forward)
                2484654   22.930    0.000  785.365    0.000 layers.py:496(restart)
               52521934   43.411    0.000  752.121    0.000 functional.py:1364(leaky_relu)
                1752713   26.491    0.000  704.103    0.000 agent.py:141(__call__)
               52521934  699.759    0.000  699.759    0.000 {built-in method torch._C._nn.leaky_relu}
               98151928  660.725    0.000  660.725    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                5258139  107.266    0.000  601.748    0.000 optimizer.py:189(zero_grad)
               98151928  596.385    0.000  596.385    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9029414  594.845    0.000  594.845    0.000 {built-in method tensor}
                2484654   11.217    0.000  513.890    0.000 level.py:8(__init__)
                5258139    5.868    0.000  502.584    0.000 game.py:23(board)
              175271400   57.218    0.000  473.621    0.000 {built-in method builtins.all}
                2484654   68.083    0.000  454.233    0.000 levels.py:95(generate)
              525883060  125.935    0.000  437.067    0.000 layers.py:452(<genexpr>)
                6995988  162.137    0.000  433.735    0.000 exploration.py:53(softmaxer)
              175271300  320.033    0.000  422.004    0.000 layers.py:63(check)
               49075964  396.458    0.000  396.458    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1752713  210.857    0.000  356.055    0.000 collector.py:54(collect)
               49075964  343.286    0.000  343.286    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
              157581247  321.954    0.000  321.954    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               49075964  316.380    0.000  316.380    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
             1137254151  220.790    0.000  314.788    0.000 enum.py:646(__hash__)
                5990080  118.300    0.000  314.043    0.000 random.py:315(sample)
               49075964  313.528    0.000  313.528    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              175271400  201.768    0.000  296.492    0.000 layers.py:110(isDone)
              343531832  228.930    0.000  282.641    0.000 tensor.py:906(grad)
                4969308   35.972    0.000  272.012    0.000 level.py:41(notUsed)
              774090477  252.783    0.000  252.783    0.000 layer.py:116(elements)
               14907924   30.611    0.000  243.310    0.000 layer.py:50(restart)
               49075964  237.936    0.000  237.936    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              175271300  155.229    0.000  237.353    0.000 layers.py:47(check)
             2555776773  229.421    0.000  229.421    0.000 layer.py:69(positions)
                5258139    6.653    0.000  221.277    0.000 loss.py:527(forward)
                5258139   19.589    0.000  214.625    0.000 functional.py:2898(mse_loss)
              376782405  146.693    0.000  198.539    0.000 layer.py:100(add)
        1602673773/1602673770  140.605    0.000  181.479    0.000 {built-in method builtins.len}
              194247005  101.702    0.000  175.841    0.000 layer.py:96(remove)
               15774417  166.401    0.000  166.401    0.000 {built-in method sum}
                2484754   63.989    0.000  140.916    0.000 layers.py:33(reset)
              136655970  140.432    0.000  140.432    0.000 level.py:32(inverse)
              237432116   95.694    0.000  139.553    0.000 random.py:250(_randbelow_with_getrandbits)
                6995988  136.729    0.000  136.729    0.000 {built-in method multinomial}
                5258139  132.210    0.000  132.210    0.000 {built-in method torch._C._nn.mse_loss}
               28013680   19.791    0.000  131.306    0.000 flatten.py:39(forward)
                8763565   12.275    0.000  127.857    0.000 tensor.py:525(__rsub__)
                5259013  121.760    0.000  121.760    0.000 {built-in method max}
                8763565  113.403    0.000  113.403    0.000 {built-in method rsub}
               28013680  111.515    0.000  111.515    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
                3505428  101.774    0.000  101.774    0.000 {built-in method nonzero}
             1320260175   99.650    0.000   99.650    0.000 {method 'append' of 'list' objects}
              183843031   98.301    0.000   98.301    0.000 {built-in method torch._C._get_tracing_state}
              147077797   96.312    0.000   96.319    0.000 module.py:934(__getattr__)
                5258139   20.009    0.000   95.890    0.000 __init__.py:28(_make_grads)
                5258139   94.468    0.000   94.468    0.000 {built-in method gather}
             1137274458   94.002    0.000   94.002    0.000 {built-in method builtins.hash}
               10516278   21.775    0.000   93.395    0.000 profiler.py:615(__enter__)
              928470104   90.851    0.000   90.851    0.000 layer.py:177(isBlocking)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-11-15>
Subject: Job 9455324: <Rocks_9x9_META_attempt2_0> in cluster <dcc> Done

Job <Rocks_9x9_META_attempt2_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Wed Mar 24 02:22:06 2021
Job was executed on host(s) <n-62-11-15>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Wed Mar 24 02:22:07 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Wed Mar 24 02:22:07 2021
Terminated at Wed Mar 24 13:17:41 2021
Results reported at Wed Mar 24 13:17:41 2021

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

    CPU time :                                   39209.07 sec.
    Max Memory :                                 6946 MB
    Average Memory :                             5246.76 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               1246.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   39405 sec.
    Turnaround time :                            39335 sec.

The output (if any) is above this job summary.

