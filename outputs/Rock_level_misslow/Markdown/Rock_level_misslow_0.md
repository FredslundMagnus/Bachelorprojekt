
# Parameters

    Name :                      Rock_level_misslow-0
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
    Softmax cap :               0.02
    Gamma :                     0.98
    Update :                    10000
    Reset chance :              0.002
    Modified done chance :      0.05
    Miss intervention cost :    -0.1
    Intervention cost :         -0.05
    Replay size :               50000
    Sample size :               50
    Minutes used :              715 minutes.
    Hours used :                11 hours.

# Profiling


      45413901962 function calls (45264532943 primitive calls) in 42912.84 seconds

##    Ordered by: cumulative time
   List reduced from 470 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 42912.836 42912.836 {built-in method builtins.exec}
                      1    0.930    0.930 42912.836 42912.836 <string>:1(<module>)
                      1  109.748  109.748 42911.906 42911.906 main.py:13(teleport)
                2667336    9.304    0.000 17706.180    0.007 game.py:27(step)
                2667336   12.380    0.000 17137.614    0.006 layers.py:373(step)
                5334672   17.118    0.000 11294.512    0.002 agent.py:26(learn)
                2667336  218.236    0.000 11180.143    0.004 layers.py:18(step)
              266733600  544.647    0.000 10939.238    0.000 layer.py:74(move)
                5334672  299.308    0.000 9510.329    0.002 learner.py:42(Qlearn)
              266733600  793.073    0.000 8134.613    0.000 layers.py:390(check)
                2667336   85.343    0.000 6733.560    0.003 agent.py:50(_learn)
                2667337  271.485    0.000 5928.270    0.002 layers.py:344(update)
        168039126/18671118  612.052    0.000 5051.885    0.000 module.py:866(_call_impl)
                2667336 2954.126    0.001 5035.252    0.002 replaybuffer.py:27(teleporter_save_data)
               13336446   35.938    0.000 4687.046    0.000 network.py:24(forward)
               13336446  151.291    0.000 4570.853    0.000 container.py:117(forward)
                2667336   73.624    0.000 4533.521    0.002 agent.py:101(_learn)
              266733600 3698.693    0.000 4384.716    0.000 layers.py:76(check)
                5334672   43.136    0.000 3670.498    0.001 optimizer.py:84(wrapper)
                2667336 2070.851    0.001 3617.671    0.001 agent.py:77(interveen)
                5334672   21.172    0.000 3480.358    0.001 grad_mode.py:24(decorate_context)
                5334672  138.423    0.000 3410.782    0.001 adam.py:55(step)
                5334438  113.611    0.000 3130.931    0.001 agent.py:45(__call__)
                5334672  710.483    0.000 3106.775    0.001 _functional.py:53(adam)
                9310724   78.006    0.000 2508.701    0.000 layers.py:394(restart)
                5334672   20.424    0.000 2459.617    0.000 tensor.py:195(backward)
                5334672   19.661    0.000 2438.528    0.000 __init__.py:68(backward)
               24006033 1608.924    0.000 2361.977    0.000 layer.py:119(update)
                5334672 2320.026    0.000 2320.026    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
              266733600  450.574    0.000 1971.332    0.000 layers.py:384(isFree)
                2667336  970.754    0.000 1792.280    0.001 replaybuffer.py:23(sample_data)
               26672892   56.197    0.000 1720.926    0.000 conv.py:398(forward)
              211215084 1716.974    0.000 1716.974    0.000 {built-in method clone}
                2667336 1034.707    0.000 1682.567    0.001 agent.py:59(modify)
               26672892   34.585    0.000 1639.234    0.000 conv.py:390(_conv_forward)
               26672892 1604.649    0.000 1604.649    0.000 {built-in method conv2d}
                9310724   35.147    0.000 1579.986    0.000 level.py:8(__init__)
             2236860058 1234.969    0.000 1520.758    0.000 layer.py:71(isFree)
                9310724  226.913    0.000 1413.980    0.000 levels.py:95(generate)
               34674666   68.050    0.000 1276.975    0.000 linear.py:93(forward)
               34674666   27.353    0.000 1176.967    0.000 functional.py:1737(linear)
               34674666 1143.307    0.000 1143.307    0.000 {built-in method torch._C._nn.linear}
             4658651272  762.387    0.000 1103.956    0.000 enum.py:646(__hash__)
                2667336   32.671    0.000  974.069    0.000 agent.py:96(__call__)
                8001774   46.016    0.000  970.199    0.000 agent.py:54(modify_board)
               83796516  115.159    0.000  825.652    0.000 layer.py:48(restart)
               11027148  814.288    0.000  814.288    0.000 {built-in method tensor}
               18621448  109.570    0.000  795.828    0.000 level.py:41(notUsed)
               24005790  793.063    0.000  793.063    0.000 {built-in method cat}
              266733700   76.881    0.000  684.497    0.000 {built-in method builtins.all}
              266733600  417.808    0.000  681.066    0.000 layers.py:216(check)
               48011112   36.400    0.000  678.851    0.000 activation.py:713(forward)
                5334672    5.160    0.000  678.655    0.000 game.py:23(board)
              266733600  404.356    0.000  665.799    0.000 layers.py:230(check)
                2667336   45.090    0.000  645.561    0.000 replaybuffer.py:19(stacker)
               48011112   38.217    0.000  642.450    0.000 functional.py:1364(leaky_relu)
                8001774  642.311    0.000  642.311    0.000 {built-in method torch._C._nn.one_hot}
              266733600  393.170    0.000  639.460    0.000 layers.py:244(check)
              849609585  199.679    0.000  637.483    0.000 layers.py:350(<genexpr>)
               48011112  596.825    0.000  596.825    0.000 {built-in method torch._C._nn.leaky_relu}
               96024096  594.940    0.000  594.940    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
              266733600  378.056    0.000  576.627    0.000 layers.py:63(check)
             1224007502  423.838    0.000  571.441    0.000 layer.py:98(add)
                5334672   96.720    0.000  550.130    0.000 optimizer.py:189(zero_grad)
               96024096  539.686    0.000  539.686    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
             6244184645  535.133    0.000  535.133    0.000 layer.py:67(positions)
             2483618860  518.269    0.000  518.269    0.000 layer.py:114(elements)
              570327857  256.666    0.000  505.242    0.000 layer.py:94(remove)
                9310824  223.397    0.000  448.203    0.000 layers.py:33(reset)
               11978060  151.982    0.000  423.855    0.000 random.py:315(sample)
              512089820  417.173    0.000  417.173    0.000 level.py:32(inverse)
              219216858  414.247    0.000  414.247    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
              266733700  273.283    0.000  410.205    0.000 layers.py:110(isDone)
                2667336  215.145    0.000  367.709    0.000 collector.py:54(collect)
               48012048  358.324    0.000  358.324    0.000 {method 'add' of 'torch._C._TensorBase' objects}
             4658670823  341.573    0.000  341.573    0.000 {built-in method builtins.hash}
              266733600  212.486    0.000  327.425    0.000 layers.py:203(check)
                5334438  118.047    0.000  315.528    0.000 exploration.py:53(softmaxer)
               48012048  313.631    0.000  313.631    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               48012048  290.549    0.000  290.549    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
               48012048  287.190    0.000  287.190    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
              336084390  209.706    0.000  259.844    0.000 tensor.py:906(grad)
              266733600  106.485    0.000  245.324    0.000 layers.py:99(<listcomp>)
             3720019194  241.583    0.000  241.583    0.000 {method 'append' of 'list' objects}
             2236860058  222.786    0.000  222.786    0.000 layer.py:175(isBlocking)
               48012048  216.829    0.000  216.829    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
        2716407280/2716407278  180.749    0.000  216.097    0.000 {built-in method builtins.len}
                5334672    7.094    0.000  214.238    0.000 loss.py:527(forward)
                5334672   18.973    0.000  207.144    0.000 functional.py:2898(mse_loss)
               18621448   14.572    0.000  206.812    0.000 level.py:38(elementsIn)
              366200646  142.604    0.000  206.457    0.000 random.py:250(_randbelow_with_getrandbits)
              570327857  204.967    0.000  204.967    0.000 {method 'remove' of 'list' objects}
               16004016  160.707    0.000  160.707    0.000 {built-in method sum}
                5334672  125.491    0.000  125.491    0.000 {built-in method torch._C._nn.mse_loss}
               18621448   60.317    0.000  118.530    0.000 level.py:39(<listcomp>)
               26672892   18.553    0.000  117.830    0.000 flatten.py:39(forward)
                5335471  116.563    0.000  116.563    0.000 {built-in method max}
                8002008   10.022    0.000  109.871    0.000 tensor.py:525(__rsub__)
                9310724   49.921    0.000  106.496    0.000 level.py:16(<dictcomp>)
               26672892   99.277    0.000   99.277    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-4>
Subject: Job 9441990: <Rock_level_misslow_0> in cluster <dcc> Done

Job <Rock_level_misslow_0> was submitted from host <gbarlogin1> by user <s183914> in cluster <dcc> at Sat Mar 20 01:13:12 2021
Job was executed on host(s) <n-62-20-4>, in queue <gpuv100>, as user <s183914> in cluster <dcc> at Sat Mar 20 13:08:40 2021
</zhome/ea/9/137501> was used as the home directory.
</zhome/ea/9/137501/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Sat Mar 20 13:08:40 2021
Terminated at Sun Mar 21 01:04:02 2021
Results reported at Sun Mar 21 01:04:02 2021

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

    CPU time :                                   42804.15 sec.
    Max Memory :                                 6044 MB
    Average Memory :                             4350.99 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               2148.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   42943 sec.
    Turnaround time :                            85850 sec.

The output (if any) is above this job summary.

