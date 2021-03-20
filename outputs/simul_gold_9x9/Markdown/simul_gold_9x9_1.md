
# Parameters

    Name :                      simul_gold_9x9-1
    Main :                      simulation
    Level :                     Levels.Causal1
    Hours :                     4.0
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
    Minutes used :              235 minutes.
    Hours used :                3 hours.

# Profiling


      7475609951 function calls (7446869530 primitive calls) in 14085.57 seconds

##    Ordered by: cumulative time
   List reduced from 449 to 100 due to restriction <100>

                  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
                      1    0.000    0.000 14108.325 14108.325 {built-in method builtins.exec}
                      1    0.903    0.903 14108.325 14108.325 <string>:1(<module>)
                      1   33.628   33.628 14107.421 14107.421 main.py:47(simulation)
                 798318   19.913    0.000 3832.943    0.005 simulator.py:51(learn)
                 798318  202.856    0.000 3813.030    0.005 simulator.py:28(learn)
                 798318 1844.135    0.002 3506.944    0.004 replaybuffer.py:27(teleporter_save_data)
                 798318    3.367    0.000 2480.253    0.003 game.py:27(step)
                 798318    4.496    0.000 2314.563    0.003 layers.py:295(step)
                 798318 1498.613    0.002 2199.855    0.003 agent.py:77(interveen)
        33529252/4789900  140.617    0.000 1551.897    0.000 module.py:715(_call_impl)
                1596636    9.299    0.000 1477.156    0.001 grad_mode.py:23(decorate_context)
                 798318   84.154    0.000 1473.371    0.002 layers.py:266(update)
                1596636   40.934    0.000 1449.118    0.001 adam.py:55(step)
                3193264   37.305    0.000 1400.005    0.000 container.py:115(forward)
               88127640 1291.141    0.000 1291.141    0.000 {built-in method clone}
                1596636  263.224    0.000 1237.336    0.001 functional.py:53(adam)
                1999218   16.732    0.000  845.660    0.000 layers.py:316(restart)
                 798318   58.928    0.000  831.615    0.001 layers.py:18(step)
                 798318  425.395    0.001  827.223    0.001 agent.py:59(modify)
                1596628    4.025    0.000  823.194    0.001 network.py:24(forward)
                1596636    9.911    0.000  790.503    0.000 tensor.py:181(backward)
                1596636    5.405    0.000  780.592    0.000 __init__.py:68(backward)
               79831800   92.060    0.000  765.425    0.000 layer.py:70(move)
                1596636  731.696    0.000  731.696    0.000 {method 'run_backward' of 'torch._C._EngineBase' objects}
                 798318  279.874    0.000  714.853    0.001 replaybuffer.py:23(sample_data)
                 798310   21.601    0.000  689.758    0.001 agent.py:45(__call__)
                1999218    8.291    0.000  674.438    0.000 level.py:8(__init__)
                1999218  112.206    0.000  643.941    0.000 levels.py:9(generate)
                6386528   11.726    0.000  578.825    0.000 conv.py:422(forward)
                6386528   12.264    0.000  562.961    0.000 conv.py:414(_conv_forward)
                6386528  548.382    0.000  548.382    0.000 {built-in method conv2d}
                7983172  488.720    0.000  488.720    0.000 {built-in method cat}
                 798318   16.651    0.000  436.488    0.001 agent.py:96(__call__)
               90522586  394.719    0.000  394.719    0.000 {method 'unsqueeze' of 'torch._C._TensorBase' objects}
                 798318   14.446    0.000  377.851    0.000 replaybuffer.py:19(stacker)
                5588202   13.846    0.000  376.975    0.000 linear.py:92(forward)
                5588202   23.562    0.000  357.043    0.000 functional.py:1669(linear)
               79831800   71.310    0.000  349.000    0.000 layers.py:306(isFree)
               67058724  205.849    0.000  320.368    0.000 tensor.py:933(grad)
                 798318    2.530    0.000  311.027    0.000 simulator.py:25(RDforward)
                1596636   29.148    0.000  306.563    0.000 optimizer.py:167(zero_grad)
                 798318    2.972    0.000  300.126    0.000 simulator.py:22(boardforward)
                3193272  183.249    0.000  295.360    0.000 layer.py:132(NoRock_update)
              293940426  234.561    0.000  277.690    0.000 layer.py:67(isFree)
                1596628   11.506    0.000  275.455    0.000 agent.py:54(modify_board)
                1999218  140.646    0.000  268.712    0.000 levels.py:75(RFS)
                2394946  260.261    0.000  260.261    0.000 {built-in method torch._C._nn.one_hot}
               19159632  259.495    0.000  259.495    0.000 {method 'mul_' of 'torch._C._TensorBase' objects}
                5588202  257.925    0.000  257.925    0.000 {built-in method addmm}
               79831800   87.325    0.000  232.873    0.000 layers.py:312(check)
               84621866   27.650    0.000  221.888    0.000 {built-in method builtins.all}
               19159632  218.022    0.000  218.022    0.000 {method 'add_' of 'torch._C._TensorBase' objects}
                9579784    9.315    0.000  210.198    0.000 activation.py:713(forward)
                3353109  205.474    0.000  205.474    0.000 {built-in method tensor}
                9579784   13.408    0.000  200.883    0.000 functional.py:1292(leaky_relu)
              243371570   60.771    0.000  200.529    0.000 layers.py:272(<genexpr>)
                9579784  186.169    0.000  186.169    0.000 {built-in method torch._C._nn.leaky_relu}
                4790066   27.716    0.000  165.397    0.000 tensor.py:21(wrapped)
               87016807   51.959    0.000  153.002    0.000 overrides.py:1070(has_torch_function)
                7996872   14.700    0.000  151.269    0.000 layer.py:44(restart)
                9579816  144.098    0.000  144.098    0.000 {method 'add' of 'torch._C._TensorBase' objects}
                1596636    1.768    0.000  144.018    0.000 game.py:23(board)
               79831800   86.681    0.000  131.930    0.000 layers.py:110(isDone)
                9579816  126.205    0.000  126.205    0.000 {method 'sqrt' of 'torch._C._TensorBase' objects}
               79831800   80.150    0.000  125.647    0.000 layers.py:47(check)
                9579816  117.637    0.000  117.637    0.000 {method 'addcdiv_' of 'torch._C._TensorBase' objects}
                9579816  105.304    0.000  105.304    0.000 {method 'addcmul_' of 'torch._C._TensorBase' objects}
                1999218   51.873    0.000  103.482    0.000 layers.py:33(reset)
                1596636    2.380    0.000   98.961    0.000 loss.py:445(forward)
                1596636    8.597    0.000   96.581    0.000 functional.py:2637(mse_loss)
              181326532   70.318    0.000   96.032    0.000 layer.py:94(add)
               95798282   38.858    0.000   95.572    0.000 {built-in method builtins.any}
                3991590   94.606    0.000   94.606    0.000 {method 'eq' of 'torch._C._TensorBase' objects}
                1999218   13.845    0.000   89.530    0.000 level.py:41(notUsed)
                4796754   34.309    0.000   87.595    0.000 random.py:315(sample)
                9579816   84.529    0.000   84.529    0.000 {method 'zero_' of 'torch._C._TensorBase' objects}
              283615130   59.438    0.000   84.138    0.000 enum.py:646(__hash__)
              367118339   74.120    0.000   74.120    0.000 layer.py:110(elements)
                 798310   26.047    0.000   73.547    0.000 exploration.py:53(softmaxer)
               97961682   66.596    0.000   66.596    0.000 level.py:32(inverse)
                1596636   65.271    0.000   65.271    0.000 {built-in method torch._C._nn.mse_loss}
              119953080   43.378    0.000   64.716    0.000 levels.py:31(<genexpr>)
              632191360   58.259    0.000   58.259    0.000 layer.py:63(positions)
               82139598   40.034    0.000   57.945    0.000 random.py:250(_randbelow_with_getrandbits)
              184411803   44.867    0.000   55.711    0.000 overrides.py:1083(<genexpr>)
               77082388   36.518    0.000   54.557    0.000 layer.py:90(remove)
        431047064/431047063   34.823    0.000   48.874    0.000 {built-in method builtins.len}
                5588202   48.551    0.000   48.551    0.000 {method 't' of 'torch._C._TensorBase' objects}
                2394954   48.470    0.000   48.470    0.000 {built-in method sum}
                6386528   45.734    0.000   45.734    0.000 {method 'flatten' of 'torch._C._TensorBase' objects}
              567203317   44.798    0.000   44.798    0.000 {method 'append' of 'list' objects}
                5588210    4.660    0.000   43.512    0.000 flatten.py:39(forward)
               31987488   15.412    0.000   43.352    0.000 random.py:285(choice)
                1596636    7.250    0.000   41.903    0.000 __init__.py:28(_make_grads)
                 798318    3.110    0.000   38.394    0.000 exploration.py:47(epsilonGreedy)
               34327728   33.879    0.000   33.879    0.000 {built-in method torch._C._get_tracing_state}
                1596636   32.930    0.000   32.930    0.000 {built-in method ones_like}
                 798319   32.395    0.000   32.395    0.000 {built-in method nonzero}
                1756276   32.288    0.000   32.288    0.000 {method 'long' of 'torch._C._TensorBase' objects}
              195854249   31.475    0.000   31.475    0.000 {method 'add' of 'set' objects}


