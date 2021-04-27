
# Parameters

    Name :                      Diamonds2_teleport-1
    Main :                      teleport
    Level :                     Levels.Causal5
    Failed actions chance :     0.0
    Hours :                     24.0
    Batch :                     100
    Width :                     9
    Height :                    9
    Graphmode :                 GraphMode.UCB1
    Network1 :                  Networks.Teleporter
    K1 :                        5000000
    Learner1 :                  Learners.Qlearn
    Exploration1 :              Explorations.softmaxer
    Gamma1 :                    0.98
    Network2 :                  Networks.Mini
    K2 :                        1000000
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
    Softmax cap :               0.02
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
    Minutes used :              1435 minutes.
    Hours used :                23 hours.

# Profiling


      74076101219 function calls (73865474248 primitive calls) in 86112.63 seconds

##    Ordered by: cumulative time
   List reduced from 474 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 86112.630 86112.630 {built-in method builtins.exec}
                      1    1.552    1.552 86112.630 86112.630 <string>:1(<module>)
                      1  181.147  181.147 86111.078 86111.078 main.py:45(teleport)
                7522942   26.725    0.000 28148.469    0.004 agent.py:29(learn)
                7522942  666.539    0.000 24147.152    0.003 learner.py:42(Qlearn)
                3761471   17.169    0.000 21481.213    0.006 game.py:41(step)
                3761471   22.410    0.000 20513.266    0.005 layers.py:718(step)
                3761471  131.770    0.000 16912.057    0.004 agent.py:54(_learn)
                3761471 6901.680    0.002 13279.200    0.004 replaybuffer.py:28(teleporter_save_data)
                3761471  304.512    0.000 12054.282    0.003 layers.py:17(step)
              376147100  642.931    0.000 11709.583    0.000 layer.py:98(move)
                3761471  108.874    0.000 11195.384    0.003 agent.py:117(_learn)
        236954889/26328929  987.828    0.000 10932.247    0.000 module.py:715(_call_impl)
                7522942   48.203    0.000 10388.681    0.001 grad_mode.py:23(decorate_context)
                7522942  258.657    0.000 10248.960    0.001 adam.py:55(step)
               18805987   50.761    0.000 10239.782    0.001 network.py:27(forward)
                3761471 6771.947    0.002 10105.767    0.003 agent.py:88(interveen)
               18805987  265.497    0.000 10071.860    0.001 container.py:115(forward)
                7522942 1893.319    0.000 8851.171    0.001 functional.py:53(adam)
                3761472  548.531    0.000 8410.588    0.002 layers.py:684(update)
              376147100 1617.871    0.000 7697.937    0.000 layers.py:735(check)
                7521574  183.401    0.000 6693.603    0.001 agent.py:49(__call__)
                7522942   47.406    0.000 5496.981    0.001 tensor.py:181(backward)
                7522942   31.371    0.000 5449.575    0.001 __init__.py:68(backward)
                7522942 5207.516    0.001 5207.516    0.001 {method 'run_backward' of 'torch._C._EngineBase' objects}
              327165567 4989.168    0.000 4989.168    0.000 {built-in method clone}
                3761471 2935.055    0.001 4805.627    0.001 replaybuffer.py:22(sample_data)
                3761471 2409.758    0.001 4515.826    0.001 agent.py:67(modify)
               37611974   69.002    0.000 3641.485    0.000 conv.py:422(forward)
               37611974   74.619    0.000 3545.687    0.000 conv.py:414(_conv_forward)
               37611974 3457.462    0.000 3457.462    0.000 {built-in method conv2d}
               48895019  119.490    0.000 3270.498    0.000 linear.py:92(forward)
               48895019  200.919    0.000 3097.399    0.000 functional.py:1669(linear)
                5416976   58.890    0.000 2859.204    0.001 layers.py:740(restart)
              376147100  792.452    0.000 2744.015    0.000 layers.py:729(isFree)
                5416976   28.172    0.000 2373.949    0.000 level.py:8(__init__)
             1051549730  644.495    0.000 2324.841    0.000 {built-in method builtins.any}
               33853248 1262.523    0.000 2226.732    0.000 layer.py:167(NoRock_update)
               48895019 2221.674    0.000 2221.674    0.000 {built-in method addmm}
              473945400 1355.459    0.000 2125.617    0.000 tensor.py:933(grad)
                3761471   53.238    0.000 2111.170    0.001 agent.py:112(__call__)
                5416976   86.431    0.000 2097.168    0.000 levels.py:249(generate)
                7522942  190.527    0.000 2062.185    0.000 optimizer.py:167(zero_grad)
               11283045   84.973    0.000 1994.366    0.000 agent.py:59(modify_board)
               30090400 1962.733    0.000 1962.733    0.000 {built-in method cat}
             3372031858 1550.248    0.000 1951.563    0.000 layer.py:95(isFree)
             7344537354 1367.504    0.000 1945.081    0.000 enum.py:646(__hash__)
               35211989  341.825    0.000 1920.526    0.000 level.py:41(notUsed)
              135412956 1848.829    0.000 1848.829    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                3761471   68.251    0.000 1583.310    0.000 replaybuffer.py:18(stacker)
              135412956 1572.117    0.000 1572.117    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
               67701006   64.428    0.000 1521.742    0.000 activation.py:713(forward)
              338448612 1506.940    0.000 1506.940    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
               67701006   93.996    0.000 1457.314    0.000 functional.py:1292(leaky_relu)
               16130369 1355.012    0.000 1355.012    0.000 {built-in method tensor}
               67701006 1354.081    0.000 1354.081    0.000 {built-in method torch._C._nn.leaky_relu}
             3707302240 1067.178    0.000 1287.439    0.000 layers.py:700(<genexpr>)
               11283045 1245.804    0.000 1245.804    0.000 {built-in method torch._C._nn.one_hot}
              376147100  697.560    0.000 1123.179    0.000 layers.py:337(check)
              376147100  671.483    0.000 1094.311    0.000 layers.py:387(check)
               26332367  152.413    0.000 1083.511    0.000 tensor.py:21(wrapped)
              376147100  653.407    0.000 1069.243    0.000 layers.py:349(check)
              616878602  358.615    0.000 1053.346    0.000 overrides.py:1070(has_torch_function)
              376147100  645.728    0.000 1049.619    0.000 layers.py:375(check)
                7522942    9.202    0.000 1036.901    0.000 game.py:37(board)
               67706478 1015.552    0.000 1015.552    0.000 {method 'add' of 'torch._C._TensorBase' objects}
              402479567  160.931    0.000  992.040    0.000 {built-in method builtins.all}
                3761471  580.655    0.000  977.198    0.000 collector.py:46(collect)
               67706478  915.497    0.000  915.497    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               35211989   26.745    0.000  895.839    0.000 level.py:38(elementsIn)
             8690638584  867.429    0.000  867.429    0.000 layer.py:91(positions)
             1489283577  427.167    0.000  861.648    0.000 layers.py:690(<genexpr>)
               67706478  838.316    0.000  838.316    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               67706478  746.207    0.000  746.207    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                7521574  256.136    0.000  717.616    0.000 exploration.py:53(softmaxer)
               67706478  591.005    0.000  591.005    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
               35211989  284.014    0.000  580.382    0.000 level.py:39(<listcomp>)
             7344564825  577.582    0.000  577.582    0.000 {built-in method builtins.hash}
             1205173503  567.397    0.000  567.397    0.000 layer.py:146(elements)
              376147100  318.992    0.000  493.273    0.000 layers.py:364(check)
              376147100  312.936    0.000  486.189    0.000 layers.py:326(check)
        4701783573/4701783571  352.442    0.000  472.522    0.000 {built-in method builtins.len}
                7522942   13.827    0.000  466.148    0.000 loss.py:445(forward)
                7522942   45.770    0.000  452.320    0.000 functional.py:2637(mse_loss)
               18807355  452.025    0.000  452.025    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
               48895019  436.121    0.000  436.121    0.000 {method 't' of 'torch._C._TensorBase' objects}
              376147100  286.470    0.000  420.493    0.000 layers.py:23(check)
             1660717480  416.404    0.000  416.404    0.000 level.py:32(inverse)
               48752784   41.366    0.000  409.406    0.000 layer.py:69(restart)
               22568826  393.520    0.000  393.520    0.000 {built-in method sum}
             1308983838  311.059    0.000  387.868    0.000 overrides.py:1083(<genexpr>)
              571413479  248.233    0.000  342.270    0.000 layer.py:130(add)
             3372031858  330.362    0.000  330.362    0.000 layer.py:203(isBlocking)
             3797734327  314.992    0.000  314.992    0.000 {method 'random' of '_random.Random' objects}
                5417076  148.437    0.000  296.664    0.000 layers.py:36(reset)
              383935785  198.889    0.000  292.906    0.000 layer.py:126(remove)
               35211989  178.233    0.000  288.712    0.000 {built-in method _functools.reduce}
                7522942  285.400    0.000  285.400    0.000 {built-in method torch._C._nn.mse_loss}
               37611974   30.097    0.000  282.208    0.000 flatten.py:39(forward)
                3761471  101.653    0.000  280.378    0.000 random.py:315(sample)


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@hpc.dtu.dk>
Subject: Job 9550900: <Diamonds2_teleport_1> in cluster <dcc> Done

Job <Diamonds2_teleport_1> was submitted from host <n-62-30-4> by user <s183905> in cluster <dcc> at Tue Apr 20 16:21:48 2021
Job was executed on host(s) <n-62-20-14>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Apr 22 09:04:12 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Apr 22 09:04:12 2021
Terminated at Fri Apr 23 08:59:32 2021
Results reported at Fri Apr 23 08:59:32 2021

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
#BSUB -W 1440
# end of BSUB options
cd ..
module -s load python3
source ../project-env/bin/activate

python main.py $LSB_PROJECT_NAME


------------------------------------------------------------

Successfully completed.

Resource usage summary:

    CPU time :                                   85897.72 sec.
    Max Memory :                                 2680 MB
    Average Memory :                             2674.04 MB
    Total Requested Memory :                     16384.00 MB
    Delta Memory :                               13704.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   86119 sec.
    Turnaround time :                            232664 sec.

The output (if any) is above this job summary.