# Other prints


------------------------------------------------------------
Sender: LSF System <lsfadmin@n-62-20-15>
Subject: Job 9434612: <simul_gold_9x9_1> in cluster <dcc> Done

Job <simul_gold_9x9_1> was submitted from host <n-62-30-8> by user <s183905> in cluster <dcc> at Thu Mar 18 20:16:27 2021
Job was executed on host(s) <n-62-20-15>, in queue <gpuv100>, as user <s183905> in cluster <dcc> at Thu Mar 18 20:16:29 2021
</zhome/ee/d/137643> was used as the home directory.
</zhome/ee/d/137643/Desktop/Bachelor/Bachelorprojekt/Utils> was used as the working directory.
Started at Thu Mar 18 20:16:29 2021
Terminated at Fri Mar 19 00:11:42 2021
Results reported at Fri Mar 19 00:11:42 2021

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

    CPU time :                                   14070.77 sec.
    Max Memory :                                 2435 MB
    Average Memory :                             2431.36 MB
    Total Requested Memory :                     8192.00 MB
    Delta Memory :                               5757.00 MB
    Max Swap :                                   -
    Max Processes :                              4
    Max Threads :                                8
    Run time :                                   14159 sec.
    Turnaround time :                            14115 sec.

The output (if any) is above this job summary.

